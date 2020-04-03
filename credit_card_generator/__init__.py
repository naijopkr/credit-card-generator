from random import randint
import re

def card_sum(card_number):
    total_sum = 0
    if not re.search(r'^\d+$', card_number):
        raise ValueError('Invalid card number!')

    for i in range(len(card_number)):
        if i % 2 == 0:
            new_digit = int(card_number[i])*2

            if new_digit > 9:
                new_digit = new_digit - 9

            total_sum += new_digit
        else:
            total_sum += int(card_number[i])

    return total_sum


def is_valid(card_number):
    return card_sum(card_number) % 10 == 0


def get_card_type(card_number):
    if not is_valid(card_number):
        raise ValueError('Invalid card number')


# TODO: GENERATE BASED ON CARD TYPE
def generate_credit_card(type = 'visa'):
    card_number = '4'
    for i in range(14):
        card_number += str(randint(0, 9))

    digits_sum = card_sum(card_number)

    card_number += str(digits_sum % 10)

    print(card_number)
    print(is_valid(card_number))


if __name__ == '__main__':
    generate_credit_card()
