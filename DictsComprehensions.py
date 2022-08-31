def run():
    # my_dict = {}
    # for i in range(1, 100):
    #     if i % 3 != 0:
    #         my_dict[i] = i ** 2

    # print(f'dictionary: {my_dict}')

    my_dictionary = { i:i**3 for i in range(1, 100) if i % 3 != 0}
    print(f'comprehension dictionary: {my_dictionary}')

    # challenge
    my_dictionary_challenge = { i:i**0.5 for i in range(1, 1001)}
    print(f'dictionary challenge: {my_dictionary_challenge}')
if __name__ == '__main__':
    run()
