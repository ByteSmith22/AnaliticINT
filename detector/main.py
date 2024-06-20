#archivo para detectar toda la actividad de mi computador

import psutil
import pygetwindow as gw
import keyboard
import mouse
import threading
import time
import analisis



# Variables
running = True
datewindows = []
anlt = analisis

#sección para crear funciones para el monitoreo
def monitorSystem():
    while running:
        print("CPU Usage:", psutil.cpu_percent(interval=1))
        print("Memory Usage:", psutil.virtual_memory().percent)
        time.sleep(1)  

def monitorWindows():
    while running:
        windows = gw.getAllWindows()
        for window in windows:
            datewindows.append(window.title)
            #print(window.title)
        time.sleep(5)  # Pausa para reducir la frecuencia de monitoreo

def on_keyEvent(event):
    print("Key:", event.name, "Event:", event.event_type, "Time:", event.time)

def on_clickEvent(event):
    print("Mouse:", event)

def result():
    ifnclear = []
    for date in datewindows:
        if(date != ""):        
            ifnclear.append(date)        
    
    return ifnclear
      

def stopMonitoring():
    global running
    running = False
    print("Deteniendo la monitorización...")
    anlt.showresult(result())


#codigo para incializar y configurar el monitoreo
#system_thread = threading.Thread(target=monitorSystem)
windows_thread = threading.Thread(target=monitorWindows)

#system_thread.start()
windows_thread.start()

keyboard.hook(on_keyEvent)
#mouse.hook(on_clickEvent)


#codigo para terminar el programa
keyboard.add_hotkey('ctrl+s', stopMonitoring)

keyboard.wait('ctrl+s')

#system_thread.join()
windows_thread.join()

print("Monitorización finalizada.")



