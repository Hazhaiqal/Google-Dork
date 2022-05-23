import webbrowser

banner = ''' 
 
░██████╗░░█████╗░░█████╗░░██████╗░██╗░░░░░███████╗  ██████╗░░█████╗░██████╗░██╗░░██╗
██╔════╝░██╔══██╗██╔══██╗██╔════╝░██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██╗░██║░░██║██║░░██║██║░░██╗░██║░░░░░█████╗░░  ██║░░██║██║░░██║██████╔╝█████═╝░
██║░░╚██╗██║░░██║██║░░██║██║░░╚██╗██║░░░░░██╔══╝░░  ██║░░██║██║░░██║██╔══██╗██╔═██╗░
╚██████╔╝╚█████╔╝╚█████╔╝╚██████╔╝███████╗███████╗  ██████╔╝╚█████╔╝██║░░██║██║░╚██╗
░╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

 ░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
 ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
 ███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
 ██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
 ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
 ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    
                  Made By: Muhammad Hazriq Haiqal bin Azhar  

'''
GREEN, RED = '\033[1;32m', '\033[91m'

print(GREEN + banner)


url = input ("URL :")
print("")

print(" Filters available")
print(" -----------------")
print(" 1. Files containing username")
print(" 2. Files containing passwords")
print(" 3. Sensitive Directories")
print(" 4. Web Server Detection")
print(" 5. Files Containing Juicy Info")
print(" 6. Pages Containing Login Portals")
print(" 7. None")
print("")
int = input(" Choose filter: ")
print("")

# displaying Google Dork enumeration link 
match int: 
    case '1': 
        print("  "+"Files containing username")
        print("  "+"-------------------------")
        print(f'site:'+(url)+' inurl:"login="')
        print("")
        webbrowser.open('http://google.com', new=1)
    case '2': 
        print("  "+"Files containing passwords")
        print("  "+"--------------------------")
        print(f'site:'+(url)+' intext:"password"')
        print(f'site:'+(url)+' "password"')
        print(f'site:'+(url)+' "admin password"')
        print(f'site:'+(url)+' intext:pass.txt')
        print("")
        webbrowser.open('http://google.com', new=1)
    case '3': 
        print("  "+"Sensitive Directories")
        print("  "+"---------------------")
        print(f'inurl:/database* ext:sql intext:index of -site:'+(url))
        print(f'inurl:"/drive/folders/" site:'+(url))
        print(f'site:'+(url)+' shared by')
        print(f'intitle:index.of ios -site:'+(url))
        print(f'inurl:"folderview?id=" site:'+(url))
        print(f'intitle:"index of" "parent directory" "desktop.ini" site:'+(url))
        print("")
        webbrowser.open('http://google.com', new=1)
    case '4':
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        print(f'site:ftp.'+(url)+' "Web File Manager"')
        print(f'inurl:oraweb -site:'+(url))
        print("")
        webbrowser.open('http://google.com', new=1)
    case '5':
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(f'"site:'+(url)+'"/""')
        print(f'intext:"password" | "passwd" | "pwd" site:'+(url))
        print(f'allintext:'+(url)+' filetype:log')
        print(f'intext:"SECRET_KEY=" site:'+(url))
        print(f'site:'+(url)+' "*.pdf"')
        print(f'intext:"private_key=" site:'+(url))
        print("")
        webbrowser.open('http://google.com', new=1)
    case '6': 
        print("  "+"Pages Containing Login Portals")
        print("  "+"------------------------------")
        print(f'site:"'+(url)+'" inurl:admin/index.php')
        print(f'inurl:("admin/password.php") +site:'+(url))
        print(f'site:'+(url)+' inurl:("administrator/login.php" OR "admin/login.php")')
        print(f'site:conf.'+(url)+'/signin/')
        print(f'site:login.'+(url)+'/signin/')
        print(f'site:admin.'+(url)+'/signin/')
        print(f'site:portal.'+(url)+'/signin/')
        print(f'site:social.'+(url)+'/signin/')
        print(f'site:accounts.'+(url)+'/signin/')
        print("")
        webbrowser.open('http://google.com', new=1)
    case '7': 
        print("  "+"Files containing username")
        print("  "+"-------------------------")
        print(f'site:'+(url)+' inurl:"login="')
        print("")
        print("  "+"Files containing passwords")
        print("  "+"--------------------------")
        print(f'site:'+(url)+' intext:"password"')
        print(f'site:'+(url)+' "password"')
        print(f'site:'+(url)+' "admin password"')
        print(f'site:'+(url)+' intext:pass.txt')
        print("")
        print("  "+"Sensitive Directories")
        print("  "+"---------------------")
        print(f'inurl:/database* ext:sql intext:index of -site:'+(url))
        print(f'inurl:"/drive/folders/" site:'+(url))
        print(f'site:'+(url)+' shared by')
        print(f'intitle:index.of ios -site:'+(url))
        print(f'inurl:"folderview?id=" site:'+(url))
        print(f'intitle:"index of" "parent directory" "desktop.ini" site:'+(url))
        print("")
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        print(f'site:ftp.'+(url)+' "Web File Manager"')
        print(f'inurl:oraweb -site:'+(url))
        print("") 
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(f'"site:'+(url)+'"/""')
        print(f'intext:"password" | "passwd" | "pwd" site:'+(url))
        print(f'allintext:'+(url)+' filetype:log')
        print(f'intext:"SECRET_KEY=" site:'+(url))
        print(f'site:'+(url)+' "*.pdf"')
        print(f'intext:"private_key=" site:'+(url))
        print("")
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(f'"site:'+(url)+'"/""')
        print(f'intext:"password" | "passwd" | "pwd" site:'+(url))
        print(f'allintext:'+(url)+' filetype:log')
        print(f'intext:"SECRET_KEY=" site:'+(url))
        print(f'site:'+(url)+' "*.pdf"')
        print(f'intext:"private_key=" site:'+(url))
        print("")
        webbrowser.open('http://google.com', new=1)
print("")

