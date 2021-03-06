def fizz(number):
    return not number % 3


def buzz(number):
    return not number % 5


def fizz_buzz(to):
    for number in range(1, to + 1):
        answer = ''
        if fizz(number):
            answer += 'fizz'
        if buzz(number):
            answer += 'buzz'

        if answer != '':
            print(answer)
        else:
            print(number)


fizz_buzz(20)  # Play to 20
# expecting fizz: 3, 6, 9, 12, 18
# expecting buzz: 5, 10, 20
# expecting fizzbuzz: 15
