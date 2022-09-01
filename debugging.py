def division(num):
    return [number for number in range(1, num + 1) if num % number == 0]

def run():
    num = int(input('Insert a number: '))
    print(division(num))

if __name__ == '__main__':
    run()