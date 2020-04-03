import re

def is_valid(card_number):
    card_sum = 0
    if not re.search(r'^\d+$', card_number):
        raise ValueError('Invalid card number!')

    for i in range(len(card_number)):
        if i % 2 == 0:
            new_digit = int(card_number[i])*2

            if new_digit > 9:
                new_digit = new_digit - 9

            card_sum += new_digit
        else:
            card_sum += int(card_number[i])

    return card_sum % 10 == 0


def get_card_type(card_number):
    if not is_valid(card_number):
        raise ValueError('Invalid card number')


def generate_credit_card():
    pass


if __name__ == '__main__':
    output = is_valid(input('Credit card number: '))
    print(output)
