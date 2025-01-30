from Caesar_Guesser import * 
class Cipher():

    def caesar_encoder(self, text: str, shift: int) -> str:
        result = ''
        self.result = result
        self.shift = shift

        for char in text:
            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base) if char.isalpha() else char

        return result
    
    def caesar_decoder(self) -> str:
        org_word = ''

        for letter in self.result:
            base = ord('A') if letter.isupper() else ord('a')

            org_word += chr((ord(letter) - base - self.shift) % 26 + base) if letter.isalpha() else letter
            
        return org_word