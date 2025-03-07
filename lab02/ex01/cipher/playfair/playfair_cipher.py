class PlayfairCipher:
    def __init__(self) -> None:
        pass
    
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")  # Replace 'J' with 'I' as per Playfair cipher rules
        seen = set()
        matrix = []

        # Add unique letters from the key
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)

        # Add the rest of the alphabet (excluding 'J' because it's already replaced by 'I')
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted
        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        # Create the 5x5 matrix
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        
        return playfair_matrix

        
    def find_letter_coords(self, matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        raise ValueError(f"Letter {letter} not found in matrix.")

        
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:
                    pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
            elif col1 == col2:
                encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text
        
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        decrypted_text1 = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
                
            if row1 == row2:
                decrypted_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
            elif col1 == col2:
                decrypted_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                    
        banro = ""
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1]
            
            if decrypted_text[-1] == "X":
                banro += decrypted_text[-2]
            else:
                banro += decrypted_text[-2]
                banro += decrypted_text[-1]
            return banro