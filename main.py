#!/usr/bin/python

import urllib.request
import urllib.parse
from urllib.parse import quote
import os
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

def start_menu():
    os.system('clear')
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red]{check_ipv[0]}[/bold red]\nipv6 : [bold red]{check_ipv[1]}[/bold red]\n')
    
    options = {
        "1": "scan ip",
        "2": "wireguard for Hiddify",
        "3": "wireguard for Hiddify without ip scanning",
        "4": "wireguard for Hiddify with a sub link",
        "5": "wireguard for v2ray and mahsaNG without noise",
        "6": "wireguard for v2ray and mahsaNG without ip scanning without noise",
        "7": "WoW for v2ray or mahsaNG without noise",
        "8": "WoW for v2ray or mahsaNG in sub link without noise",
        "9": "Add/Delete shortcut",
        "10":"get wireguard.conf",
        "11":"wireguard for nikaNg and MahsaNg  with noise",
        "12":"wireguard for nikaNg and MahsaNg without ip scanning with noise",
        "13":"WoW with noise for Nikang or MahsaNg ",
        "14":"WoW with noise for Nikang or MahsaNg in sub link",
        "15": "wireguard for Sing-box and Hhidify | old | ",
        "16": "wireguard for Sing-box and Hiddify| old | without ip scanning",
        "17": "wireguard for Sing-box and Hiddify | old | with a sub link",
        "00" : "info",
        "0": "Exit"
    }

    rprint("[bold red]by Telegram= @arshiacomplus[/bold red]")
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    what = Prompt.ask("Choose an option", choices=list(options.keys()), default="0")
    return what
def get_number_of_configs():
    while True:
        try:
            how_many = int(Prompt.ask('\nHow many configs do you need (2 to 4): '))
            if how_many >= 2 and how_many <= 4:
                break
        except ValueError:
            console.print("[bold red]Please enter a valid number![/bold red]", style="red")
    return how_many
def gojo_goodbye_animation():
    frames  = [
        "\n\033[94m(＾-＾)ノ\033[0m",  # آبی
        "\n\033[93m(＾-＾)ノ~~~\033[0m",  # زرد
        "\n\033[92m(＾-＾)ノ~~~~~~\033[0m" , # سبزl
    ]
    
    for frame in frames:
      #  os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(1)
if __name__ == "__main__":
    os.system('clear')
    
    
    what=start_menu()


    if what =='1':
        
        do_you_save=input_p('Do you want to save in a result csv\n', {"1" : 'Yes' , "2" : "No"})
        which = 'n'
        if do_you_save=='1':
            os.system('termux-setup-storage')
            which = input_p('Do you want for bpb panel(with comma) or vahid panel(with enter) in a result csv\n ', {'1' : 'bpb panel(with comma)',
             '2' : 'vahid panel(with enter)', '3':'with score', '4':'clean'})
            if which !="4" :
                need_port = input_p('Do you want to save port in result\n ', {'1' : 'Yes',
             '2' : 'No'})
            if which =='4':
                which = input_p('Do you want for bpb panel(with comma) or vahid panel(with enter) in a result csv\n ', {'1' : 'bpb panel(with comma)',
             '2' : 'vahid panel(with enter)'})
                with open('/storage/emulated/0/result.csv', 'r') as f:
                    b=f.readlines()
                    with open('/storage/emulated/0/clean_result.csv', 'w') as ff:
                        for j in b:
                                 if which =='1':
                                     ff.write(j[:j.index('|')-1])
                                     if j != b[len(b)-1]:
                                          ff.write(',')
                                 else:
                                     ff.write(j[:j.index('|')-1])
                                     ff.write('\n')
                                    
                print(' saved in /storage/emulated/0/clean_result.csv !')
                exit()
                            
            
       
            
        main()
    elif what=='2' or what=="3" or what =='7' or what =='13'  or what=='15' or what=="16":
    
        if what == '7' or what=='13':
            
            polrn_block= input_p('Do you want to block p@rn sites\n' , {"1": "Yes", "2": "No"})
            
            isIran =input_p('Iran or Germany\n' , {"1" : "Ip Iran[faster speed]", "2" : "Germany[slower speed]"})
            
            
        main2()
    elif what=='4' or what=='17':
        how_many=get_number_of_configs()  

        for i in range(how_many):
            main3()
    elif what =='5' or what =='6' or what=='11' or what=='12':
        
            
        api_url = 'http://s9.serv00.com:1074/arshiacomplus/api/wirekey'
        if what=='5' or what =='11':
            endpoint_ip_best_result=main()
            endpoint_ip = str(endpoint_ip_best_result[0])+":"+str(endpoint_ip_best_result[1])
        else:
            endpoint_ip=input('Enter ip with port (defualt = n):')
            if endpoint_ip=='N' or  endpoint_ip=='n':
                endpoint_ip="162.159.195.166:878"
            else:
                temp_ip2=''
                temp_port2=''
                temp_c2=0
                while endpoint_ip[temp_c2] !=':':
                        temp_ip2=temp_ip2+endpoint_ip[temp_c2]
                        temp_c2=temp_c2+1
                            
                        
                set_enter_ip2=endpoint_ip.index(":")
                temp_port2=endpoint_ip[set_enter_ip2+1: ]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i]
                endpoint_ip=str(temp_ip2 +":" +str(temp_port2))
                
                
        rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
        try:
            config = fetch_config_from_api()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        wireguard_url = generate_wireguard_url(config, endpoint_ip)
        if wireguard_url:
            os.system('clear')
            print(f"""


{wireguard_url}




""")
        else:
            print("Failed to generate WireGuard URL.")
    elif what == '8' or  what=='14':
        how_many=get_number_of_configs()
        polrn_block= input_p('Do you want to block p@rn sites\n' , {"1": "Yes", "2": "No"})

        
        main2()
    
    elif what == '9':

        if os.path.exists('/data/data/com.termux/files/usr/etc/bash.bashrc.bak'):
            
            Delete=input_p('Do you want to Delete short cut',{"1" : "Yes", "2" : "No"})
            if Delete=='1':
                os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
                os.rename('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', '/data/data/com.termux/files/usr/etc/bash.bashrc')
                console.print("[bold red]Shortcut Deleted,  successful[/bold red]", style="red")
    
    
            exit()
        while True:
            name = input("\nEnter a shortcut name : ")
            if not name.isdigit():
                break
                
            
            else:
                console.print("\n[bold red]Please enter a name![/bold red]", style="red")
                
        with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as f2:
            txt= f2.read()
            with open('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', 'w') as f:
                f.write(txt)
        text=f'''
{name}() {{
bash <(curl -fsSL https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/install.sh)
}}\n'''
        with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r+') as f:
               content = f.read()
               f.seek(0, 0)
               f.write(text.rstrip('\r\n') + '\n' + content)
        rprint(f"\n[bold green]Please Restart your  termux and Enter [bold red]{name}[/bold red] to run script[/bold green]")

    elif what =='10':
        endpoint_ip_best_result=main()
        endpoint_ip = str(endpoint_ip_best_result[0])+":"+str(endpoint_ip_best_result[1])
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        name_conf=input('\nEnter a name: (defult [Enter]) : ')
        
        os.system('termux-setup-storage')
        
            
        
        if name_conf=='' :
            
            name_conf='acpwire.conf'
        path = '/storage/emulated/0/'+name_conf+".conf"
        with open(path, 'w') as f:
            f.write(f'''[Interface]
PrivateKey = {all_key[1]}
Address = 172.16.0.2/32, {all_key[0]}
DNS = 1.1.1.1, 1.0.0.1, 2606:4700:4700::1111, 2606:4700:4700::1001
MTU = 1280

[Peer]
PublicKey = {all_key[3]}
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = {endpoint_ip}''')
        rprint(f'\n[bold green]{name_conf} saved in {path}.conf[/bold green]')
    
    elif what == '00':
        info()
        
    elif what=='0':
        gojo_goodbye_animation()
        time.sleep(1)
        console.print("""
[bold magenta]Exiting... Goodbye![/bold magenta]""")
        
        
        exit()
