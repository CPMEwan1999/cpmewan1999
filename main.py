def start_menu():
    
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
