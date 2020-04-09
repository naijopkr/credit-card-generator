import credit_card_generator as cdg
import sys, getopt

def help():
    print('Generate credit card number:')
    print('credit-card-generator [-t] <card_type>')
    print()
    print('Validate credit card number:')
    print('credit-card-generator -v <card-number>')
    print()
    print('\t-t\tspecify card type (optional)')
    print('\t-v\tvalidate card number')
    print()
    sys.exit()


def validate_card(card):
        try:
            card_type = cdg.get_card_type(card)
        except ValueError as err:
            print(err)
        else:
            print('This is a valid card.')
            print(f'Card flag: {card_type}')

        sys.exit()


def generate_card(card_type = None):
    card = cdg.generate_credit_card(card_type)
    card_flag = cdg.get_card_type(card)
    print(f'Card number: {card}')
    print(f'Flag: {card_flag}')
    sys.exit()


def main(argv):
    try:
        opts, _args = getopt.getopt(argv, 'hv:t:')

        if not (opts):
            generate_card()

        for opt, value in opts:
            if (opt == '-v'):
                validate_card(value)

            if (opt == '-t'):
                generate_card(value)

            if (opt == '-h'):
                help()

            print(f'Option \'{opt}\' does not exits.\n')
            help()
            sys.exit()

    except getopt.GetoptError:
        help()

if __name__ == '__main__':
    main(sys.argv[1:])
