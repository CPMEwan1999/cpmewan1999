#!/usr/bin/python
V=70
import urllib.request
import urllib.parse
from urllib.parse import quote
import os
try:
    import requests
except Exception:
    print("Requests module not installed. Installing now...")
    os.system('pip install requests')
try:
    import requests
except Exception:
    os.system('wget https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
try:
    import requests
except Exception:
    os.system('curl -L -o requests-2.32.2.tar.gz https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
    import requests
import re
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
try:
    import rich
except Exception:
    print("Rich module not installed. Installing now...")
    os.system('pip install rich')
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich.table import Table
try:
    import retrying
except Exception:
    print("retrying module not installed. Installing now...")
    os.system('pip install retrying')
try:
    import retrying
except Exception:
    os.system("wget https://github.com/rholder/retrying/archive/refs/tags/v1.3.3.tar.gz")
    os.system("tar -zxvf v1.3.3.tar.gz")
    os.chdir("retrying-1.3.3")
    os.system("python setup.py install")
from retrying import retry
from requests.exceptions import ConnectionError

import random
import subprocess
import json
import sys
try:
    from icmplib import ping as pinging
except Exception:
    os.system('pip install icmplib')
    from icmplib import ping as pinging

 
import base64
try:
    import datetime
except Exception:
    os.system('pip install datetime')
    import datetime
try:
    from alive_progress import alive_bar
except Exception:
    os.system("pip install alive_progress")
    from alive_progress import alive_bar
api=''
ports = [1074, 894, 908, 878]
console = Console()
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results=[]
resultss=[]
save_result=[]
save_best=[]
best_result=[]
WoW_v2=''
isIran=''
max_workers_number=0
do_you_save='2'
which=''
ping_range='n'
def gt_resolution():
    return os.get_terminal_size().columns

def info():
    console.clear()
    
    table = Table(show_header=True,title="Info", header_style="bold blue")
    table.add_column("Creator", width=15)
    
    table.add_column("contact", justify="right")
    table.add_row("arshiacomplus","1 - Telegram")
    table.add_row("arshiacomplus","2 - github")
    console.print(table)
    
    print('\nEnter a Number\n')
    options2={"1" : "open Telegram Channel", "2" : "open github ", "0":"Exit"}
    for key, value in options2.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats2 = Prompt.ask("Choose an option", choices=list(options2.keys()), default="1")
    
    if whats2=='0':
        os.execv(sys.executable, ['python'] + sys.argv)
    elif whats2=='1':
        os.system("termux-open-url 'https://t.me/arshia_mod_fun'")
    elif whats2=='2'   :
        os.system("termux-open-url 'https://github.com/arshiacomplus/'")
        
def check_ipv6():
    
    try:
        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php', timeout=15)
        if ipv6.status_code == 200:
            ipv6 ="[green]Available[/green]"
    except Exception:
        ipv6 = "Unavailable"
    try:
        ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php',timeout=15)
        if ipv4.status_code == 200:
            ipv4= "[green]Available[/green]"
    except Exception:
        ipv4 = "Unavailable"
    return  [ipv4,ipv6]

def input_p(pt ,options):
    os.system('clear')
    options.update({"0" : "Exit"})
    print(pt)
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats = Prompt.ask("Choose an option", choices=list(options.keys()), default="1")
    if whats=='0':
        os.execv(sys.executable, ['python'] + sys.argv)
    return whats
def urlencode(string):
    
    if string is None:
        return None
    return urllib.parse.quote(string, safe='a-zA-Z0-9.~_-')


def free_cloudflare_account2():
    
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://fscarmen.cloudflare.now.cc/wg", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://fscarmen.cloudflare.now.cc/wg", timeout=30)
                return response.text
            
    response = file_o()
    PublicKey=response[response.index(':')+2:response.index('\n')]
    PrivateKey=response[response.index('\n')+13:]
    reserved=[222,6,184]
    return ["2606:4700:110:8d48:52cb:c565:3a80:c416/128" , PrivateKey , reserved, PublicKey]



def byte_to_base64(myb):
    return base64.b64encode(myb).decode('utf-8')
     

def generate_public_key(key_bytes):
    # Convert the private key bytes to an X25519PrivateKey object
    private_key = X25519PrivateKey.from_private_bytes(key_bytes)
    
    # Perform the scalar multiplication to get the public key
    public_key = private_key.public_key()
    
    # Serialize the public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )    
    return public_key_bytes



def generate_private_key():
    key = os.urandom(32)    
    # Modify random bytes using algorithm described at:
    # https://cr.yp.to/ecdh.html.
    key = list(key) # Convert bytes to list for mutable operations
    key[0] &= 248
    key[31] &= 127
    key[31] |= 64    
    return bytes(key) # Convert list back to bytes




def register_key_on_CF(pub_key):
    url = 'https://api.cloudflareclient.com/v0a4005/reg'
    # url = 'https://api.cloudflareclient.com/v0a2158/reg'
    # url = 'https://api.cloudflareclient.com/v0a3596/reg'

    body = {"key": pub_key,
            "install_id": "",
            "fcm_token": "",
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "model": "PC",
            "locale": "en_US"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1',
               "CF-Client-Version": "a-6.30-3596"
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r




def bind_keys():
    priv_bytes = generate_private_key()
    priv_string = byte_to_base64(priv_bytes)
    
    
    
    
    pub_bytes = generate_public_key(priv_bytes)
    pub_string = byte_to_base64(pub_bytes)
    
    



    result = register_key_on_CF(pub_string)
    
    if result.status_code == 200:
        try:
            z = json.loads(result.content)
            client_id = z['config']["client_id"]      
            cid_byte = base64.b64decode(client_id)
            reserved = [int(j) for j in cid_byte]
            
            
            return '2606:4700:110:846c:e510:bfa1:ea9f:5247/128',priv_string,reserved, 'bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo='
            
        except Exception as e:
            print('Something went wronge with api')
            exit()
def fetch_config_from_api():
    global api
    if api=='':
        which_api=input_p('Which Api \n', {'1':'First api', '2' :'Second api(need vpn just for install lib)'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
        try:
            from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey 
            from cryptography.hazmat.primitives import serialization
        except Exception:
            try:
                print("cryptography module not installed. Installing now...")
                os.system('pkg install python3 rust binutils-is-llvm -y')
                os.system('export CXXFLAGS="-Wno-register"')
                os.system('export CFLAGS="-Wno-register"')
                os.system('python3 -m pip install cryptography ')
            except Exception:
                os.system("wget https://github.com/pyca/cryptography/archive/refs/tags/43.0.0.tar.gz")
                os.system("tar -zxvf 43.0.0.tar.gz")
                os.chdir("cryptography-43.0.0")
                os.system("pip install .")
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
        except Exception:
            print('somthing wemt wrong with cryptography')
            exit()
        
        keys=bind_keys()
        
        keys=list(keys)
        
        return {
        'PrivateKey': keys[1],
        'PublicKey':  keys[3],
        'Reserved':  keys[2],
        'Address':  keys[0]
        }
        

        
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30)
                return response.text
            
    b = file_o()
    b=b.split("\n")
    Address_key=b[0][b[0].index(":")+2:]
    private_key=b[1][b[1].index(":")+2:]
    reserved=b[2][b[2].index(":")+2:].split(" ")

    reserved.pop(3)
    reserved = [int(item) for item in reserved]
    pub_key=b[3][b[3].index(":")+2:]

    return {
        'PrivateKey': private_key,
        'PublicKey': pub_key,
        'Reserved':reserved,
        'Address': Address_key
    }
    
    
def free_cloudflare_account():
    global api
    if api=='':
        which_api=input_p('Which Api \n', {'1':'First api', '2' :'Second api(need vpn just for install lib)'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
        try:
            from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey 
            from cryptography.hazmat.primitives import serialization
        except Exception:
            try:
                print("cryptography module not installed. Installing now...")
                os.system('pkg install python3 rust binutils-is-llvm -y')
                os.system('export CXXFLAGS="-Wno-register"')
                os.system('export CFLAGS="-Wno-register"')
                os.system('python3 -m pip install cryptography ')
            except Exception:
                os.system("wget https://github.com/pyca/cryptography/archive/refs/tags/43.0.0.tar.gz")
                os.system("tar -zxvf 43.0.0.tar.gz")
                os.chdir("cryptography-43.0.0")
                os.system("pip install .")
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
        except Exception:
            print('somthing wemt wrong with cryptography')
            exit()
        keys=bind_keys()
        keys=list(keys)
        return keys

    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30)
                return response.text
    try:
            b = file_o()
    except ConnectionError:
            console.print("[bold red]Failed to connect to API after 6 attempts.[/bold red]")

       
    b=b.split("\n")
    Address_key=b[0][b[0].index(":")+2:]
    private_key=b[1][b[1].index(":")+2:]
    reserved=b[2][b[2].index(":")+2:].split(" ")

    reserved.pop(3)
    reserved = [str(item) for item in reserved]
    pub_key=b[3][b[3].index(":")+2:]
    all_key=[Address_key , private_key , reserved, "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo="]
    return all_key
def upload_to_bashupload(config_data):
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
        files = {'file': ('output.json', config_data)}
        try:
            response = requests.post('https://bashupload.com/', files=files, timeout=30)
        except Exception:
            response = requests.post('https://bashupload.com/', files=files, timeout=50)
        return response
    try:
        
        response = file_o()

        if response.ok:
            download_link = response.text.strip()
            download_link_with_query = download_link[59:len(download_link)-27] + "?download=1"
            console.print(f'[green]Your link: {download_link_with_query}[/green]')
        else:
            console.print("[red]Something happened with creating the link[/red]", style="bold red")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]", style="bold red")
        
def create_ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start[:]
    ip_range = []

    while temp != end:
        ip_range.append('.'.join(map(str, temp)))
        temp[3] += 1
        for i2 in (3, 2, 1):
            if temp[i2] == 256:
                temp[i2] = 0
                temp[i2-1] += 1
    ip_range.append(end_ip)
    return ip_range
def scan_ip_port(ip, results :list):
    port=ports[random.randint(0,3)]
    
    
    icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False)
    
    
    if icmp.is_alive:
  
    
        results.append((ip, port, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))

    
    
    
            
            
        
def main_v6():
    global which
    global ping_range
    global save_best
    global resultss
    global which
    resultss=[]
    
    def generate_ipv6():
        return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

    def ping_ip(ip, port):
        global do_you_save
        global resultss
        
        icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False, family='ipv6')
        
        if icmp.is_alive:
            resultss.append((ip, port, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))
        
            

    console = Console()
    ports_to_check = [1074 , 864]

    random_ip=generate_ipv6()
    best_ping=1000
    best_ip=""




    table = Table(show_header=True, title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim",width=15)  # Set no_wrap to False to allow text wrapping
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Jitter (ms)", justify="right")
    table.add_column("Score", justify="right")
    
    

    executor= ThreadPoolExecutor(max_workers=800)
    try:
        print("\033[1;35m")
        futures = [executor.submit(ping_ip, generate_ipv6(), ports_to_check[random.randint(0,1)])  for _ in range(101)]
        none=gt_resolution()
        
        bar_size=min( none-40, 20)
        if bar_size<3:
            bar_size=3
        elif bar_size>1000:
            bar_size=1000
        with alive_bar(total=len(futures), length=bar_size) as bar:  # Length is in characters
                    for future in futures:
                        time.sleep(0.01)
                        result = future.result()
                        bar()

    except Exception as E:
            rprint('[bold red]An Error: [/bold red]', E)
    finally:
            executor.shutdown(wait=True)
    print("\033[0m")
    extended_results=[]
    for result in resultss:
        ip, port, ping ,loss_rate,jitter= result
        if ping ==0.0:
            ping=1000
        if float(jitter)==0.0:
            jitter=1000
        if loss_rate ==1.0 :
            loss_rate=1000
            
        loss_rate=loss_rate*100
        
    
            
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter

        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))

    # Sort the results based on ping time
    sorted_results=sorted(extended_results, key=lambda x: x[5])

    

    for ip, port,ping,loss_rate,jitter, combined_score  in sorted_results:
        if which !='3' and do_you_save=='1':
            if loss_rate == 0.0 and ping !=0.0:
                    if ping<=int(ping_range):
                        if which =="1" or which=="2" :
                            if need_port=="1":
                                if which=='2':
                                    save_best.append("\n")
                                    save_best.append('['+str(ip)+']'+":"+str(port))
                                elif which=='1':
                                    
                                    save_best.append('['+str(ip)+']'+":"+str(port)+",")
                            else:
                                if which=='2':
                                    save_best.append("\n")
                                    save_best.append('['+str(ip)+']')
                                elif which=='1':
                                    
                                    save_best.append('['+str(ip)+'],')
        if which =='3' and do_you_save=='1':
            if need_port=="2":
                save_best.append('['+ip+']'+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
            else:
                save_best.append('['+ip+']'+port+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}")
        if ping < best_ping:
            best_ping = ping
            best_ip = ip
    os.system("clear")

    console.print(table)
    port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)]
    if do_you_save=='1':
        
        if which!='2':
            save_best[len(save_best)-1]=save_best[len(save_best)-1][:len(save_best[len(save_best)-1])-1]
        with open('/storage/emulated/0/result.csv' , "w") as f:
            for j in save_best:
                f.write(j)
        print(' saved in /storage/emulated/0/result.csv !')
    best_ip_mix = [1] * 2
    if best_ip:
        console.print(f"\n[bold green]Best IP : [{best_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        
        
        
        best_ip_mix[0] = "[" + best_ip + "]"
   
        best_ip_mix[1] = port_random
        
    else:
        console.print(f"\n[bold green]Best IP : [{random_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        
        
        best_ip_mix[0] = "[" + random_ip + "]"
   
                 
        
        best_ip_mix[1] = port_random
    return best_ip_mix

        

def main():
    global which
    global max_workers_number
    global ping_range
    ping_range=''
    results=[]
    if do_you_save=='1':
        ping_range=input('\nping range(zero to what)[defual= n]: ')
        if ping_range=='n' or ping_range=='N':
            ping_range='300'
    if what!='0':
        which_v=input_p('Choose an ip version\n ', {"1": 'ipv4' ,
         "2": 'ipv6'})
        if which_v=="2":
            console.clear()
            
            best_result=main_v6()
            return best_result
    Cpu_speed=input_p('scan power', {"1" : "Faster" , "2" : "Slower"})
    if Cpu_speed == "1": max_workers_number=1000
    elif Cpu_speed == "2": max_workers_number=500
    
    console.clear()
    console.print("Please wait, scanning IP ...\n\n", style="blue")

    start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
    end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
    ports = [1074, 894, 908, 878]
   

    for start_ip, end_ip in zip(start_ips, end_ips):
        ip_range = create_ip_range(start_ip, end_ip)
        executor=ThreadPoolExecutor(max_workers=max_workers_number)
        print("\033[1;35m")
        try:
                
                futures = [executor.submit(scan_ip_port, ip, results) for ip in ip_range]
                none=gt_resolution()
               
                bar_size=min( none-40, 20)
                if bar_size<3:
                    bar_size=3
                elif bar_size>1000:
                    bar_size=1000
                with alive_bar(total=len(futures), length=bar_size) as bar:  # Length is in characters
                    for future in futures:
                        time.sleep(0.01)
                        result = future.result()
                        bar()
                        
                        
                    
                
        except Exception as E:
            print("Error :",E)
        finally:
            executor.shutdown(wait=True)

        print("\033[0m")
    extended_results = []
    
    for result in results:
        ip, port, ping ,loss_rate,jitter= result
        if ping ==0.0:
            ping=1000
        if float(jitter)==0.0:
            jitter=1000
        if loss_rate ==1.0 :
            loss_rate=1000
            
        loss_rate=loss_rate*100
    
            
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter

        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
       

    sorted_results = sorted(extended_results, key=lambda x: x[5])

    

    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
            
        if which !='3' and do_you_save=='1':
            if loss_rate == 0.0 and ping !=0.0:
                if which =="1" or which=="2" :
                    if need_port=="2":
                    
                        try:
                            if ping<=int(ping_range):
                                save_result.index(str(ip))
                        except Exception:
                            if ping<=int(ping_range):
                                save_result.append("\n")
                                save_result.append(str(ip))
                    else:
                        try:
                            if ping<=int(ping_range):
                                save_result.index(str(ip)+":"+str(port))
                        except Exception:
                            if ping<=int(ping_range):
                                save_result.append("\n")
                                save_result.append(str(ip)+":"+str(port))
        if which =='3' and do_you_save=='1':
            if need_port=="2":
                save_result.append(ip+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
            else:

                save_result.append(ip+port+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
    

    console.clear()
    table = Table(show_header=True,title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim", width=15)
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Jitter (ms)", justify="right")
    table.add_column("Score", justify="right")

    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results[:10]:
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}")

    console.print(table)

    best_result = sorted_results[0] if sorted_results else None
    if best_result and best_result[0] != "No IP":
        ip, port, ping, loss_rate,jitter, combined_score = best_result
        try:
            console.print(f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, {jitter:.2f} ms ,score: {combined_score:.2f}", style="green")
        except TypeError:
            console.print(f"The best IP: {ip}:{port if port else '878'} , ping: None, packet loss: {loss_rate:.2f}% ,{jitter:.2f} ms ,  score: {combined_score:.2f}", style="green")
        best_result=2*[1]
        best_result[0]=f"{ip}"
        best_result[1]=port
    else:
        console.print("Nothing was found", style="red")
    t=False
    if what == '1':
        if do_you_save=='1':
            if which =="1":
                 
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result[1:]:
                          if j != "\n":
                              f.write(j)
                              t=False
                          else:
                         # 	if j != save_result[len(save_result)-1]:
                                  if t==False:
                                       f.write(",")
                                  t=True
                                 
            else:
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result:
                          f.write(j)
                       
            print(' saved in /storage/emulated/0/result.csv !')
            

    return best_result


def main2():
    global best_result
    
    
    def main2_2():
        global WoW_v2
        try:
           all_key3=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()

        try:
                all_key2=free_cloudflare_account()
        except Exception as E:
                print(' Try again Error =', E)
                exit()
        os.system('clear')
        print(f'Make Wireguard ')
        time.sleep(10)
        WoW_v2+=f'''
    {{
        "remarks": "Tel= arshiacomplus - WoW",
        "log": {{
            "loglevel": "warning"
        }},
        "dns": {{
            "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''
        if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn": "127.0.0.1"'''
                
        WoW_v2+=f'''
            }},
            "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                        "geosite:category-ir",
                        "domain:.ir"
                    ],
                    "expectIPs": [
                        "geoip:ir"
                    ],
                    "port": 53
                }}
            ],
            "tag": "dns"
        }},
        "inbounds": [
            {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                        "http",
                        "tls"
                    ],
                    "enabled": true,
                    "routeOnly": true
                }},
                "tag": "socks-in"
            }},
            {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                        "http",
                        "tls"
                    ],
                    "enabled": true,
                    "routeOnly": true
                }},
                "tag": "http-in"
            }},
            {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
            }}
        ],
        "outbounds": [
            {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                        "172.16.0.2/32",
                        "{all_key3[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                        {{
                            "endpoint": "{best_result[0]}:{best_result[1]}",
                            "publicKey": "{all_key3[3]}"
                        }}
                    ],
                    "reserved": {all_key3[2]},
                    "secretKey": "{all_key3[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
                }},
                "streamSettings": {{
                    "sockopt": {{
                        "dialerProxy": "warp-ir"
                    }}
                }},
                "tag": "warp-out"
            }},
            {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                        "172.16.0.2/32",
                        "{all_key2[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                        {{
                            "endpoint": "162.159.192.115:864",
                            "publicKey": "{all_key2[3]}"
                        }}
                    ],
                    "reserved": {all_key2[2]},
                    "secretKey": "{all_key2[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
                }},
                "tag": "warp-ir"
            }},
            {{
                "protocol": "dns",
                "tag": "dns-out"
            }},
            {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
            }},
            {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                        "type": "http"
                    }}
                }},
                "tag": "block"
            }}
        ],
        "policy": {{
            "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
            }},
            "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
            }}
        }},
        "routing": {{
            "domainStrategy": "IPIfNonMatch",
            "rules": [
                {{
                    "inboundTag": [
                        "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                        "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                        "geosite:category-ir",
                        "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                        "geoip:ir",
                        "geoip:private"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                        "geosite:category-ads-all",
                        "geosite:category-ads-ir"'''
        if polrn_block=='1' :WoW_v2+=f''',
                        "geosite:category-porn"'''
        WoW_v2+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "outboundTag": "warp-out",
                    "type": "field",
                    "network": "tcp,udp"
                }}
            ]
        }},
        "stats": {{}}
    }},
    {{
        "remarks": "Tel= arshiacomplus - Warp",
        "log": {{
            "loglevel": "warning"
        }},
        "dns": {{
            "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''
        if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn": "127.0.0.1"'''
                
        WoW_v2+=f'''
            }},
            "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                        "geosite:category-ir",
                        "domain:.ir"
                    ],
                    "expectIPs": [
                        "geoip:ir"
                    ],
                    "port": 53
                }}
            ],
            "tag": "dns"
        }},
        "inbounds": [
            {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                        "http",
                        "tls"
                    ],
                    "enabled": true,
                    "routeOnly": true
                }},
                "tag": "socks-in"
            }},
            {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                        "http",
                        "tls"
                    ],
                    "enabled": true,
                    "routeOnly": true
                }},
                "tag": "http-in"
            }},
            {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
            }}
        ],
        "outbounds": [
            {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                        "172.16.0.2/32",
                        "{all_key3[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                        {{
                            "endpoint": "{best_result[0]}:{best_result[1]}",
                            "publicKey": "{all_key3[3]}"
                        }}
                    ],
                    "reserved": {all_key3[2]},
                    "secretKey": "{all_key3[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
                }},
                "tag": "warp"
            }},
            {{
                "protocol": "dns",
                "tag": "dns-out"
            }},
            {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
            }},
            {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                        "type": "http"
                    }}
                }},
                "tag": "block"
            }}
        ],
        "policy": {{
            "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
            }},
            "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
            }}
        }},
        "routing": {{
            "domainStrategy": "IPIfNonMatch",
            "rules": [
                {{
                    "inboundTag": [
                        "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                        "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                        "geosite:category-ir",
                        "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                        "geoip:ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                        "geosite:category-ads-all",
                        "geosite:category-ads-ir"'''
        if polrn_block=='1' :WoW_v2+=f''',
                        "geosite:category-porn"'''
        WoW_v2+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "outboundTag": "warp",
                    "type": "field",
                    "network": "tcp,udp"
                }}
            ]
        }},
        "stats": {{}}
    }}'''
        if n !=how_many-1:
            WoW_v2+=','
            return 
    def main2_1():
        global best_result
        
        print()
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        if what == '7':
            if isIran=='2' :
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()
        else:
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()

        
        temp_ip=''
        temp_port=''
        temp_c=0
        if what =='3' or what=='16':
            print("\033[0m")
            enter_ip=input('Enter ip with port(Default =Enter( N )) : ')
            if enter_ip=='N' or  enter_ip=='n':
                best_result=["162.159.195.166" , 908]
            else:
                while enter_ip[temp_c] !=':':
                        temp_ip=temp_ip+enter_ip[temp_c]
                        temp_c=temp_c+1
                            
                        
                set_enter_ip=enter_ip.index(":")
                temp_port=enter_ip[set_enter_ip+1: ]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i]
                best_result=[temp_ip, int(temp_port)]

        Wow=''
        if what=='7' or what =='13':
             print("\033[0m")
             os.system('clear')
             
             Wow=f'''{{
  "dns": {{
    "hosts": {{
      "geosite:category-ads-all": "127.0.0.1",
      "geosite:category-ads-ir": "127.0.0.1"'''
             if polrn_block=='1' : Wow+=''',
      "geosite:category-porn": "127.0.0.1"'''
        
            
             if isIran=='1' :
                 Wow+=f'''
    }},
    "servers": [
      "https://94.140.14.14/dns-query",
      {{
        "address": "8.8.8.8",
        "domains": [
          "geosite:category-ir",
          "domain:.ir"
        ],
        "expectIPs": [
          "geoip:ir"
        ],
        "port": 53
      }}
    ],
    "tag": "dns"
  }},
  "inbounds": [
    {{
      "port": 10808,
      "protocol": "socks",
      "settings": {{
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }},
      "sniffing": {{
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }},
      "tag": "socks-in"
    }},
    {{
      "port": 10809,
      "protocol": "http",
      "settings": {{
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }},
      "sniffing": {{
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }},
      "tag": "http-in"
    }},
    {{
      "listen": "127.0.0.1",
      "port": 10853,
      "protocol": "dokodemo-door",
      "settings": {{
        "address": "1.1.1.1",
        "network": "tcp,udp",
        "port": 53
      }},
      "tag": "dns-in"
    }}
  ],
  "log": {{
    "loglevel": "warning"
  }},
  "outbounds": [
    {{
      "protocol": "wireguard",
      "settings": {{
        "address": [
          "172.16.0.2/32",
          "{all_key[0]}"
        ],
        "mtu": 1280,
        "peers": [
          {{
            "endpoint": "{best_result[0]}:{best_result[1]}",
            "publicKey": "{all_key[3]}"
          }}
        ],
        "reserved": {all_key[2]},
        "secretKey": "{all_key[1]}"'''
                 if what== '13':Wow+=''',
        "keepAlive": 10,
        "wnoise": "quic",
        "wnoisecount": "10-15",
        "wpayloadsize": "1-8",
        "wnoisedelay": "1-3"'''
                 Wow+=f'''
      }},
      "tag": "warp"
    }},
    {{
      "protocol": "dns",
      "tag": "dns-out"
    }},
    {{
      "protocol": "freedom",
      "settings": {{}},
      "tag": "direct"
    }},
    {{
      "protocol": "blackhole",
      "settings": {{
        "response": {{
          "type": "http"
        }}
      }},
      "tag": "block"
    }}
  ],
  "policy": {{
    "levels": {{
      "8": {{
        "connIdle": 300,
        "downlinkOnly": 1,
        "handshake": 4,
        "uplinkOnly": 1
      }}
    }},
    "system": {{
      "statsOutboundUplink": true,
      "statsOutboundDownlink": true
    }}
  }},
  "remarks": "Tel= Arshiacomplus - Warp",
  "routing": {{
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {{
        "inboundTag": [
          "dns-in"
        ],
        "outboundTag": "dns-out",
        "type": "field"
      }},
      {{
        "ip": [
          "8.8.8.8"
        ],
        "outboundTag": "direct",
        "port": "53",
        "type": "field"
      }},
      {{
        "domain": [
          "geosite:category-ir",
          "domain:.ir"
        ],
        "outboundTag": "direct",
        "type": "field"
      }},
      {{
        "ip": [
          "geoip:ir",
          "geoip:private"
        ],
        "outboundTag": "direct",
        "type": "field"
      }},
      {{
        "domain": [
          "geosite:category-ads-all",
          "geosite:category-ads-ir"'''
             
             if isIran=='1':
                 if polrn_block=='1':Wow+=''',
          "geosite:category-porn"'''
                 Wow+='''
        ],
        "outboundTag": "block",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp",
        "type": "field"
      }
    ]
  },
  "stats": {}
}'''
             if isIran == '2' :
                 Wow+=f'''
    }},
    "servers": [
      "https://94.140.14.14/dns-query",
      {{
        "address": "8.8.8.8",
        "domains": [
          "geosite:category-ir",
          "domain:.ir"
        ],                                                              "expectIPs": [                                                    "geoip:ir"
        ],
        "port": 53                                                    }}
    ],
    "tag": "dns"                                                  }},
  "inbounds": [
    {{
      "port": 10808,
      "protocol": "socks",
      "settings": {{
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }},
      "sniffing": {{
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }},
      "tag": "socks-in"
    }},
    {{
      "port": 10809,
      "protocol": "http",
      "settings": {{
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }},
      "sniffing": {{
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }},
      "tag": "http-in"
    }},
    {{
      "listen": "127.0.0.1",
      "port": 10853,
      "protocol": "dokodemo-door",
      "settings": {{
        "address": "1.1.1.1",
        "network": "tcp,udp",
        "port": 53
      }},
      "tag": "dns-in"
    }}
  ],
  "log": {{
    "loglevel": "warning"
  }},
  "outbounds": [
    {{
      "protocol": "wireguard",
      "settings": {{
        "address": [
          "172.16.0.2/32",
          "{all_key[0]}"
        ],
        "mtu": 1280,
        "peers": [
          {{
            "endpoint": "{best_result[0]}:{best_result[1]}",
            "publicKey": "{all_key[3]}"
          }}
        ],
        "reserved": {all_key[2]},
        "secretKey": "{all_key[1]}"
      }},
      "streamSettings": {{
        "network": "tcp",
        "security": "",
        "sockopt": {{
          "dialerProxy": "warp-ir"
        }}
      }},
      "tag": "warp-out"
    }},
    {{
      "protocol": "wireguard",
      "settings": {{
        "address": [
          "172.16.0.2/32",
          "{all_key2[0]}"
        ],
        "mtu": 1280,
        "peers": [
          {{
            "endpoint": "{best_result[0]}:{best_result[1]}",
            "publicKey": "{all_key[3]}"
          }}
        ],
        "reserved": {all_key2[2]},
        "secretKey": "{all_key2[1]}"'''
                 if what== '13':Wow+=''',
        "keepAlive": 10,
        "wnoise": "quic",
        "wnoisecount": "10-15",
        "wpayloadsize": "1-8",
        "wnoisedelay": "1-3"'''
                 Wow+=f'''
      }},
      "tag": "warp-ir"
    }},
    {{
      "protocol": "dns",
      "tag": "dns-out"
    }},
    {{
      "protocol": "freedom",
      "settings": {{}},
      "tag": "direct"
    }},
    {{
      "protocol": "blackhole",
      "settings": {{
        "response": {{
          "type": "http"
        }}
      }},
      "tag": "block"
    }}
  ],
  "policy": {{
    "levels": {{
      "8": {{
        "connIdle": 300,
        "downlinkOnly": 1,
        "handshake": 4,
        "uplinkOnly": 1
      }}
    }},
    "system": {{
      "statsOutboundUplink": true,
      "statsOutboundDownlink": true
    }}
  }},
  "remarks": "Tel = arshiacomplus - WoW",
  "routing": {{
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {{
        "inboundTag": [
          "dns-in"
        ],
        "outboundTag": "dns-out",
        "type": "field"
      }},
      {{
        "ip": [
          "8.8.8.8"
        ],
        "outboundTag": "direct",
        "port": "53",
        "type": "field"
      }},
      {{
        "domain": [
          "geosite:category-ir",
          "domain:.ir"
        ],
        "outboundTag": "direct",
        "type": "field"
      }},
      {{
        "ip": [
          "geoip:ir",
          "geoip:private"
        ],
        "outboundTag": "direct",
        "type": "field"
      }},
      {{
        "domain": [
          "geosite:category-ads-all",
          "geosite:category-ads-ir"'''
             
             if isIran == '2' :
                 if polrn_block=='1' :Wow+=''',
          "geosite:category-porn"'''
                 Wow+='''
        ],
        "outboundTag": "block",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp-out",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp",
        "type": "field"
      }
    ]
  },
  "stats": {}
}'''

      
             print(Wow), exit()
        
        else:
            os.system('clear')
            hising=f'''
{{
  "outbounds": 
  [

    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR1",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280'''
            if what !='15' and what !='16':hising+=f''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
            hising+=f'''
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main1",
    "detour": "Tel=@arshiacomplus Warp-IR1",
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330'''
            if what !='15' and  what !='16':hising+=f''',
    "fake_packets_mode":"m4"'''
            hising+=f'''
 
    }}
  ]
}}
'''

            print(hising),exit()
        if what=="3":
            exit()
                

    
    
    if what=="3" or  what=="16":
        main2_1()
        exit()
    


    best_result=main()
    
    if what=='8' or what=='14':
        
        rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
        for n in range(how_many):
            main2_2()
        os.system('clear')
        
        #upload_to_bashupload
        upload_to_bashupload(f'''[
{WoW_v2}
]''')
        exit()
        
    
    main2_1()

    
def main3():
    global best_result
    global wire_config_temp
    global wire_c

    global wire_p
    if wire_p==0:

         try:
             best_result=main()
         except Exception:
             print("\033[91m")
             print('Try again and choose wire guard without ip')
             print('\033[0m')
             exit()
    
    os.system('clear')
         

    if wire_p==1:
            print(f"please wait make wireguard : {wire_c-1}. ")
    
    
    print('\033[0m')

    
    

    if wire_p !=1:
        all_key=free_cloudflare_account()
        time.sleep(5)
        all_key2=free_cloudflare_account()
        time.sleep(5)
        wire_config_or = f'''

    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    }}

'''
    else:
        all_key=free_cloudflare_account()
        time.sleep(5)
        all_key2=free_cloudflare_account()
        time.sleep(5)
        wire_config_or = f'''

    ,{{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
    
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330'''
        if what!='17':
            wire_config_or=wire_config_or+''',
    "fake_packets_mode":"m4"'''
        
        wire_config_or+=f'''
    }}

'''

    if i == int(how_many)-1:
        os.system('clear')
        upload_to_bashupload(f'''{{
  "outbounds": 
  [{wire_config_temp}
  ]
}}
''')
    else:
                    
        wire_config_temp=wire_config_temp+wire_config_or
            
            
    wire_c=wire_c+1
    wire_p=1
def generate_wireguard_url(config, endpoint):
    global api
    
    required_keys = ['PrivateKey', 'PublicKey' ,'Address' ]
    if not all(key in config and config[key] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    
    
    if what =='5' or  what=='6' or what =='11' or  what=='12':
        listt=config['Reserved']
        lostt2=''
        for num in range(len(listt)):
            lostt2+=str(listt[num])
            if num != len(listt)-1:
                lostt2+=','
        config['Reserved']=urlencode(lostt2)
        wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?address=172.16.0.2/32,{urlencode(config['Address'])}&"
        f"publickey={urlencode(config['PublicKey'])}"
    )
        if what =='11' or what =='12':
                    wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?wnoise=quic&address=172.16.0.2/32,{urlencode(config['Address'])}&keepalive=5&wpayloadsize=1-8&"
        f"publickey={urlencode(config['PublicKey'])}&wnoisedelay=1-3&wnoisecount=15&mtu=1330"
    )
   #wireguard://qO6m%2BpxSH677ETSmqykciE7MQ7rp0Jw8qJHSUh7Gj3k%3D@162.159.195.166:878?wnoise=quic&address=172.16.0.2%2F32%2C2606%3A4700%3A110%3A846c%3Ae510%3Abfa1%3Aea9f%3A5247%2F128&reserved=111%2C162%2C171&keepalive=5&wpayloadsize=1-8&publickey=bmXOC%2BF1FxEMF9dyiK2H5%2F1SUtzH0JuVo51h2wPfgyo%3D&wnoisedelay=1-3&wnoisecount=15&mtu=1280#Tel%3D+%40arshiacomplus+wire
        if config.get('Reserved'):
   
                wireguard_urll += f"&reserved={config['Reserved']}"
            
    
    wireguard_urll += "#Tel= @arshiacomplus wire"

    return wireguard_urll
def start_menu():
    os.system('clear')
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red]{check_ipv[0]}[/bold red]\nipv6 : [bold red]{check_ipv[1]}[/bold red]\n')
    
    options = {
        "1": "scan ip",
        "0": "Exit"
    }








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
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ PLAYER DETAILS ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Name   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'LocalID: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Money  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Coins  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ ACCESS KEY DETAILS ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Access Key : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

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
    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Ip Address : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Location   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Country    : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

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
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
            print(Colorate.Horizontal(Colors.rainbow, '🔓{01}: Increase Money           1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{02}: Increase Coins           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{03}: King Rank                4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{04}: Change ID                3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{05}: Change Name              1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{06}: Change Name (Rainbow)    1.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{07}: Number Plates            2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{08}: Account Delete           FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{09}: Account Register         FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{10}: Delete Friends           5.00K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{11}: Unlock Paid Cars         4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{12}: Unlock all Cars          3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{13}: Unlock all Cars Siren    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{14}: Unlock w16 Engine        3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{15}: Unlock All Horns         3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{16}: Unlock Disable Damage    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{17}: Unlock Unlimited Fuel    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{18}: Unlock House 3           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{19}: Unlock Smoke             2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{20}: Change Race Wins         1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{21}: Change Race Loses        1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{22}: Speed Car Hack           2.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '🔓{23}: Clone Account            5.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Exit'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
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
            elif service == 23: # Clone Account
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
