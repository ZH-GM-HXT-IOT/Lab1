import machine      
import time
pin_time=1                                #define time to judge which LED blinks
pin1 = machine.Pin(0, machine.Pin.OUT)    #define LED1       
pin2 = machine.Pin(2, machine.Pin.OUT)    #define LED2
while(1):   
    time.sleep_ms(200)                    #both LED sleeps 200ms before every circulation
    if pin_time % 5 == 1:                 #condition to control different LED blink frequency
        pin1.off()                        #LED1&2 blinks when time is an integral mutiple for 5
        pin2.off()
        time.sleep_ms(200)
        pin1.on()
        pin2.on()
    else:
        pin1.off()                        #only LED1 blinks when time is not an integral mutiple for 5
        time.sleep_ms(200)
        pin1.on()         
    pin_time = pin_time + 1               #time flips
           
