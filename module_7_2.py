def custom_write(file_name, strings):
    string_positions = {}
    file_a = open(file_name, 'a', encoding='utf-8')
    for index, lines in enumerate(strings, start=1):
        string_positions[index,file_a.tell()] = lines
        file_a.write(lines + '\n')
    file_a.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
