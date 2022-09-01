def division(num):
    return [number for number in range(1, num + 1) if num % number == 0]

def run():
    #Validatin error swith try, except, raise
    # try:
    #     num = int(input('Insert a number: '))
    #     if num <= 0:
    #         raise Exception('Number not allow')
    #     print(division(num))
    # except ValueError as v:
    #     print(v)
    #     print('Numbers are just allow')
    # except Exception as e:
    #     print(e)
    #     print('Number must be greater that 0')

    #Validating errors with assert statements

    num = input('Insert a number:')

    assert num.isnumeric() and int(num) <= 0, 'Numbers are just allow and greater than 0'
    
    division(int(num))
if __name__ == '__main__':
    run()