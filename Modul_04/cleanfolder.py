from file_parser import *
from normalize import normalize


def goodbye(*args):
    return 'Good bye!'


def handle_media(filename: Path, target_folder: Path):
    filename = Path(filename)
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


def handle_other(filename: Path, target_folder: Path):
    try:
        filename = Path(filename)
        target_folder.mkdir(exist_ok=True, parents=True)
        filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))
    except IsADirectoryError:
        return 'IsADirectoryError'
    except FileNotFoundError:
        return 'FileNotFoundError'
    except PermissionError:
        return 'PermissionError'


def handle_archive(filename: Path, target_folder: Path):
    filename = Path(filename)
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


def handle_programs(filename: Path, target_folder: Path):
    try:
        filename = Path(filename)
        target_folder.mkdir(exist_ok=True, parents=True)
        filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))
    except IsADirectoryError:
        return 'IsADirectoryError'
    except FileNotFoundError:
        return 'FileNotFoundError'
    except PermissionError:
        return 'PermissionError'


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Folder deletion failed {folder}")


def file_parser(*args):
    star = '*' * 60
    try:
        folder_for_scan = Path(args[0])
        scan(folder_for_scan.resolve())
    except FileNotFoundError:
        return f"Not able to find '{args[0]}' folder. Please enter a correct folder name."
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return 'Unknown file '
    for file in JPEG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPEG'))
    for file in JPG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPG'))
    for file in PNG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'PNG'))
    for file in SVG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'SVG'))
    for file in GIF_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'GIF'))
    for file in MP3_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'MP3'))
    for file in OGG_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'OGG'))
    for file in WAV_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'WAV'))
    for file in AMR_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'AMR'))
    for file in AVI_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'AVI'))
    for file in MP4_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MP4'))
    for file in MOV_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MOV'))
    for file in MKV_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MKV'))
    for file in DOC_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'DOC'))
    for file in DOCX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'DOCX'))
    for file in TXT_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'TXT'))
    for file in PDF_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'PDF'))
    for file in XLSX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'XLSX'))
    for file in XLS_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'XLS'))
    for file in CSV_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'CSV'))
    for file in PPTX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'PPTX'))
    for file in OTHER:
        handle_other(file, Path(args[0] + '/' + 'other'))
    for file in APP_PROGRAMS:
        handle_programs(file, Path(args[0] + '/' + 'programs' + '/' + 'APP'))
    for file in PY_PROGRAMS:
        handle_programs(file, Path(args[0] + '/' + 'programs' + '/' + 'PY'))
    for file in HTML_PROGRAMS:
        handle_programs(file, Path(args[0] + '/' + 'programs' + '/' + 'HTML'))
    for file in ZIP_ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'ZIP'))
    for file in GZ_ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'GZ'))
    for file in TAR_ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'TAR'))
    for file in RAR_ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'RAR'))
    for file in ARJ_ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'ARJ'))
    for folder in FOLDERS[::-1]:
        handle_folder(folder)

    return f'{star}''\n'f"Files in {args[0]} sorted succesffully"'\n'f'{star}'


COMMANDS = {file_parser: ['clean', 'clear'], goodbye: ['good bye', 'close', 'exit', '.']}


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def command_parser(user_command: str, COMMANDS: dict) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    while True:
        print('Print clean and address your folder',
              'for MacOS: clean /Folder/Trash',
              'for Windows: clean C:\Folder\Trash', sep='\n')
        user_command = input('Enter you command >>> ')
        command, data = command_parser(user_command, COMMANDS)
        print(command(*data))
        print('Do you have some folder for clean?')
        var = input('Press: y/n >>> ')
        if var == 'y':
            print('*' * 60)
            continue
        elif var == 'n':
            break
        elif command is goodbye:
            break


if __name__ == '__main__':
    main()