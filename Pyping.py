import os
import time
from pythonping import ping

os.system('cls')
print("Attention : Le programme doit être exécuté en tant qu'administrateur")
time.sleep(5)
os.system('cls')

install = input('Avez vous installé pystyle et pythonping ? (O/N)\n> ')
if install == "O":
    pass
else:
    pip = input(' [0] Pip | [1] Pip3\n> ')
    if pip == "0":
        os.system('pip install pystyle')
        os.system('pip install pythonping')
    else:
        print('Erreur')
    if pip == "1":
         os.system('pip3 install pystyle')
         os.system('pip3 install pythonping')
    else:
        print('Erreur')

os.system('cls')

import pystyle
from pystyle import *

Banner1 = """
██████╗ ██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝ 
██████╔╝ ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗
██╔═══╝   ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║
██║        ██║   ██║     ██║██║ ╚████║╚██████╔╝
╚═╝        ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝"""

Banner2 = (r"""
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'   0x#7012""")

print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner2, Banner1, 

center=True), 2)))
print()
print()
ip     = str(Write.Input("IP > ", Colors.yellow_to_red, interval=0.0001))
sec     = str(Write.Input("Time > ", Colors.yellow_to_red, interval=0.0002))

os.system('cls')

ping(f'{ip}', count=f'{sec}', verbose=True)
time.sleep(3)
os.system('cls')
