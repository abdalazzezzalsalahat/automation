from faker import Faker
import shutil
import re

fake = Faker('en_US')

phone_regix = re.compile(r'((\(?\d{3}\)?)(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))? )', re.VERBOSE)

e_mail_regix = re.compile(r'([a-zA-Z0-9._%+-] + @[a-zA-Z0-9.-] + (\.[a-zA-Z]{2,4}))', re.VERBOSE)

with open('./assets/potential-contacts.txt', 'r') as file:
    text = file.read().replace('\n', '')

def get_e_mails(file):
    
    emails = []
    for i in e_mail_regix.findall(file):
        if i[0] not in emails:
            emails.append(i[0])
    return emails

def get_phone_number(file):
    
    nums = []
    for i in phone_regix.findall(file):
        num_lst = [i[1], i[3], i[5]]
        num_comp = '-'.join(num_lst)
        num_comp = re.sub(r'[(|)]', '', num_comp)
        if num_comp not in nums:
            nums.append(num_comp)
    return nums

def save(num, e_mails):

    with open('phone_numbers.txt', 'w+')as p:
        for x in num:
            p.write(x + '\n')

    with open('e_mails.txt', 'w+') as e: 
        for n in e_mails: 
            e.write(n + '\n')

if __name__ == '__main__':
    e_mails = get_e_mails(text)
    phone_nums = get_phone_number(text)
    save(phone_nums, e_mails)

    print(phone_nums)
    print('*'*40)
    print(e_mails)

