
import random
service_info = input('enter name of services(Gooogle, Spotify etc....)')
name_info = input('enter your emailaddr or username')
m = input('select a mode from(s:SAVE/g:GENERATE/dp:DISPLAY_PASSWORD/du:DISPLAY_USERNAME)')
def save_password(password):
        with open("passwordram.txt", mode="a") as t:
            t.write(f'\n{service_info},{name_info},{password}\n')
        return f'{password} and {name_info} were registered in {service_info}'
def generate_password(length):       
    numberofinput=int(input("enter the length of password"))
    uppercases = ["A","B","C","D","E","F","G","H","I","J","K","L","M",'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercases = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['2', '1', '3', '4', '5', '6', '7', '8', '9', '10']
    content = uppercases + lowercases + numbers
    password = ''.join(random.choices(content, k=numberofinput))
    save_password(password)
    return password
def display_password(k):                           
    with open('passwordram.txt', mode = 'r') as p:
         for line in p:
              if k in line:
                   return line[2]
def display_username(k):
     with open('passwordram.txt', mode = 'r') as p:
          for line in p:
               if k in line:
                    return line [1]
def delete_line(k):
     with open('passwordram.txt', mode = 'r') as p:
          for line in p:
               if k in line:
                    del line 
               return f'all of information you registered in {k} has deleted'               
if m == 's':
     password = input()
     result = save_password(password)
elif m == 'g':
     length = int(input())
     result = generate_password(length)
elif m == 'dp':
     k = input()
     result = display_password(k)
elif m == 'du':
     k = input()
     result = display_username(k)
elif m == 'del':
     k = input()
     result = delete_line(k)
else:
    result = print('Sorry, THAT doesnt exist in this program')
print(result)
