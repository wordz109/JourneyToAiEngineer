#Mengubah Pascal Case atau Camel Case menjadi Snake Case
#Menggunakan For loop dan List Comprehension
def snake_case_cara1(masuk):
    snake_case_char = []
    for char in masuk :
        if char.isupper():
            converted_char = '_' + char.lower()
            snake_case_char.append(converted_char)
        else :
            snake_case_char.append(char)
    return ''.join(snake_case_char).strip('_')

def snake_case_cara2(masuk):
    snake_case_char = ['_' + char.lower() if char.isupper() else char for char in masuk]
    return ''.join(snake_case_char).strip('_')

def main():
    print(snake_case_cara1('MatthewXaveriusSalomo'))
    print(snake_case_cara2('SalomoXaveriusMatthew'))
main()
