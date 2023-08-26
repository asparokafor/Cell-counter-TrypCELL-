#@aspar_okafor
#trypcell_python
import sys
import time
import turtle
import os

def menu_lines():
        print("_" *80)
        print()

def exiting():
    f=0
    while f<3:
        f+=1
        print('[exiting', '.'*f, ']')
        time.sleep(0.2)
    sys.exit()

print("[TrypCell V1.0 - @aspar_okafor]")
menu_lines()
print("[tip: use 5 counting cells for real values]")
menu_lines()
time.sleep(1)
enter = input("[PRESS ENTER TO CONTINUE...]")

while enter!='':
    if enter !='':
                print("[wrong input, try again]")
                enter = input('PRESS ENTER TO CONTINUE')

while enter =='':
    if enter =='':
                os.system('clear')
                menu_lines()
                print('1.) Using trypan blue and PBS')
                menu_lines()
                print('2.) Using only PBS')
                menu_lines()
                print('3.) Exit')
                menu_lines()
                choice = input('CHOOSE ONE: ')
                if choice == '3':
                        exiting()

                if choice == '2':
                        os.system('clear')
                        dil_PBS = int(input("HOW MUCH PBS DO YOU USE? "))
                        dil_CELLS = int(input("HOW MUCH CELL SOLUTION DO YOU USE? "))
                        D=(dil_CELLS+dil_PBS)/dil_CELLS
                                #aquire data for more math
                        i = int(input("Total cells: "))
                        v=i/5
                        print('Average # of cells/square ', round(v))
                        menu_lines()
                        print('Dilution Factor ', D)
                        menu_lines()
                        c=v*D*10000
                        print('Concentration (Viable cells/ml) ', round(c), 'cells/ml')
                        print()
                        menu_lines()
                        exiting()
                                                                                            
                if choice == '1':
                        os.system('clear')
                        dil_PBS = int(input("HOW MUCH PBS DO YOU USE? "))
                        dil_TRY = int(input("HOW MUCH TRYPAN BLUE DO YOU USE? "))
                        dil_CELLS = int(input("HOW MUCH CELL SOLUTION DO YOU USE? "))

                        D=(dil_CELLS+dil_PBS+dil_TRY)/dil_CELLS
                        i = int(input('Total (viable) cells '))
                        z = int(input('Total non-viable cells '))
                        menu_lines()
                        p=i/(i+z)
                        p=p*100
                        print('Percentage of viable cells: ',round(p), '%')
                        menu_lines()
                        v=(i+z)/5
                        print('Average # of cells/square ',round(v))
                        menu_lines()
                        D=(dil_CELLS+dil_PBS)/dil_CELLS
                        print('Dilution factor ', D)
                        menu_lines()
                        c=v*D*10000
                        print('Concentration (Total cells/ml) ', round(c), 'cells/ml')
                        menu_lines()
                        v=i/5
                        c=v*D*10000
                        print('Concentration (Viable cells/ml)', round(c), 'cells/ml')
                        menu_lines()
                        enter = input('PRESS ENTER TO EXIT ')
                        while enter != '':
                                if enter =='':
                                        sys.exit()
                                elif enter !='':
                                        print("[wrong input]")
                                        enter = input('PRESS ENTER TO EXIT ')

                if choice !='3' or '2' or '1':
                        print("[wrong input, exiting]")
                        sys.exit()

