from collections import UserDict
import pickle


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Title(Field):
    pass
    # @property
    # def value(self) -> str:
    #   return self.__value
    #
    # @value.setter
    # def value(self, value: str):
    #   max_title_length = 20
    #
    #   if len(value) > max_title_length:
    #     raise AttributeError(f"The note title is too long, be sure it is less then {max_title_length} symbols")
    #   elif value[0].lower() in Translator.CYRILLIC_SYMBOLS:
    #     print("All cyrillic letters will be translated to latin:")
    #     self.__value = Translator(value).translate_text()


class Note(Field):

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = Translator(value).translate_text()


class Tag(Field):

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = Translator(value).translate_text()


class Translator:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

    def __init__(self, text):
        self.text = text

    def translate_text(self):
        TRANSLATION = (
            "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
        TRANS = {}

        CYRILLIC = tuple([char for char in self.CYRILLIC_SYMBOLS])

        for cyrillic, latin in zip(CYRILLIC, TRANSLATION):
            TRANS[ord(cyrillic)] = latin
            TRANS[ord(cyrillic.upper())] = latin.upper()

        return self.text.translate(TRANS)


class Record:

    def __init__(self, title: str, note=None, tag=None):
        self.title = title
        if note is None:
            self.tag = []
            self.note = [{"note": "", "tag": self.tag}]
        else:
            self.tag = [tag]
            self.note = [{"note": str(note), "tag": self.tag}]

    def add_note(self, new_note):
        self.note[0]["note"] += " " + str(new_note)

    def add_tag(self, new_tag):
        if new_tag in self.note[0]["tag"]:
            print(f'The tag: "{new_tag}" is already used')
        else:
            self.note[0]["tag"].append(new_tag)

    def find_note(self, tag_value):
        all_tags = []
        for i in self.note[0]["tag"]:
            all_tags.append(str(i))

        if tag_value in all_tags:
            print('-' * 50, "The note you are looking for looks like:", sep='\n')
            print(self.note[0]["note"], '-' * 50, sep='\n')
            return self.note[0]["note"]

    def delete_note(self, tag_value):
        if tag_value in self.note[0]["tag"]:
            print(f"The note with a tag {tag_value} will be deleted from the notebook")

    def __str__(self) -> str:
        v_note = ''
        for i in self.note:
            for k, v in i.items():
                if k == 'note':
                    v_note = v
                return '{:<6} :'.format('Title') + f' {self.title}\n' \
                       '{:<6} :'.format('Note') + f' {v_note}\n' \
                       '{:<6} :'.format('Tag') + f' {self.tag}\n'


class NoteBook(UserDict):

    def add_record(self, record: list):
        self.data[record.title] = record

    def delete_record(self, record):
        del self.data[record.title]

    def iterator(self, func=None):
        index, print_block = 1, '-' * 50 + '\n'
        for record in self.data.values():
            if func is None or func(record):
                print_block += str(record) + '\n'
                if index < 1:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, input_nb):
        try:
            return self.func(input_nb)
        except IndexError:
            return 'Error! Print correct data!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Data is incorrect!'
        except AttributeError:
            return "AttributeError"
        except TypeError:
            return 'Error! Give me only 1 command'


# "****************************************"
# "************ get NoteBook  *************"
# "****************************************"

file_name = 'NoteBook.bin'


def save_nb(nb):
    with open(file_name, "wb") as fh:
        pickle.dump(nb, fh)


def load_nb():
    try:
        with open(file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
    except (EOFError, FileNotFoundError):
        unpacked = NoteBook()
        return unpacked


# "****************************************"
# "******** functional commands  **********"
# "****************************************"

@InputError
def add(input_nb):
    print("You are going to create a new record in your note book.")
    input_title = input("Please add the title of your note: ")
    while input_title == "":
        print("You must give a note title, other way  you cannot create a note record!")
        input_title = input("Please add the title of your note: ")
    input_note = input("What is your note: ")
    input_tag = input("Specify a tag of your note: ")
    if input_note and input_tag:
        title = Title(input_title)
        input_record = Record(str(title), Note(input_note), Tag(input_tag))
    elif input_note and input_tag == "":
        input_record = Record(Title(input_title), Note(input_note))
    else:
        input_record = Record(Title(input_title))
    input_nb.add_record(input_record)
    save_nb(input_nb)
    return f'The Note add successfully'


@InputError
def tag(input_nb):
    all_nb_titles = list(input_nb.keys())
    print(f"Here is all titles in your notebook:\n{all_nb_titles}")
    input_title = input("Specify the title of the note, where you want to add a new tag: ")
    if input_title in all_nb_titles:
        input_tag = input("Which tag do you want to add: ")
        input_nb[input_title].add_tag(input_tag)
        save_nb(input_nb)
        return f'The tag: "{input_tag}" add successfully'
    else:
        return f"No note with a title '{input_title}' was found"


# @InputError
# def find_records(input_nb):
#     output_nb = []
#     articles_dict_with_key = []
#     count_match = 0
#     letter_case = input("Give a key word to find a match in the notes: ")
#     for tup in list(input_nb.items()):
#         output_nb.append(dict([tup]))
#         nb_dict = dict([tup])
#         for key, value in nb_dict.items():
#             words_in_dict = [key.lower(), value.note[0]["note"].lower()]
#             for i in value.note[0]["tag"]:
#                 words_in_dict.append(str(i))
#
#             if any(letter_case.lower() in s for s in words_in_dict):
#                 articles_dict_with_key.append(tup)
#                 count_match += 1
#     print(f"The given key words '{letter_case}' were found in {count_match} note books")
#     print(f"The matches are : {articles_dict_with_key}")

@InputError
def find_records(input_nb):
    output_nb = []
    articles_dict_with_key = []
    count_match = 0
    letter_case = input("Give a key word to find a match in the notes: ")
    for tup in list(input_nb.items()):
        output_nb.append(dict([tup]))
        nb_dict = dict([tup])
        for key, value in nb_dict.items():
            words_in_dict = [key.lower(), value.note[0]["note"].lower()]
            for i in value.note[0]["tag"]:
                words_in_dict.append(str(i))

            if any(letter_case.lower() in s for s in words_in_dict):
                articles_dict_with_key.append(tup)
                count_match += 1
    if count_match == 0:
        result = f'Matches not found'
    else:
        result = f"The given key words '{letter_case}' were found in {count_match} note books\n"
    for i in articles_dict_with_key:
        result += f'{i[1]}\n'
    return result


@InputError
def find_note_by_tag(input_nb):
    print("List of all tags:")
    for rec, value in input_nb.items():
        print('{:<15}  {:<10}  {:<10}'.format(rec, '-> tags:', str(value.note[0]["tag"])))

    input_tag = input("Give a tag to find a corresponding notes: ")
    notes_with_tag = []
    for rec, value in input_nb.items():
        notes_with_tag.append(value.find_note(input_tag))

    if all(v is None for v in notes_with_tag):
        print(f"Cannot find a note using the tag: '{input_tag}'")
    return ''


@InputError
def delete_note(input_nb):
    all_nb_titles = list(input_nb.keys())
    print(f"Here is all titles in your notebook:\n{all_nb_titles}")
    input_title = input("Specify the title of the note that should be deleted: ")
    if input_title in all_nb_titles:
        input_nb.delete_record(input_nb[input_title])
        save_nb(input_nb)
        return f"The note with a title '{input_title}' is deleted"
    else:
        return f"No note with a title '{input_title}' was found"


@InputError
def edit_note(input_nb):
    all_nb_titles = list(input_nb.keys())
    print(f"Here is all titles in your notebook:\n{all_nb_titles}")
    input_title = input("Specify the title of the note that should be edited: ")
    if input_title in all_nb_titles:
        input_note = input("What is a new note: ")
        for key, value in input_nb.items():
            if key == input_title:
                old_note = value.note[0]['note']
                value.note[0]['note'] = input_note
                save_nb(input_nb)
                return f"Note: '{old_note}' is changed to: '{value.note[0]['note']}'."
    else:
        return f"No note with a title '{input_title}' was found"


@InputError
def clean_all(input_nb):
    yes_no = input('Are you sure you want to delete all notes? (y/n) ')
    if yes_no == 'y':
        input_nb.clear()
        save_nb(input_nb)
        return 'Notebook is empty'
    else:
        return 'Removal canceled'


@InputError
def show_all(input_nb):
    if not input_nb:
        return 'NoteBook is empty'
    result = 'List of all notes:\n'
    print_list = input_nb.iterator()
    for item in print_list:
        result += f'{item}'
    return result


# "****************************************"
# "********** helping commands  ***********"
# "****************************************"

def greeting(*args):
    return 'Hello! Can I help you?'


def exiting(input_nb):
    save_nb(input_nb)
    return 'Good bye!'


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def helping(*args):
    return """
    *********** Service command ***********
    "help", "?"          --> Commands list
    "close", "exit", "." --> Exit from AddressBook
    *********** Add/edit command **********
    add --> add new note record
    tag --> add new tag to the note record
    edit note --> change an old note to a new one
    *********** Info command *************
    find notes --> find notes by Key Word
    find by tag --> find note by tag
    show all --> show data of all notes
    *********** Delete command ***********
    delete note --> delete note record
    clean all --> delete all notes
    """


COMMANDS = {greeting: ['hello'],
            helping: ['help', 'h', '?'],
            add: ['add'],
            tag: ['tag'],
            find_records: ['find notes'],
            find_note_by_tag: ['find by tag'],
            delete_note: ['delete note'],
            edit_note: ['edit note'],
            show_all: ['show'],
            clean_all: ['clear', 'clean', 'clean all'],
            exiting: ['goodbye', 'close', 'exit', '.']
            }


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    input_nb = load_nb()
    print(helping())
    while True:
        user_command = input("Enter command:>>> ")
        if user_command == "exit":
            return f"Exit"
        command, data = command_parser(user_command)
        print(command(input_nb))

        if command is exiting:
            break
