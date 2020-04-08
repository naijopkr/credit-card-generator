from random import randint
import re
import json
import os

json_path = os.path.join(os.path.dirname(__file__), 'lib/card_types.json')


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

    with open(json_path) as cards_data:
        card_types = json.load(cards_data)

        card_flags = card_types.keys()
        possible_cards = set(card_flags)
        card_type_name = 'Not available'
        for card_flag in card_flags:
            print(f'Testing for: {card_flag}')
            candidate = card_types[card_flag]

            # Test length
            if not len(card_number) in candidate['lengths']:
                possible_cards.remove(card_flag)
                continue

            #Test patterns
            has_pattern = False
            for pattern in candidate['patterns']:
                if (isinstance(pattern, list)):
                    for num in range(pattern[0], pattern[1]):
                        if re.match(str(num), card_number):
                            has_pattern = True
                            break

                    if has_pattern:
                        break
                else:
                    if re.match(str(pattern), card_number):
                        has_pattern = True
                        break

            if has_pattern:
                card_type_name = candidate['niceType']
                break
            else:
                possible_cards.remove(card_flag)

    return card_type_name


def get_card_props(type):
    pass


# TODO: GENERATE BASED ON CARD TYPE
def generate_credit_card(type = 'visa'):
    card_number = '4'
    for i in range(14):
        card_number += str(randint(0, 9))

    digits_sum = card_sum(card_number)

    card_number += str((10 - digits_sum % 10) % 10)

    return card_number


if __name__ == '__main__':
    card = generate_credit_card()
    card_name = get_card_type(card)
    print(card_name)
