from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
GIF_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
XLS_DOCUMENT = []
CSV_DOCUMENT = []
PPTX_DOCUMENT = []

OTHER = []
APP_PROGRAMS = []
PY_PROGRAMS = []
HTML_PROGRAMS = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
RAR_ARCHIVES = []
ARJ_ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'GIF': GIF_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'MP4': MP4_VIDEO,
    'AVI': AVI_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'XLS': XLS_DOCUMENT,
    'CSV': CSV_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
    'RAR': RAR_ARCHIVES,
    'ARJ': ARJ_ARCHIVES,
    'APP': APP_PROGRAMS,
    'PY': PY_PROGRAMS,
    'HTML': HTML_PROGRAMS

}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    file_list = sorted(folder.glob("**/*"))
    sorter(file_list, folder)


def sorter(file_list, folder):
    for i in range(len(file_list)):
        item = file_list[i]
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'programs', 'OTHER'):
                FOLDERS.append(item)
            continue
        ext = get_extension(item.name)
        fullname = item
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)
