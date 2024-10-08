# ANSI 转义序列，用于设置文本颜色和重置文本属性
RESET = "\x1b[0m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"

# 打印彩色文本
banner_str = MAGENTA + """
      ░▀             ▀░   
　　 ▌▒▒░            ░▒▒▐  
　　 ░▒▒▒░          ░▒▒▒░  
　　▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐ 
　　░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ 
　    ▀▀▀  ▄▒▒▒▒▒▒▒▄  ▀▀▀  
　  ░░░▐ ░▀ ▒▒▒▒▒ ▀░ ▌░░░ 
　 ▐▌░░░▐▄▌░▐▌▒▒▒▐▌░▐▄▌░░▐▌   
　　 ░░░▐ ▌░░▌▒▒▒▐░░▐ ▌░░         
　　▒▀▄▄▄ ▄▄▄▌░▄░▐▄▄▄ ▄▄▀▒             ██        ██                     ██      ██ 
　　░░░░░░░░░░└┴┘░░░░░░░░░            ░██       ░░                     ░██     ░░
　　  ▄▄░░░░░░░░░░░░░░▄▄              ░██        ██  ███████    ██████ ░██  ██  ██  ███████ 
　　        ▒▒▒▒▒▒                    ░██       ░██ ░░██░░░██  ██░░░░  ░██ ██  ░██ ░░██░░░██
　　 ▀░░   ▒▒╖░░╥░░╓▒▐                ░██       ░██  ░██  ░██  ░█████  ░████   ░██  ░██  ░██ 
　　 ▒░   ▒▒╖░░╥░░╓▒▐                 ░██       ░██  ░██  ░██  ░░░░░██ ░██░██  ░██  ░██  ░██
　　 ▒░▀▀▀░░║░░║░░║░░                 ░████████ ░██  ███  ░██  ██████  ░██░░██ ░██  ███  ░██
　　▄▄▄▄▀▀┴┴╚╧╧╝╧╧╝┴┴                 ░░░░░░░░  ░░  ░░░   ░░  ░░░░░░   ░░  ░░  ░░  ░░░   ░░ 
　　                       
    """ + RESET

banner_str_welcome = GREEN + """
     ██       ██           ██                                            ██  ██  ██
    ░██      ░██          ░██                                           ░██ ░██ ░██
    ░██   █  ░██   █████  ░██   █████    ██████   ██████████    █████   ░██ ░██ ░██
    ░██  ███ ░██  ██░░░██ ░██  ██░░░██  ██░░░░██ ░░██░░██░░██  ██░░░██  ░██ ░██ ░██
    ░██ ██░██░██ ░███████ ░██ ░██  ░░  ░██   ░██  ░██ ░██ ░██ ░███████  ░██ ░██ ░██
    ░████ ░░████ ░██░░░░  ░██ ░██   ██ ░██   ░██  ░██ ░██ ░██ ░██░░░░   ░░  ░░  ░░ 
    ░██░   ░░░██ ░░██████ ███ ░░█████  ░░██████   ███ ░██ ░██ ░░██████   ██  ██  ██
    ░░       ░░   ░░░░░░ ░░░   ░░░░░    ░░░░░░   ░░░  ░░  ░░   ░░░░░░   ░░  ░░  ░░ 

""" + RESET