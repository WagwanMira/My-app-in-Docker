
from flask import Flask
import random
import string
import os 
b = os.environ ['a']
b = int(b)
a = 0
a = int(a)
 
def generate_password(length, count):
    passwords = []
    for i in range(count):
        password = ''. join(random. choice(string. ascii_letters + string. digits + string. punctuation) for _ in range(length))
        passwords. append(password)
        return passwords

app = Flask(__name__)

@app.route('/')

def hello_name():
    print("Helo world",b)
    if b > 0:
        with open('config.txt', 'w') as file:
            file.write(str(b))
            file.close()
            password = generate_password(b, 1)
            return 'Your new password is: %s' %  password
    else:
        with open('config.txt', 'r') as file:
            a = file.read()
            a = int(a)                
            password = generate_password(a, 1)
            return 'Your new password is: %s' %  password
     
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=4567)
