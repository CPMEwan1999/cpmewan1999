# Current version of the script 
debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')
server_local = "http://127.0.0.1:3000"
server_online = "https://api.topixsb.dev"
mode_server = server_online
"""
-------------------------------------------
MAJOR (Angka Pertama):

Angka ini meningkat ketika ada perubahan yang tidak kompatibel yang mengharuskan 
pengguna untuk memodifikasi kode atau penggunaan mereka yang ada. Misalnya, 
jika suatu fungsi dihapus atau perilakunya berubah secara signifikan, Anda akan 
meningkatkan versi mayor.
-------------------------------------------
MINOR (Angka Kedua):

Angka ini meningkat ketika fitur baru ditambahkan dengan cara yang kompatibel 
dengan versi sebelumnya. Ini berarti bahwa fungsionalitas yang ada tetap tidak 
berubah, tetapi kemampuan atau peningkatan baru diperkenalkan. Misalnya, 
jika fungsi baru ditambahkan tanpa memengaruhi yang sudah ada, Anda akan 
menaikkan versi minor.
-------------------------------------------
PATCH (Angka Ketiga):

Angka ini meningkat ketika perbaikan bug yang kompatibel dengan versi sebelumnya 
diperkenalkan. Ini biasanya merupakan perubahan kecil yang menyelesaikan masalah 
tanpa menambah fitur baru atau merusak fungsionalitas yang ada. Misalnya, 
jika ada bug yang diperbaiki dalam suatu fungsi tetapi antarmuka fungsi tersebut 
tetap sama, Anda akan menaikkan versi patch.
-------------------------------------------
"""



import os,sys,random,requests


VERSION_CHECK_URL = f"{mode_server}/termux-version"

def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Pastikan direktori ada
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        
def update_script():
    version_info = get_latest_version_info()
    if not version_info:
        return
    
    latest_version = version_info.get("version")
    download_url = version_info.get("download_url")
    print(download_url)
    print(f"CURRENT_VERSION {CURRENT_VERSION}\nlatest_version {latest_version}\ndownload_url {download_url}")
    if latest_version and download_url:
        if latest_version != CURRENT_VERSION:
            print(f"New version available: {latest_version}")
            print(f"Downloading update... {download_url}")
            download_new_version(download_url, sys.argv[0])
            print("Script updated to the latest version. Please restart the script.")
            exit()
        else:
            print("You already have the latest version.")
    else:
        print("Invalid version information received.")
update_script()


import platform
from datetime import datetime
local_ip = requests.get('https://api.ipify.org').text
response = requests.get(f"https://ipinfo.io/{local_ip}/json")
data_jaringan = response.json()

try:
    from colorama import init, Fore, Back, Style
    init()
    # Fungsi color pengganti menggunakan colorama
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    # Reinisialisasi setelah install
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem



def disp(clrnama):
    def get_closest_color(r, g, b):
        # Memetakan warna RGB ke warna colorama terdekat
        colors = {
            'RED': (255, 0, 0, Fore.RED),
            'GREEN': (0, 255, 0, Fore.GREEN),
            'BLUE': (0, 0, 255, Fore.BLUE),
            'YELLOW': (255, 255, 0, Fore.YELLOW),
            'MAGENTA': (255, 0, 255, Fore.MAGENTA),
            'CYAN': (0, 255, 255, Fore.CYAN),
            'WHITE': (255, 255, 255, Fore.WHITE)
        }
        
        min_distance = float('inf')
        closest_color = Fore.WHITE  # default
        
        for _, (cr, cg, cb, color) in colors.items():
            distance = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_color = color
                
        return closest_color

    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    
    for clrx in clrVnama:
        if clrfirsttime == False:
            try:
                # Mengkonversi hex ke RGB
                clrcode1 = int(clrx[0:2], 16)
                clrcode2 = int(clrx[2:4], 16)
                clrcode3 = int(clrx[4:6], 16)
                clrhuruf = clrx[7:8]
                
                # Mendapatkan warna colorama terdekat
                closest_color = get_closest_color(clrcode1, clrcode2, clrcode3)
                clrdisps += closest_color + clrhuruf + Style.RESET_ALL
            except:
                clrdisps += clrx[7:8]
                
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return clrdisps

warnasekarang=""
def generate(namax):
    global warnasekarang
    gabungwarna = ""
    contohnama = namax
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }
    while True:
        while True:
            tanya = random.choice(["merah","kuning","hijau","biru","ungu","pink"])
            if tanya!=warnasekarang:
                warnasekarang = tanya
                break
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "kuning":
            data["kodewarna"] = [230, 245, 66]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        elif tanya == "ungu":
            data["kodewarna"] = [150, 66, 245]
            break
        elif tanya == "pink":
            data["kodewarna"] = [245, 66, 215]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1]+tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0]-tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2]+tambah >= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1]-tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0]+tambah >= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2]-tambah >= 255:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]
        # print(f"{huruf} {data['kodewarna']}")
        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    # print(f"hasil\t:  {disp(data['kodewarnaCPM'])}")
    # print(f"kode\t:  {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]
def refresh_x():
    import inspect
    kucing_garong = inspect.getfile(inspect.currentframe())
    with open(kucing_garong, 'r') as file:
        gajah_terbang = file.read()
        gajah_duduk = len(gajah_terbang)
    return gajah_duduk
pySystem.Clear()
pySystem.Size(80, 40)


text = "▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ \n"
    brand_name += "▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ \n"
    brand_name += "▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒\n"
    brand_name += "▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
    brand_name += "▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░\n"
    brand_name += "░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "CYAN": Fore.CYAN,
            "YELLOW": Fore.YELLOW,
            "GOLD": Fore.YELLOW  # Colorama tidak memiliki gold, gunakan yellow sebagai alternatif
        }
        return w[colr.upper()] + tex + Style.RESET_ALL
    except:
        return tex
def mask_password(password):
    if len(password) <= 3:
        return password
    return password[:3] + '*' * (len(password) - 3)
def heder():
        if Your_Data['username']:
            get_userInfo()
        pySystem.Clear()
        print(f"build : {refresh_x()}")
        versi_tampil = disp(generate(f"Topix SB CPM TOOLS {CURRENT_VERSION}"))
        loc_info = f"  Location\t  : {data_jaringan.get('city')}, {data_jaringan.get('region')}, {data_jaringan.get('country')}"
        loc_info = pyColorate.Horizontal(pyColors.green_to_yellow, loc_info)
        isp_info = f"  ISP     \t  : {data_jaringan.get('org')}"
        isp_info = pyColorate.Horizontal(pyColors.green_to_yellow, isp_info)
        bannerwz = f"""{c("cyan","=====================================================")}
  {versi_tampil} {c("cyan","||")} {c("green","https://carparking.topixsb.dev/")}
{c("cyan","=====================================================")}
{loc_info}
{isp_info}"""
        if Your_Data['email_web']:
            data_client=f"""
  username   : {Your_Data['username']}
  role       : {Your_Data['role']}
  money      : {Your_Data['money']}
  expire_at  : {Your_Data['expire_at']}
  last login : {Your_Data['last_login_date']}"""
            if 'email' in Your_Data:
                data_client+=f"""\n\n  Car Parking Email : {Your_Data["email"]}
  Car Parking Passw : {mask_password(Your_Data["password"])}"""
            
            bannerwz+=pyColorate.Horizontal(pyColors.green_to_yellow, data_client)
        print(bannerwz)

tex="""     IMPORTANT READ

    You must log out of the CPM application first, 
    unless you only want to use the "Inject Rank" and "Instant Rank" features, 
    as these two features do not require you to log out.

    Please refill your cash only at https://carparking.topixsb.dev

"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))



def warnain(text,inpo="",title=""):
    tex = f"""{c("cyan","=====================================================")}"""
    if inpo:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.red_to_purple, inpo)}"
    if title:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.cyan_to_green, title)}"
    tex+=f"""
{pyColorate.Horizontal(pyColors.cyan_to_green, text)}
{c("cyan","=====================================================")}"""
    print(tex)


def send_registration_data(uname, upass):
    url = f"{mode_server}/register-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        # Pastikan untuk memanggil .json() untuk mendapatkan data JSON
        response_data = response.json()
        return response_data
    except Exception as e:
        return f"An error occurred: {e}"
def send_login_data(uname, upass):
    url = f"{mode_server}/login-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        if debug_mode:
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")
        
        if response.status_code != 200:
            try:
                error_data = response.json()
                return {
                    "status": False, 
                    "message": error_data.get('message', 'Unknown error occurred')
                }
            except:
                return {
                    "status": False, 
                    "message": f"Server error: {response.status_code}"
                }
            
        try:
            response_data = response.json()
            
            if response_data['status']:
                # Simpan semua data user termasuk token
                Your_Data.update({
                    'access_token': response_data['access_token'],
                    'username': response_data['data']['username'],
                    'role': response_data['data']['role'],
                    'money': response_data['data']['money'],
                    'email_web': response_data['data']['email'],
                    'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Tambahkan waktu login
                })
            return response_data
            
        except ValueError as e:
            return {
                "status": False, 
                "message": f"Invalid JSON response: {response.text}"
            }
            
    except requests.RequestException as e:
        return {
            "status": False, 
            "message": f"Request error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": False, 
            "message": f"Unexpected error: {str(e)}"
        }

def serper(cit, datanya):
    # Cek apakah token masih ada
    if not Your_Data.get('access_token'):
        return {"status": False, "message": "Silakan login terlebih dahulu"}

    url = f"{mode_server}/app_endpoint"

    data = {
        "access_token": Your_Data['access_token'],
        "username": Your_Data['username'],
        "item": {
            "name": cit
        },
        "email": Your_Data.get('email', ''),
        "password": Your_Data.get('password', '')
    }
    
    for x in datanya:
        data[x] = datanya[x]
        
    try:
        response = requests.post(url, json=data)
        
        # Handle berbagai status code
        if response.status_code == 401:
            # Token expired atau invalid
            Your_Data.clear()
            Your_Data.update({
                'email_web': None, 
                'expire_at': None, 
                'last_login_date': None, 
                'money': None, 
                'role': None, 
                'username': None,
                'access_token': None
            })
            return {"status": False, "message": "Sesi anda telah berakhir, silakan login kembali"}
        elif response.status_code == 429:
            # Rate limit
            return {"status": False, "message": "Terlalu banyak request, mohon tunggu beberapa saat"}
        elif response.status_code >= 500:
            # Server error
            return {"status": False, "message": "Server sedang bermasalah, coba lagi nanti"}
            
        try:
            result = response.json()
            return result
        except ValueError:
            return {"status": False, "message": f"Invalid JSON response: {response.text}"}
            
    except requests.RequestException as e:
        return {"status": False, "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": False, "message": f"Unexpected error: {str(e)}"}


def get_userInfo():
    url = f"{mode_server}/get_UserInfo"

    data = {
        "user": Your_Data['username'],
        "access_token": Your_Data['access_token']
    }

    try:
        response = requests.post(url, json=data, timeout=10.0)
        
        if response.status_code == 401:
            Your_Data.clear()
            Your_Data.update({
                'email_web': None, 
                'expire_at': None, 
                'last_login_date': None, 
                'money': None, 
                'role': None, 
                'username': None,
                'access_token': None
            })
            return {"status": False, "message": "Sesi anda telah berakhir, silakan login kembali"}
            
        try:
            reqreg = response.json()
            Your_Data['role'] = reqreg['role']
            Your_Data['last_login_date'] = reqreg['last_login_date']
            Your_Data['expire_at'] = reqreg['expire_at']
            Your_Data['money'] = reqreg['balance']
            return {"status": True}
        except ValueError:
            return {"status": False, "message": f"Invalid JSON response: {response.text}"}
            
    except requests.Timeout:
        return {"status": False, "message": "Request timeout. Silakan coba lagi."}
    except requests.RequestException as e:
        return {"status": False, "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": False, "message": f"Unexpected error: {str(e)}"}

datamobil=[ 
{"id": 140, "name": 'Cars 13'},
{"id": 184, "name": 'Cars 29'},
{"id": 131, "name": 'Cars 34'},
{"id": 187, "name": 'Cars 38'},
{"id": 9, "name": 'Cars 39'},
{"id": 21, "name": 'Cars 40'},
{"id": 39, "name": 'Cars 41'},
{"id": 54, "name": 'Cars 42'},
{"id": 60, "name": 'Cars 43'},
{"id": 62, "name": 'Cars 44'},
{"id": 121, "name": 'Cars 45'},
{"id": 126, "name": 'Cars 46'},
{"id": 147, "name": 'Cars 47'},
{"id": 148, "name": 'Cars 48'},
{"id": 151, "name": 'Cars 49'},
{"id": 154, "name": 'Cars 50'},
{"id": 161, "name": 'Cars 51'},
{"id": 168, "name": 'Cars 52'},
{"id": 177, "name": 'Cars 53'},
{"id": 180, "name": 'Cars 54'},
{"id": 185, "name": 'Cars 55'},
{"id": 196, "name": 'Cars 56'},
{"id": 200, "name": 'Cars 57'},
{"id": 206, "name": 'Cars 58'},
{"id": 209, "name": 'Cars 59'},
{"id": 0, "name": 'Cars 60'},
{"id": 1, "name": 'Cars 61'},
{"id": 6, "name": 'Cars 62'},
{"id": 8, "name": 'Cars 63'},
{"id": 12, "name": 'Cars 64'},
{"id": 30, "name": 'Cars 65'},
{"id": 43, "name": 'Cars 66'},
{"id": 81, "name": 'Cars 67'},
{"id": 85, "name": 'Cars 68'},
{"id": 112, "name": 'Cars 69'},
{"id": 113, "name": 'Cars 70'},
{"id": 150, "name": 'Cars 71'},
{"id": 160, "name": 'Cars 72'},
{"id": 175, "name": 'Cars 73'},
{"id": 181, "name": 'Cars 74'},
{"id": 182, "name": 'Cars 75'},
{"id": 183, "name": 'Cars 76'},
{"id": 210, "name": 'Cars 77'},
{"id": 5, "name": 'Cars 78'},
{"id": 11, "name": 'Cars 79'},
{"id": 17, "name": 'Cars 80'},
{"id": 19, "name": 'Cars 81'},
{"id": 20, "name": 'Cars 82'},
{"id": 28, "name": 'Cars 83'},
{"id": 35, "name": 'Cars 84'},
{"id": 47, "name": 'Cars 85'},
{"id": 49, "name": 'Cars 86'},
{"id": 51, "name": 'Cars 87'},
{"id": 82, "name": 'Cars 91'},
{"id": 88, "name": 'Cars 93'},
{"id": 128, "name": 'Cars 98'},
{"id": 156, "name": 'Cars 101'},
{"id": 189, "name": 'Cars 102'},
{"id": 14, "name": 'Cars 107'},
{"id": 103, "name": 'Cars 120'},
{"id": 109, "name": 'Cars 122'},
{"id": 144, "name": 'Cars 127'},
{"id": 153, "name": 'Cars 128'},
{"id": 211, "name": 'Cars 132'},
{"id": 104, "name": 'Cars 134'},
{"id": 115, "name": 'Cars 135'},
{"id": 143, "name": 'Cars 139'},
{"id": 188, "name": 'Cars 141'},
{"id": 7, "name": 'Cars 143'},
{"id": 32, "name": 'Cars 146'},
{"id": 41, "name": 'Cars 147'},
{"id": 58, "name": 'Cars 148'},
{"id": 162, "name": 'Cars 149'},
{"id": 178, "name": 'Cars 150'},
{"id": 198, "name": 'Cars 151'},
{"id": 202, "name": 'Cars 152'},
{"id": 203, "name": 'Cars 153'},]
data_AWD = [
                '6L45-A/T',
                '7S Tronic',
                '7 DSG',
                '8 Speed Tiptonic S',
                '9G Tronic',
                'Speedshift mct 9',
                'dsg7s',
                'dsg/s-tronic',
                'getrag 233',
                'getrag v161',
                'gr6',
                'sc924',
                'l6sss',
                'nsx9',
                'smt6',
                'w6maa gen 2',
                'zf 4hp22',
                'zf 6hp26s',
                'zf 8hp50',
                'zf 8hp70',
                'zf 8hp76',
                'zf 8hp'
            ]


Your_Data = {
    'email_web': None, 
    'expire_at': None, 
    'last_login_date': None, 
    'money': None, 
    'role': None, 
    'username': None,
    'access_token': None
}
req_menu = requests.get(f"{mode_server}/get_menu")
menu_cpm1 = req_menu.json()
req_menu = requests.get(f"{mode_server}/get_menu_cpm2")
menu_cpm2 = req_menu.json()


import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cpmewan1999 import CPMEwan1999

__CHANNEL_USERNAME__ = "Ewan1999Kurd"
__GROUP_USERNAME__   = "Ewan19_99Kurd"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ \n"
    brand_name += "▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ \n"
    brand_name += "▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒\n"
    brand_name += "▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
    brand_name += "▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░\n"
    brand_name += "░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '===========[ 𝙿𝙻𝙰𝚈𝙴𝚁 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 ]==========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Name   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'📍LocalID: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Money  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'📍Coins  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '=========[ 𝙰𝙲𝙲𝙴𝚂𝚂 𝙺𝙴𝚈 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 ]========='))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Access Key : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '==============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]=============='))
    print(Colorate.Horizontal(Colors.rainbow, f'📍Country : {data.get("country")}.'))    
    print(Colorate.Horizontal(Colors.rainbow, f'📍Region  : {data.get("regionName")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'📍City    : {data.get("city")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '================[ 𝐌𝐄𝐍𝐔 ]================'))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] ACCOUNT EMAIL[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] ACCOUNT PASSWORD[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] ACCESS KEY[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] TRYING TO LOGIN[/bold cyan]: ", end=None)
        cpm = CPMEwan1999(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN'))
                print(Colorate.Horizontal(Colors.rainbow, '! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
            print(Colorate.Horizontal(Colors.rainbow, '📍{01}: Increase Money           1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{02}: Increase Coins           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{03}: King Rank                4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{04}: Change ID                3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{05}: Change Name              1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{06}: Change Name (Rainbow)    1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{07}: Number Plates            2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{08}: Account Delete           FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{09}: Account Register         FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{10}: Delete Friends           5.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{11}: Unlock Paid Cars         4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{12}: Unlock all Cars          3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{13}: Unlock all Cars Siren    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{14}: Unlock w16 Engine        3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{15}: Unlock All Horns         3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{16}: Unlock Disable Damage    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{17}: Unlock Unlimited Fuel    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{18}: Unlock House 3           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{19}: Unlock Smoke             2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{20}: Change Race Wins         1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{21}: Change Race Loses        1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{22}: Speed Car Hack           2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{23}: All Cars 99HP            2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '📍{24}: Clone Account            5.000K'))            
            print(Colorate.Horizontal(Colors.rainbow, '📍{00} : Exit'))
            
            print(Colorate.Horizontal(Colors.rainbow, '================[ 𝐂𝐏𝐌☆ ]================'))
            
            service = IntPrompt.ask(f"[bold][?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '================[ 𝐂𝐏𝐌☆ ]================'))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH MONEY DO YOU WANT'))
                amount = IntPrompt.ask("[?] AMOUNT")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH COINS DO YOU WANT'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] NOTE:[/bold red]: IF THE KING RANK DOESN'T APPEAR IN GAME, CLOSE IT AND OPEN FEW TIMES", end=None)
                console.print("[bold red] [!] NOTE:[/bold red]: PLEASE DON'T DO KING RANK ON SAME ACCOUNT TWICE", end=None)
                sleep(2)
                console.print("[%] GIVING YOU A KING RANK: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW ID'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID ID'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW NAME'))
                new_name = Prompt.ask("[?] NAME")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW RAINBOW NAME'))
                new_name = Prompt.ask("[?] NAME")
                console.print("[%] SAVING YOUR DATA: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] GIVING YOU A NUMBER PLATES: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] AFTER DELETING YOUR ACCOUNT THERE IS NO GOING BACK'))
                answ = Prompt.ask("[?] DO YOU WANT TO DELETE THIS ACCOUNT", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] REGISTRING NEW ACCOUNT'))
                acc2_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
                acc2_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
                console.print("[%] CREATING NEW ACCOUNT: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: IN ORDER TO TWEAK THIS ACCOUNT WITH Ewan_Kurdish.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'YOU MOST SIGN-IN TO THE GAME USING THIS CCOUNT'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'THIS EMAIL IS ALREADY EXISTS'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] DELETING FRIENDS: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL", end=None)
                console.print("[%] UNLOCKING ALL PAID CARS: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] UNLOCKING ALL CARS: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] UNLOCKING ALL CARS SIREN: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] UNLOCKING W16 ENGINE: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] UNLOCKING ALL HORNS: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] UNLOCKING DISABLE DAMAGE: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] UNLOCKING UNLIMITED FUEL: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] UNLOCKING HOUSE 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] UNLOCKING SMOKE: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] CHANGING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] INSERT HOW MUCH RACES YOU LOSE'))
                amount = IntPrompt.ask("[?] AMOUNT")
                console.print("[%] CHANGING YOUR DATA: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            elif service == 22: # Hack Car Speed (299hp)
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[?] CAR ID")
                console.print("[%] HACKING CAR SPEED: ", end=None)
                if cpm.hack_car_speed(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    console.print("==================================")
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[!] THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 23: # Hack All Car Speed 99hp
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                console.print("[%] HACKING All CARS SPEED 99HP: ", end=None)
                if cpm.hack_car_sexo():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 24: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                to_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
                to_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
                console.print("[%] CLONING YOU ACCOUNT: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DO YOU WANT TO EXIT ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
            else: continue
            break
        break
