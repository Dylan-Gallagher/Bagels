# Bagels

import random


def run_tutorial():
    print("The computer guesses a three-digit number (no number repeats itself) and you have to guess what it is")


def generate_number():
    computers_number_list = [0] * 3
    for i in computers_number_list:
        while i < 3:
            chosen_number = random.randint(0, 9)
            if chosen_number not in computers_number_list:
                computers_number_list[i] = chosen_number
                i += 1
    number = ''
    for i in computers_number_list:
        number += str(i)
    number = int(number)
    return number


def get_user_input():
    number = input("Enter your guess: ")
    return number


def has_won(num, ai_num):
    if int(num) == ai_num:
        return True
    else:
        return False


def make_clues(num, ai_num):
    computers_number_list = list(map(int, str(ai_num)))
    players_number_list = list(map(int, str(num)))

    bagels = True
    clues = []
    i = 0
    while i < 3:
        if players_number_list[i] in computers_number_list:
            bagels = False
            if players_number_list[i] == computers_number_list[i]:
                clues.append("Fermi ")
            else:
                clues.append("Pico ")
        i += 1
    if bagels:
        clues.append("Bagels ")

    return clues


def sort_clues(arr):
    arr.sort()
    string = ""
    for i in arr:
        string += i
    return string

print("Welcome to to Bagels")

tutorial = input("Do you want a quick tour of the game? ").lower()

if tutorial.startswith("y"):
    run_tutorial()

computers_number = generate_number()
# print("computers number:", computers_number)

while True:

    users_number = get_user_input()

    if has_won(users_number, computers_number):
        print("You have won!")
        break

    unsorted_clues = make_clues(users_number, computers_number)
    sorted_clues = sort_clues(unsorted_clues)
    print(sorted_clues)









