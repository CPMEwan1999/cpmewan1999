import argparse
import simplecrypt
import nacl.secret
import nacl.utils
import nacl.pwhash
import base64
import random
import uuid

def generate_password():
    response = uuid.uuid4().hex[:random.randint(28,32)] + '/' + uuid.uuid4().hex[:random.randint(4,8)].upper() + '/' + uuid.uuid4().hex[:random.randint(16,32)]
    return response

def secret_key(password, salt):
    p_hash = base64.b64encode(password)
    s_hash = base64.b64encode(salt)
    secret_key = "{p}:{s}".format(p=p_hash, s=s_hash)
    return secret_key

parser = argparse.ArgumentParser(description='encryption tool')
parser.add_argument('-p', '--password', help='your password (required)', required=True)
parser.add_argument('-f', '--filename', help='your file to encrypt', required=True)
parser.add_argument('-s', '--secret', help='your file that contains your secret', required=True)
args = parser.parse_args()

key_password = args.password
content_file = args.filename
secret_file = args.secret
password = generate_password()
my_secret_string = 'this is my secure string'

kdf = nacl.pwhash.argon2i.kdf
salt_size = nacl.pwhash.argon2i.SALTBYTES
salt = nacl.utils.random(salt_size)
key = kdf(nacl.secret.SecretBox.KEY_SIZE, password, salt)

box = nacl.secret.SecretBox(key)
encrypted = box.encrypt(my_secret_string)

with open(content_file, 'w') as x:
    file_content = base64.b64encode(encrypted)
    x.write(file_content)

with open(secret_file, 'w') as y:
    sk = secret_key(password, salt)
    cipher = simplecrypt.encrypt(key_password, sk)
    encoded_cipher = base64.b64encode(cipher)
    y.write(encoded_cipher)
