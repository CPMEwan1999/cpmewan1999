#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
import turtle
from pystyle import Colors, Colorate

from cpmewan1999 import CPMEwan1999

__CHANNEL_USERNAME__ = "Ewan1999Kurd"
__GROUP_USERNAME__   = "Ewan19_99Kurd"

# bmw-symbol-in-python
wn=turtle
turtle.bgcolor("#8b8682")
turtle.speed(0)
wn.setup(1530,780)
turtle.penup()
turtle.left(90)
turtle.forward(375)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#9ac0cd")
turtle.penup()
turtle.circle(375,-30)
turtle.left(90)
turtle.forward(16)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.circle(375-16,200)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.forward(16)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.circle(-375,200)
turtle.pendown()
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#607b8b")
turtle.penup()
turtle.circle(-375,160)
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.circle(375-16,160)
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.end_fill()
turtle.pendown()
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.circle(359,30)
turtle.circle(359)
turtle.right(-90)
turtle.forward(120)
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor("#0f0f0f")
turtle.circle(239,-240)
turtle.right(90)
turtle.forward(120)
turtle.right(-90)
turtle.circle(359,120*2)
turtle.right(-90)
turtle.forward(120)
turtle.right(-90)
turtle.end_fill()
turtle.left(90)
turtle.forward(120)
turtle.left(90)
for i in range(1):
    for  color0 in ('#1a1a1a','#2b2b2b','#3d3d3d','#4d4d4d','#595959','#737373','#7f7f7f','#a1a1a1','#ababab','#c2c2c2','#cfcfcf','#d9d9d9','#d9d9d9','#cfcfcf','#c2c2c2','#ababab','#a1a1a1','#7f7f7f','#737373','#595959','#4d4d4d','#3d3d3d','#2d2d2d','#1a1a1a',):
        turtle.begin_fill()
        turtle.fillcolor(color0)
        turtle.penup()
        turtle.circle(359,10-5)
        turtle.left(90)
        turtle.penup()
        turtle.forward(120)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.circle(-239,10-5)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(120)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(359,10-5)
        turtle.end_fill()
turtle.left(60+180)
turtle.pencolor("black")
turtle.penup()
turtle.goto(0,228.5)
turtle.pendown()
turtle.pensize(7+3)
turtle.circle(226+1.9)
turtle.left(90)
turtle.forward(228*2+1)
turtle.left(90)
turtle.circle(227.9,90.5)
turtle.left(89.5)
turtle.forward(228*2+1)
turtle.pencolor("black")
turtle.penup()
turtle.goto(0,228.5)
turtle.pendown()
turtle.pensize(5)
turtle.circle(226+1.9)
turtle.left(90)
turtle.forward(228*2+1)
turtle.left(90)
turtle.circle(227.9,90.5)
turtle.left(89.5)
turtle.forward(228*2+1)
turtle.pensize(1)
turtle.pencolor("#7d26cd")
turtle.penup()
turtle.goto(-5-0.5,5-0.2)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#3399cc")
turtle.forward(220)
turtle.right(90+0.5)
turtle.circle(-220,90-0.5)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.goto(5,5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#f7f7f7")
turtle.right(90)
turtle.forward(220)
turtle.right(90.5)
turtle.circle(-220,90-0.5)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
turtle.penup()
turtle.goto(-5,-5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#f7f7f7")
turtle.forward(220)
turtle.left(90+1)
turtle.circle(220,89)
turtle.right(-90)
turtle.forward(220)
turtle.end_fill()
turtle.penup()
turtle.goto(5,-5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#3399cc")
turtle.right(90)
turtle.forward(220-0.5)
turtle.right(91)
turtle.circle(-220,90-1)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
# MAKING BORDER'S
turtle.pencolor("black")
turtle.right(90)
turtle.penup()
turtle.goto(6,4)
turtle.pendown()
for i in range(1):
    for color2 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color2)
        turtle.penup()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.end_fill()
turtle.left(90)
turtle.penup()
turtle.goto(6.5,7)
turtle.pendown()
for i in range(1):
    for color3 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color3)
        turtle.penup()
        turtle.forward(19.8)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(19.8)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(19.8)
        turtle.pendown()
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.right(90)
turtle.penup()
turtle.circle(-220,90)
turtle.right(90)
turtle.forward(5-0.5)
turtle.right(90)
turtle.circle(215,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.pendown()
turtle.end_fill()
turtle.penup()
turtle.goto(4,-4)
turtle.pendown()
for i in range(1):
    for color4 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color4)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.penup()
turtle.goto(4,-4)
turtle.pendown()
turtle.right(90)
for i in range(1):
    for color5 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color5)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.left(90)
turtle.circle(220,89.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.circle(-215,90-1.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.goto(-5,-4)
turtle.pendown()
for i in range(1):
    for color9 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color9)

        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.penup()
turtle.goto(-5+0.4,-4)
turtle.pendown()
turtle.right(90)
for i in range(1):
    for color11 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color11)
        turtle.penup()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.left(91-0.5)
turtle.circle(220,89.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.circle(-215,90-1.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.end_fill()
#making left white boarder
turtle.penup()
turtle.goto(-6,5-0.1)
turtle.pendown()
turtle.left(179.5)
for i in range(1):
    for color11 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1',):
        turtle.begin_fill()
        turtle.fillcolor(color11)
        turtle.penup()
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.pendown()
        turtle.end_fill()
turtle.penup()
turtle.goto(-6,5-1)
turtle.pendown()
turtle.left(90)
for i in range(1):
    for color8 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1',):
        turtle.begin_fill()
        turtle.fillcolor(color8)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.end_fill()
turtle.penup()
turtle.goto(-5.3,5.4)
turtle.forward(220)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.right(91-0.6)
turtle.circle(-220,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.circle(215,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.end_fill()
# END BORDER'S
turtle.penup()
turtle.left(-90)
turtle.goto(0,239)
turtle.left(180)
turtle.circle(239,-40)
turtle.pendown()
for i in range(1):
    for  color1 in ('#c7c7c7','#8a8a8a','#7f7f7f','#6e6e6e','#595959','#4d4d4d','#3d3d3d','#242424','#242424','#3d3d3d','#4d4d4d','#595959','#6e6e6e','#7f7f7f','#8a8a8a','#c7c7c7'):
        turtle.begin_fill()
        turtle.fillcolor(color1)
        turtle.circle(239,10)
        turtle.left(90)
        turtle.penup()
        turtle.forward(8)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(-231,10)
        turtle.left(90)
        turtle.penup()
        turtle.forward(8)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(239,10)
        turtle.end_fill()
turtle.right(90+30)
turtle.penup()
turtle.goto(0,239)
turtle.pendown()
turtle.circle(239,-40)
turtle.fillcolor("#a4d3ee")
turtle.begin_fill()
turtle.left(90)
turtle.forward(8)
turtle.left(90)
turtle.circle(-231,200)
turtle.left(90)
turtle.forward(8)
turtle.left(90)
turtle.circle(239,200)
turtle.end_fill()
turtle.left(40)
# making "B"
turtle.penup()
turtle.goto(0,239)
turtle.circle(239,60)
turtle.right(90)
turtle.forward(15)
turtle.right(10)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(95)
turtle.right(90)
turtle.forward(75)
for i in range(8+1):
    turtle.forward(8)
    turtle.right(18)
turtle.left(30+100)
for i in range(8+1):
    turtle.forward(8)
    turtle.right(18)
turtle.left(20-7)
turtle.forward(80)
turtle.end_fill()
turtle.penup()
turtle.back(27)
turtle.right(90)
turtle.forward(17+2)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#bfbfbf")
turtle.forward(23)
turtle.right(90)
turtle.forward(45)
for i in range(5):
    turtle.forward(8/3)
    turtle.right(18)
for i in range(5):
    turtle.forward(8/2+0.5)
    turtle.right(18)
turtle.forward(43)
turtle.end_fill()
turtle.penup()
turtle.right(90)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#bfbfbf")
turtle.forward(21)
turtle.right(90)
turtle.forward(40)
for i in range(10):
    turtle.forward(7/2)
    turtle.right(18)
turtle.forward(40)
turtle.end_fill()
#making "m" letter
turtle.penup()
turtle.goto(-50-5,239)
turtle.left(42-1+180)
turtle.forward(10)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(93)
turtle.right(90)
turtle.forward(30-1)
turtle.right(68)
turtle.forward(70)
turtle.left(140)
turtle.forward(70)
turtle.right(74-0.3)
turtle.forward(33)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(20-1)
turtle.right(90)
turtle.forward(70-5)
turtle.left(160)
turtle.forward(70)
turtle.right(70)
turtle.forward(20)
turtle.right(70-3)
turtle.forward(70)
turtle.left(160)
turtle.forward(60+5)
turtle.right(90)
turtle.forward(20)
turtle.end_fill()
# MAKING LETTER "W"
turtle.penup()
turtle.goto(0,239)
turtle.circle(239,-59-0.7)
turtle.right(90+5)
turtle.forward(14)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(87)
turtle.left(100+3)
turtle.forward(21)
turtle.left(80-5)
turtle.forward(55)
turtle.right(150)
turtle.forward(55)
turtle.left(77)
turtle.forward(25-1)
turtle.left(80-7)
turtle.forward(55)
turtle.right(150)
turtle.forward(55)
turtle.left(76)
turtle.forward(22)
turtle.left(103)
turtle.forward(89)
turtle.left(90-13)
turtle.forward(24)
turtle.left(70+1)
turtle.forward(55+2)
turtle.right(140+5+0.5)
turtle.forward(57-0.5)
turtle.left(70+4)
turtle.hideturtle()
turtle.forward(25)
turtle.end_fill()
turtle.done()

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
