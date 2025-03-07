class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text, key):
        rail = [['' for _ in range(len(text))] for _ in range(key)]
        direction_down = False
        row, col = 0, 0
        for char in text:
            rail[row][col] = char
            col += 1
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        encrypted_text = ''.join([''.join(rail[i]) for i in range(key)])
        return encrypted_text

    def decrypt_text(self, cipher_text, key):
        rail = [['' for _ in range(len(cipher_text))] for _ in range(key)]
        direction_down = False
        row, col = 0, 0
        for _ in cipher_text:
            rail[row][col] = '*'
            col += 1
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        index = 0
        for i in range(key):
            for j in range(len(cipher_text)):
                if rail[i][j] == '*' and index < len(cipher_text):
                    rail[i][j] = cipher_text[index]
                    index += 1

        decrypted_text = []
        row, col = 0, 0
        for _ in cipher_text:
            decrypted_text.append(rail[row][col])
            col += 1
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        return ''.join(decrypted_text)