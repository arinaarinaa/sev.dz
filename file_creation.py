

def function_of_file_creation():
    with open('my_file.scv', 'a', encoding = 'utf-8') as f:
        f.write(f'Фамилия, имя, номер телефона и доп информация \n')
    
