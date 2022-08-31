def run():
    my_list = [1, 'String', 1.5]
    my_dictionary = {
        'first_name': 'name'
    }

    super_list = [
        {'first_name': 'name'},
        {'first_name_1': 'name_1'},
        {'first_name_2': 'name_2'},
        {'first_name_3': 'name_3'},
        {'first_name_4': 'name_4'},
    ]

    super_dictionary = {
        'list_1': [1, 'String', 1.5],
        'list_2': [1, 'String', 1.5],
        'list_3': [1, 'String', 1.5],
        'list_4': [1, 'String', 1.5],
    }

    for key, value in super_dictionary.items():
        print(f'key: {key} - value: {value}')

    for item in super_list:
        print(f'items from super list: {item}')

if __name__ == '__main__':
    run()