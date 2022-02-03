import getpass
from requests import get
from os import name, system
import subprocess
import platform
import socket
import re
import uuid
import psutil
import winreg

# THIS CODE HAS BEEN MOVED TO A SEPARATE REPO


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


ip = get('https://api.ipify.org').content.decode('utf8')
user = getpass.getuser()


while True:
    stdin = input(user + ">")

    if stdin == "help":
        print("help | This command allows you to see all commands\n"
              "IP | This command allows you to see your public IP address\n"
              "software_installed | This command allows you to see all installed software on your computer\n"
              "pc_specs | This command allows you to see a variety of your computer's specifications\n"
              "clear | This command allows you to clear out all previous commands\n"
              "open | This command allows you to open software\n"
              "exit | This command allows you to leave this console")

    if stdin == "IP":
        print(ip)

    if stdin == "open":
        openin = input(user + "_open> ")
        if openin == "exit":
            break
        else:
            subprocess.call([openin])

    if stdin == "software_installed":
        software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,
                                                                                     winreg.KEY_WOW64_64KEY) + foo(
            winreg.HKEY_CURRENT_USER, 0)
        for software in software_list:
            print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
        print('Number of installed apps: %s' % len(software_list))

    if stdin == "pc_specs":
        print("Operative System |", platform.system(), "| Operative system release |", platform.release(), "| Operative system version", platform.version())
        print("Architecture |", platform.machine())
        print("Hostname |", socket.gethostname())
        print("Private IP-address |", socket.gethostbyname(socket.gethostname()))
        print("MAC-address |", ':'.join(re.findall('..', '%012x' % uuid.getnode())))
        print("Processor |", platform.processor())
        print("Amount of RAM-memory |", str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")

    if stdin == "clear":
        clear()

    if stdin == "exit":
        break
