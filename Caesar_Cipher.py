
def caesar_cipher(message,offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % 26
            encrypted_text += alphabet[new_index]
    print('Kalimat Awal: ', message)
    print('Kalimat Setelah dienkripsi: ',encrypted_text)

text = input("Masukkan Teks :")
shift = int(input("Masukkan angka untuk berapa kali diubah :"))
caesar_cipher(text,shift)