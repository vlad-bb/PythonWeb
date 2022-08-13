import asyncio

from aiopath import AsyncPath
from typing import Dict, List, Tuple
from time import time
from register_extensions import REGISTER_EXTENSIONS


async def sorter(folder) -> Dict[Tuple[str, str], List[AsyncPath]]:
    file_list = await sorted(folder.glob("**/*"))
    result = {}
    async for file in [files for files in file_list if files.is_file()]:
        ext = await file.suffix[1:].upper()
        file_type = await REGISTER_EXTENSIONS.get(ext, "other")
        if result.get((ext, file_type)):
            result[(ext, file_type)].append(await file)
        else:
            result[(ext, file_type)] = [file]
    return await result


async def get_bad_folders(folder: AsyncPath) -> List[AsyncPath]:
    folder_list = [
        folder
        async for folder in folder.glob("*")
        if folder.is_dir() and folder.name not in set(REGISTER_EXTENSIONS.values())
    ]

    bad_folders_list = [list(await folder.glob("**/*")) async for folder in folder_list]
    async for lst in bad_folders_list:
        if lst:
            folder_list.extend(await lst)

    return await folder_list


async def remove_folders(folders: List[AsyncPath]):
    positiv_result = []
    negativ_result = []
    async for folder in folders[::-1]:
        try:
            await folder.rmdir()
            positiv_result.append(await folder.name)
        except OSError:
            negativ_result.append(await folder.name)
    return await positiv_result, await negativ_result


async def file_parser(*args):
    star = "*" * 60
    try:
        folder_for_scan = AsyncPath(args[0])
        sorted_file_dict = sorter(folder_for_scan.resolve())
    except FileNotFoundError:
        return (
            f"Not able to find '{args[0]}' folder. Please enter a correct folder name."
        )
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return "Unknown file "
    for file_types, files in sorted_file_dict.items():
        async for file in files:
            if not (folder_for_scan / file_types[1]).exists():
                await (folder_for_scan / file_types[1]).mkdir()
            if not (folder_for_scan / file_types[1] / file_types[0]).exists():
                await (folder_for_scan / file_types[1] / file_types[0]).mkdir()
            await file.replace(folder_for_scan / file_types[1] / file_types[0] / file.name)

    old_folder_list = await get_bad_folders(folder_for_scan)
    positive, negative = await remove_folders(old_folder_list)
    str_positive = "\n".join(positive)
    str_negative = "\n".join(negative)
    return await (
        f"{star}"
        "\n"
        f"Files in {args[0]} sorted succesffully"
        "\n"
        f"Folders that are deleted: {str_positive}"
        "\n"
        f"Folders that are not deleted:{str_negative}"
        "\n"
        f"{star}"
    )


async def main(path: AsyncPath):
    r = await asyncio.gather(file_parser(path), return_exceptions=True)
    return r

if __name__ == "__main__":
    """ Speed test work with asyncio """
    timer = time()
    result = asyncio.run(main(AsyncPath('/Users/admin/Desktop/test')))
    print(result)
    print(f'Speed test work with asyncio {round(time() - timer, 4)}')