import os
import subprocess as sp
import platform
import psutil
from pygame import mixer

paths = {
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'microsoft edge': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.exe",
}

def open_notepad():
    os.system("C:\\Windows\\notepad.exe")


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')

def open_microsoftEdge():
    os.startfile(paths['microsoft edge'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])


def shut_down():
    os.system('shutdown -s')


def re_start():
    os.system('shutdown -r')


def sys_info(my_system):
    my_system = platform.uname()

    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")



def get_cpu_temp():
    result = 0.0
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        if line.isdigit():
            result = float(line) / 1000
    return result


def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available * 1000)


def install(query):
    os.system("pip install" + query)

def stop_music():
    mixer.music.stop()


def pause_music():
    mixer.music.pause()

def telegram():
    os.system("telegram")


def excel():
    os.system("excel")


def power_point():
    os.system("powerpoint")

def word():
    os.system("winword")

def power_BI():
    os.system("Power BI Desktop")
