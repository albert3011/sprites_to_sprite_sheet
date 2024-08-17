def generate_pic():
    import os
    from math import ceil
    from PIL import Image

    f = open('path.txt', encoding="utf-8")
    directory = f.read()

    print(f'Директория - {directory}')

    files = os.listdir(directory)

    print(f'Список файлов - {files}')
    print(f'Количество файлов - {len(files)}')

    img = Image.open(f'{directory}\\{files[0]}')

    print(f"Ширина одной картинки: {img.width}")
    print(f"Высота одной картинки: {img.height}")

    columns = 12

    if len(files) > columns and len(files) % columns == 0:
        result_height = int(len(files) / columns * img.height)
    elif len(files) == columns:
        result_height = img.height
    elif len(files) > columns and len(files) % columns != 0:
        result_height = int(ceil(len(files) / columns) * img.height)
    else:
        result_height = img.height
        columns = len(files)

    print(f'Высота результата - {result_height}')
    result_width = columns * img.width
    print(f'Ширина результата - {result_width}')

    picture = Image.new('RGBA', (result_width, result_height))

    row = 0
    column = 0
    for i in range(0, len(files)):
        img = Image.open(f'{directory}/{files[i]}')
        pos_x = img.width * column
        pos_y = img.height * row
        picture.paste(img, (pos_x, pos_y))
        if column < columns - 1:
            column += 1
        else:
            column = 0
            row += 1

    picture.save('result.png')
    print('Результат сохранён.\nCreated by Albert_OS')
