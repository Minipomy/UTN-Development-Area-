import re
import time

def convert_uppercase(text:str) -> str:
    return(text.upper())

def convert_lowercase(text:str) -> str:
    return(text.lower())

def convert_concat(text_a:str, text_b:str) -> str:
    return(f'{text_a +" "+ text_b}')

def count_chars(text:str) -> int:
    return(len(text))

def count_chars_with_elem(text:str, elem:str) -> int:
    counter = 0
    for char in text:
        if (char == elem):
            counter+=1
    return(counter)

def get_strings_with_char(text:str, elem:str) -> list[str]:
    list = []
    temp_text = text.split()
    for char in temp_text:
        if elem in char:
            list.append(char)
    return(list)

def remove_spaces(text:str) -> str:
    temp_text = ""
    for char in text:
        if (char != " "):
            temp_text += char
    return(temp_text)

def get_name_lastname(name:str, lastname:str) -> list[str]:
    list_person = []
    list_person.append(name.capitalize())
    list_person.append(lastname.capitalize())
    return(list_person)

def concat_linedown(list_names:list[str]):
    lined_down = ""
    for char in list_names:
        lined_down += char + '\n'
    return(lined_down)

def generate_email(name:str, lastname:str) -> str:
    name = f'{name[0].lower()}'
    lastname = f'{lastname.strip().lower()}'
    doamin = '@utn-fra.com.ar'
    dot = '.'
    return(f'{name}{dot}{lastname}{doamin}')

def generate_commas(list:list[str]) -> str:
    text = f'{", ".join(list[:-1])} y {list[-1]}'
    return(text)

def credit_card():
    pattern = r'\d{16}'
    cc_number = 0
    censored = '****-****-****-'
    
    print('creditcard() - Started execution')
    while(True):
        try:
            cc_number = int(input('Please, enter your Credit Card number:\n'))
            while(len(str(cc_number)) < 16):
                cc_number = int(input('Please, enter your Credit Card number:\n'))
            break
        except ValueError as Error:
            print(f"WARNING:\n{Error}\n\
            Should be a 0~16 number:\n\
            BAD_INPUT\n")
        finally:
            print('creditcard() - Ended execution')
    match = re.search(pattern, str(cc_number)).group()
    hidden = re.sub(r'\d{12}', censored, match)
    return(hidden)

print(time.localtime())
print(credit_card())


def rem_domain(mail:str):
    pattern = r'[^@]+'
    match = re.search(pattern, mail)
    if match:
        return(match.group())

