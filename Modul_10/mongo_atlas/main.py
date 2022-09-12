from models import Note, Record, Tag
from models import connect

# подсчитаем объекты в коллекциях
notes_count = Note.objects.count()

# если нет объектов в коллекциях, создать один
if not notes_count:
    # сначала - создать объект Tag
    tag = Tag(name='Покупки')
    # потом - создание объектов Record
    record1 = Record(description='Покупка колбасы')
    record2 = Record(description='Покупка молока')
    record3 = Record(description='Покупка масла')
    #  Последнее, создаем объект Note и сохраняем его
    Note(name='Поход в магазин', records=[record1, record2, record3], tags=[tag, ]).save()

# подсчитаем объекты
notes_count = Note.objects.count()
print(notes_count)

# найдем объект по имени
note = Note.objects(name='Поход в кино')

# если объекта нет - создаем его
if not note:
    note = Note(name='Поход в кино', records=[Record(description='Сходил на Мстителей'), ], tags=[Tag(name='Развлечения'), ]).save()
else:
    # если объект существует - удаляем его
    note.delete()

# снова считаем объекты
notes_count = Note.objects.count()
print(notes_count)

# найдем все записи
notes = Note.objects()
print("-------------------")
for note in notes:
    print(f"id={note.id}")
    print(f"name={note.name}")
    print(f"date={note.created}")
    print("Записи:")
    for record in note.records:
        print(record.description)
        print(record.done)
    print("Теги:")
    for tag in note.tags:
        print(tag.name)
    print("-------------------")
