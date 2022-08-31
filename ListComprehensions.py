def run():
    
    """
        common way to create a list with a loop
    """
    # list = []
    # for i in range(1,101):
    #     list.append(i ** 2)

    # print(f'List items: {list}')

    #comprehension way to create list with items

    list = [ i ** 2 for i in range(1, 100) if i % 2 == 0]
    print(f'comprehension list: {list}')

    challenge_list = [ i for i in range(1, 10000) if i % 36 == 0]

if __name__ == '__main__':
    run()