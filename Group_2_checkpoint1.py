import machine
import time

def One_chara(chara):                           #define the function that send a single Morse code
    if chara == 'S':
        times = 500                             #if the code to send is 's', the interval is configured to be short       
    else:
        times = 1000                            #if the code to send is 'o', the interval is configured to be long       
        
    
    for i in range(1,3):
        pin.on()
        time.sleep_ms(times)
        pin.off()
        time.sleep_ms(times)

    
pin = machine.Pin(2,machine.Pin.OUT)          # preconfiguration
pin.on()

while (1):                          
    One_chara('S')
    One_chara('O')
    One_chara('S')
    time.sleep_ms(200)                       # short interval between each "SOS" 
 
    
