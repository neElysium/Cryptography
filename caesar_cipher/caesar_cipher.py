def caesar_cipher(text, shift, encrypt=True):
    """
    Performs a Caesar cipher encryption or decryption.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The number of positions to shift the alphabet.
        encrypt (bool): True to encrypt, False to decrypt.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character
            if encrypt:
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result


if __name__ == "__main__":
    # Example usage
    plaintext = "HELLO WORLD"
    shift = 3
    ciphertext = caesar_cipher(plaintext, shift, encrypt=True)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)

    # Decryption
    decrypted_text = caesar_cipher(ciphertext, shift, encrypt=False)
    print("Decrypted text:", decrypted_text)
