def num_to_char(number):

    number_str = str(number)
    characters = []

    for digit in number_str:
        characters.append(chr(ord('0') + int(digit)))

    return ''.join(characters)

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    print(num_to_char(number))