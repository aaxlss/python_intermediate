def division(num):
    return [number for number in range(1, num + 1) if num % number == 0]

def run():
    try:
        num = int(input('Insert a number: '))
        if num <= 0:
            raise Exception('Number not allow')
        print(division(num))
    except ValueError as v:
        print(v)
        print('Numbers are just allow')
    except Exception as e:
        print(e)
        print('Number must be greater that 0')
if __name__ == '__main__':
    run()