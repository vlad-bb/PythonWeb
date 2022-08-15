import asyncio
from pathlib import Path

from logger import get_logger
from aiopath import AsyncPath
from typing import Dict, List, Tuple
from time import time
from register_extensions import REGISTER_EXTENSIONS

logger = get_logger(__name__)


def get_file_list(folder):
    file_list = sorted(folder.glob("**/*"))
    return file_list


async def sorter(folder) -> Dict[Tuple[str, str], List[AsyncPath]]:
    file_list = get_file_list(folder)
    # logger.info(f'file_list {file_list}')
    result_dict = {}
    for file in [files for files in file_list if files.is_file()]:
        ext = file.suffix[1:].upper()
        file_type = REGISTER_EXTENSIONS.get(ext, "other")
        if result_dict.get((ext, file_type)):
            result_dict[(ext, file_type)].append(file)
        else:
            result_dict[(ext, file_type)] = [file]
    # logger.info(f'result_dict{result_dict}')
    return result_dict


def get_bad_folders(folder: AsyncPath) -> List[AsyncPath]:
    folder_list = [
        folder
        for folder in folder.glob("*")
        if folder.is_dir() and folder.name not in set(REGISTER_EXTENSIONS.values())
    ]

    bad_folders_list = [list(Path(folder).glob("**/*")) for folder in folder_list]
    for lst in bad_folders_list:
        if lst:
            folder_list.extend(lst)

    return folder_list


def remove_folders(folders: List[AsyncPath]):
    positiv_result = []
    negativ_result = []
    for folder in folders[::-1]:
        try:
            folder.rmdir()
            positiv_result.append(folder.name)
        except OSError:
            negativ_result.append(folder.name)
    return positiv_result, negativ_result


async def file_parser(folder_for_scan):
    star = "*" * 60
    try:
        sorted_file_dict = await sorter(folder_for_scan)
    except FileNotFoundError:
        return (
            f"Not able to find '{folder_for_scan}' folder. Please enter a correct folder name."
        )
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return "Unknown file "
    for file_types, files in sorted_file_dict.items():
        for file in files:
            if not (folder_for_scan / file_types[1]).exists():
                (folder_for_scan / file_types[1]).mkdir()
            if not (folder_for_scan / file_types[1] / file_types[0]).exists():
                (folder_for_scan / file_types[1] / file_types[0]).mkdir()
            file.replace(folder_for_scan / file_types[1] / file_types[0] / file.name)

    old_folder_list = get_bad_folders(folder_for_scan)
    positive, negative = remove_folders(old_folder_list)
    str_positive = "\n".join(positive)
    str_negative = "\n".join(negative)
    print(
        f"{star}"
        "\n"
        f"Files in {folder_for_scan} sorted succesffully"
        "\n"
        f"Folders that are deleted: {str_positive}"
        "\n"
        f"Folders that are not deleted:{str_negative}"
        "\n"
        f"{star}"
    )


async def main(path):
    path = Path(path).resolve()
    # a_path = AsyncPath(path)
    await asyncio.gather(file_parser(path), return_exceptions=False)
    # logger.info(f'main result {result}')


if __name__ == "__main__":
    """ Speed test work with asyncio """
    timer = time()
    # logger.info(f'time {time()}')
    asyncio.run(main('/Users/admin/Desktop/test'))
    print(f'Speed test work with asyncio {round(time() - timer, 4)}')
