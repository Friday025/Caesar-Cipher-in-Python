from ascii_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
    The function `caesar_cipher` encodes or decodes a message using the Caesar cipher algorithm based on
    a specified shift value and direction.
    
    :param text: The `text` parameter in the `caesar_cipher` function refers to the message that you
    want to encode or decode using the Caesar cipher algorithm. This text can be any string containing
    alphabetic characters that you want to shift by a certain value based on the shift value provided
    :param shift: The `shift` parameter in the `caesar_cipher` function represents the number of
    positions you want to shift the characters in the message. Positive values shift the characters to
    the right (encode), while negative values shift the characters to the left (decode) based on the
    alphabet
    :param direction: The `direction` parameter in the `caesar_cipher` function determines whether the
    message should be encoded or decoded based on the shift value. If the direction is "encode", the
    message will be shifted by the specified value. If the direction is "decode", the message will be
    shifted in the opposite
    :return: The function `caesar_cipher` returns the encoded or decoded message based on the shift
    value and direction specified.
    """
shift_value = int(input("Enter how many values you want to shift: "))

# Function to encode or decode a message based on the shift value
def caesar_cipher(text, shift, direction):
    result_message = ""
    if direction == "decode":
        shift = -shift
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result_message += alphabet[new_position]
        else:
            result_message += char
    return result_message

is_game = True

while is_game:
    st = input("Hey, enter your message here: ").lower()
    direction = input("What do you want to do, encode or decode: ").lower()

    if direction in ['encode', 'decode']:
        result_message = caesar_cipher(st, shift_value, direction)
        print(f"Your {direction}d message is: {result_message}")
    else:
        print("Invalid input. Please enter 'encode' or 'decode'.")

    is_continue = input("Want to continue this chat (y or n)? ").lower()
    if is_continue == "n":
        is_game = False

print("Goodbye!")
