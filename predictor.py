import random

MAX_LEN = 100

def convert_number_to_triade(number):
    res = ""
    while number > 0:
        dig = number % 2
        res = str(dig) + res
        number = number // 2

    while len(res) < 3:
        res = '0' + res
    return res

def get_triada_dict(result):
    triada_dict = {}

    for i in range(8):
        triada = convert_number_to_triade(i)
        triada_dict[triada] = [0, 0]

    for i in range(0, len(result) - 3):
        cur_triada = result[i:i + 3]
        if result[i + 3] == "0":
            triada_dict[cur_triada][0] += 1
        else:
            triada_dict[cur_triada][1] += 1

    return triada_dict

def generate_first_triada():
    first_triada = ""
    for i in range(3):
        first_triada += str(random.randint(0, 1))
    return first_triada


print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")

result = ""
while True:
    print("Print a random string containing 0 or 1:\n")
    text = input()
    text_to_add = ""
    for c in text:
        if c in ('0', '1'):
            text_to_add += c
    result += text_to_add
    res_len = len(result)
    if res_len < MAX_LEN:
        print(f"Current data length is {res_len}, {MAX_LEN - res_len} symbols left")
        # print("Print a random string containing 0 or 1:\n")
    else:
        break

print("Final data string:")
print(result)

triada_dict = get_triada_dict(result)

print("\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
balance = 1000

while True:
    print("\nPrint a random string containing 0 or 1:")

    test_string = input()

    if test_string == "enough":
        break

    check = True
    for c in test_string:
        if not c in ('0', '1'):
            check = False

    if not check:
        continue

    triada_dict = get_triada_dict(test_string)

    first_triada = generate_first_triada()

    prediction = first_triada
    guessed_count = 0
    for i in range(3, len(test_string)):
        probabilities = triada_dict[test_string[i - 3: i]]
        if probabilities[0] > probabilities[1]:
            prediction += '0'
        elif probabilities[0] < probabilities[1]:
            prediction += '1'
        else:
            prediction += str(random.randint(0, 1))

        if prediction[i] == test_string[i]:
            guessed_count += 1

    print("prediction:")
    print(prediction)

    number_of_guessed = len(test_string) - 3
    currency = guessed_count / number_of_guessed * 100
    print(f"\nComputer guessed right {guessed_count} out of {number_of_guessed} symbols ({round(currency, 2)} %)")

    lose_count = guessed_count
    win_count = number_of_guessed - lose_count
    balance += win_count - lose_count
    print(f"Your balance is now ${balance}")

print("Game over!")

