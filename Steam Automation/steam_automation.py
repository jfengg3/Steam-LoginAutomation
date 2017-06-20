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
    time.sleep(2)

    #if steam guard
    sguard_found = pyautogui.locateOnScreen('sguard.png')
    if sguard_found is not None:
        print('This account seems to be running on an authorization.')
        time.sleep(0.5)
        print('Searching for any available backup codes in PC..')
        time.sleep(0.5)
        try:
            x, y = 1068, 588
            code_path = 'C:\\Users\\admin\\Desktop\\codes.txt'

            with open(code_path, 'r') as f:
                print(code_path.split("\\")[-1] + " containing backup codes was found!")
                codelist = []
                for line in f:
                    codes = line.split('\n')
                    codelist.append(codes[0])
                print("File is holding " + str(len(codelist)) + " backup codes.")
                #Getting first code in the list
                getCode = codelist[0]
                pyautogui.click(x, y, clicks=1, button='left')
                pyautogui.typewrite(getCode)
                pyautogui.typewrite(['enter'])
                #Removing used code
                codelist.pop(0)
                #Updating codelist
                codes = ""
                for code in codelist:
                    codes += code + "\n"
                with open('C:\\Users\\admin\\Desktop\\codes.txt', 'w') as d:
                    d.write(codes)
                time.sleep(0.5)
                print('Done..! Logging-in.')

        except FileNotFoundError:
            print('Could not find any files with steam guard codes.')

    else:
        print('Account does not require any subsequent authentication.')
        time.sleep(0.5)
        print('Done..! Logging-in.')

except FileNotFoundError:
    credentials = ["","",""]
    print("No active accounts found. Make sure you have at least 1 account setup as active.")

#End the program
sys.exit(0)
