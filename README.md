# Steam Login Automation
> Runs and login into Steam.exe automatically when script is run.

This is part of my 'study-the-examples' series, of how certain things can be done in python through 3rd-party libraries. Scripts are designed as accord to me, and not for client use. You can however download and edit them to work on your computer.

## Documentation

### Libraries
- PyAutoGUI

### Usage
This script is not yet compiled into an executable, thus you will need to compile it manually.

Also note for accounts with steam guard which requires code authentication, I have no idea how to get the code. This, I had resorted to creating another method which reads 'backup codes' (which can be generated through steam web) from a text file and automatically inputs into the authenticator.

This script can only assign one 'backup codes' text file to an account only! If more than one account requires authentication, it will not work flawlessly.

Codes must be written the following way:

![image](http://i.imgur.com/lUa5zT9.png)

#### !Note, before compiling the source
1. Setting the paths to locate
   * Open steam_automation.py
   * See line 10 > Set your steam.exe path (Eg. 'C:\Program Files (x86)\Steam\Steam.exe')
   * See line 38 > Set your 'backup codes' path (Eg. 'C:\\Users\\admin\\Desktop\\codes.txt')
2. Setting up accounts to run automation
   * Run script steam_accounts.py
   * Start adding as many steam accounts you wish
      * By default, all accounts will be inactive[0] once added. Only 1 account can be active[1] concurrently.
      * To change account's activity > Account list > Change account activity
   * The account with active status will be automated
   * Remember to exit the program systematically through option 5
   * You're ready to run the automation

#### Workflow
1. Make sure no existing steam processes are running
2. Run the script
3. It will automate the whole login process for you correspond to your active account
