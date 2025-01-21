import urllib.request
import urllib.parse
from urllib.parse import quote
import os

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
        

def start_menu():
    os.system('clear')
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red]{check_ipv[0]}[/bold red]\nipv6 : [bold red]{check_ipv[1]}[/bold red]\n')
    
    options = {
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
    
    
        
      
