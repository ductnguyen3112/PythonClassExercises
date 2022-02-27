def greet():
    print("hello")


greet()


def greet_by_name(name):
    print(f'hello {name}')


def get_factorial(number):
    output = number
    for i in range(1, number):
        output *= i
        return output


a = get_factorial(5)
print(a)

games = ["Mario", "Tank", "Pikachu", "Fifa"]
# for game in games:
#    game += " suck!"
#    print(game)
#       print(games)
print(games[1])
print(games[1:])
print(games[:2])
print(games[1:4])
print(games[0:3:2])
print(games[::-1])

best = "Vancouver"
print(best[::-1])

games[1] = 'x'
print(best)


def get_evens_number(number):
    out = []

    for n in range(number):
        if n % 2 == 0:
            out.apprend(n)
        return out
    evens = get_evens_numer(10)
# print(evens[::-1])

