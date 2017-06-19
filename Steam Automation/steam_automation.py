import pyautogui, subprocess, time, sys, json

try:
    with open('login.data', 'r') as d:
        credentials = json.load(d)
    d.close()

    pyautogui.FAILSAFE = True
    print('Launching Steam.exe...')
    path = ['C:\Program Files (x86)\Steam\Steam.exe']
    run_prog = subprocess.Popen(path)

    #Automation
    print("1 active account found. Getting it's credentials..")
    time.sleep(1)
    print("Uid of account founded is, "+credentials[0])
    time.sleep(4)
    x, y = 960, 455
    pyautogui.doubleClick(x, y, button='left')
    pyautogui.typewrite(credentials[1])
    print('Entering username... '+str(len(credentials[1]))+" length")
    x, y = 960, 489
    pyautogui.click(x, y, clicks=1, button='left')
    pyautogui.typewrite(credentials[2])
    print('Entering password...'+str(len(credentials[2]))+" length")
    pyautogui.typewrite(['enter'])
    print('Done!')

except FileNotFoundError:
    credentials = ["","",""]
    print("No active accounts found. Make sure you have at least 1 account setup as active.")

#End the program
sys.exit(0)
