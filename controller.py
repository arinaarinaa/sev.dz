from user import user_interface
from file_creation import function_of_file_creation
from log import*

infa = user_interface()
time_now = log()
def writing():
    with open ('my_file.scv', 'a', encoding = 'utf-8') as data:
        data.write(f'{time_now} -> {infa[0]};{infa[1]}; {infa[2]};{infa[3]} \n')