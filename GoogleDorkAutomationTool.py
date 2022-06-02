import requests 
import argparse

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
 

#function get url from user 
def urlinput():
        url = input ("URL :")
        print("")
        return url

#function get filter according to the user 
def filter():
        print(" Filters available")
        print(" -----------------")
        print(" 1. Files containing username")
        print(" 2. Files containing passwords")
        print(" 3. Sensitive Directories")
        print(" 4. Web Server Detection")
        print(" 5. Files Containing Juicy Info")
        print(" 6. Pages Containing Login Portals")
        print(" 7. Content Management System Scan")
        print(" 8. No Filter(Display all)")
        print("")
        int = input(" Choose filter: ")
        print("")
        return int


#function called Dork (Files containing username)
def filter1(url):
        print("  "+"Files containing username")
        print("  "+"-------------------------")
        print(' | site:'+(url)+' inurl:"login="')
        print("")
      


#function called Dork (Files Containing passwords)
def filter2(url):
        print("  "+"Files containing passwords")
        print("  "+"--------------------------")
        print(' | site:'+(url)+' intext:"password"')
        print(' | site:'+(url)+' "password"')
        print(' | site:'+(url)+' "admin password"')
        print(' | site:'+(url)+' intext:pass.txt')
        print("")

#function called Dork (Sensitive Directories)
def filter3(url):
        print("  "+"Sensitive Directories")
        print("  "+"---------------------")
        print(' | inurl:/database* ext:sql intext:index of -site:'+(url))
        print(' | inurl:"/drive/folders/" site:'+(url))
        print(' | site:'+(url)+' shared by')
        print(' | intitle:index.of ios -site:'+(url))
        print(' | inurl:"folderview?id=" site:'+(url))
        print(' | intitle:"index of" "parent directory" "desktop.ini" site:'+(url))
        print("")
        

#function called Dork (Web Server Detection)
def filter4(url):
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        print(' | site:ftp.'+(url)+' "Web File Manager"')
        print(' | inurl:oraweb -site:'+(url))
        print("")
       


#function called Dork (Files Containing Juicy Info)
def filter5(url): 
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(' | "site:'+(url)+'"/""')
        print(' | intext:"password" | "passwd" | "pwd" site:'+(url))
        print(' | allintext:'+(url)+' filetype:log')
        print(' | intext:"SECRET_KEY=" site:'+(url))
        print(' | site:'+(url)+' "*.pdf"')
        print(' | intext:"private_key=" site:'+(url))
        print("")
       


#function called Dork (Pages Containin Login Portals)
def filter6(url): 
        print("  "+"Pages Containing Login Portals")
        print("  "+"------------------------------")
        print(' | site:"'+(url)+'" inurl:admin/index.php')
        print(' | inurl:("admin/password.php") +site:'+(url))
        print(' | site:'+(url)+' inurl:("administrator/login.php" OR "admin/login.php")')
        print(' | site:conf.'+(url)+'/signin/')
        print(' | site:login.'+(url)+'/signin/')
        print(' | site:admin.'+(url)+'/signin/')
        print(' | site:portal.'+(url)+'/signin/')
        print(' | site:social.'+(url)+'/signin/')
        print(' | site:accounts.'+(url)+'/signin/')
        print("")
       


#function called Dork (All dork)
def filter8(url):
        print("")
        filter1(url)
        print("")
        filter2(url)
        print("")
        filter3(url)
        print("")
        filter4(url)
        print("")
        filter5(url)
        print("") 
        filter6(url)
        print("")
        filter7(url)
        print("")
        
        

def get(websiteToScan):
    global user_agent
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    }
    return requests.get(websiteToScan, allow_redirects=False, headers=user_agent)
 
#function called CMS Scan 
def filter7(url): 
    print("  "+"Content Management System Scan")
    print("  "+"------------------------------")
    print("")
    # Check to see if the site argument was specified
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--site", help="Use this option to specify the domain or IP to scan.")
    args = parser.parse_args()
    if args.site is None:
        websiteToScan = url
    else:
        websiteToScan = args.site

    # Check the input for HTTP or HTTPS and then remove it, if nothing is found assume HTTP
    if websiteToScan.startswith('http://'):
        proto = 'http://'
        # websiteToScan = websiteToScan.strip('http://')
        websiteToScan = websiteToScan[7:]
    elif websiteToScan.startswith('https://'):
        proto = 'https://'
        # websiteToScan = websiteToScan.strip('https://')
        websiteToScan = websiteToScan[8:]
    else:
        proto = 'http://'

    # Check the input for an ending / and remove it if found
    if websiteToScan.endswith('/'):
        websiteToScan = websiteToScan.strip('/')

    # Combine the protocol and site
    websiteToScan = proto + websiteToScan

    # Check to see if the site is online
    print
    print("[+] Checking to see if the site is online...")

    try:
        onlineCheck = get(websiteToScan)
    except requests.exceptions.ConnectionError as ex:
        print("[!] " + websiteToScan + " appears to be offline.")
    else:
        if onlineCheck.status_code == 200 or onlineCheck.status_code == 301 or onlineCheck.status_code == 302:
            print(" |  " + websiteToScan + " appears to be online.")
            print
            print("Beginning scan...")
            print
            print("[+] Checking to see if the site is redirecting...")
            redirectCheck = requests.get(websiteToScan, headers=user_agent)
            if len(redirectCheck.history) > 0:
                if '301' in str(redirectCheck.history[0]) or '302' in str(redirectCheck.history[0]):
                    print("[!] The site entered appears to be redirecting, please verify the destination site to ensure accurate results!")
                    print("[!] It appears the site is redirecting to " + redirectCheck.url)
            elif 'meta http-equiv="REFRESH"' in redirectCheck.text:
                print("[!] The site entered appears to be redirecting, please verify the destination site to ensure accurate results!")
            else:
                print(" | Site does not appear to be redirecting...")
        else:
            print("[!] " + websiteToScan + " appears to be online but returned a " + str(
                onlineCheck.status_code) + " error.")
            print
            exit()

        print
        print("[+] Attempting to get the HTTP headers...")
        # Pretty print the headers - courtesy of Jimmy
        for header in onlineCheck.headers:
            try:
                print (" | " + header + " : " + onlineCheck.headers[header])
            except Exception as ex:
                print ("[!] Error: " + ex.message)

        ####################################################
        # WordPress Scans
        ####################################################

        print("")
        print ("[+] Running the WordPress scans...")
        print ("    ------------------------------")
        print("")

        # Use requests.get allowing redirects otherwise will always fail
        wpLoginCheck = requests.get(websiteToScan + '/wp-login.php', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Login page: " + websiteToScan + '/wp-login.php')
        else:
            print (" |  Not Detected: WordPress WP-Login page: " + websiteToScan + '/wp-login.php')

        # Use requests.get allowing redirects otherwise will always fail
        wpAdminCheck = requests.get(websiteToScan + '/wp-admin', headers=user_agent)
        if wpAdminCheck.status_code == 200 and "user_login" in wpAdminCheck.text and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Admin page: " + websiteToScan + '/wp-admin')
        else:
            print (" |  Not Detected: WordPress WP-Admin page: " + websiteToScan + '/wp-admin')

        wpAdminUpgradeCheck = get(websiteToScan + '/wp-admin/upgrade.php')
        if wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text:
            print ("[!] Detected: WordPress WP-Admin/upgrade.php page: " + websiteToScan + '/wp-admin/upgrade.php')
        else:
            print (" |  Not Detected: WordPress WP-Admin/upgrade.php page: " + websiteToScan + '/wp-admin/upgrade.php')

        wpAdminReadMeCheck = get(websiteToScan + '/readme.html')
        if wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text:
            print ("[!] Detected: WordPress Readme.html: " + websiteToScan + '/readme.html')
        else:
            print (" |  Not Detected: WordPress Readme.html: " + websiteToScan + '/readme.html')

        wpLinksCheck = get(websiteToScan)
        if 'wp-' in wpLinksCheck.text:
            print ("[!] Detected: WordPress wp- style links detected on index")
        else:
            print (" |  Not Detected: WordPress wp- style links detected on index")

        ####################################################
        # Joomla Scans
        ####################################################

        print("")
        print ("[+] Running the Joomla scans...")
        print ("    ---------------------------")
        print("")

        joomlaAdminCheck = get(websiteToScan + '/administrator/')
        if joomlaAdminCheck.status_code == 200 and "mod-login-username" in joomlaAdminCheck.text and "404" not in joomlaAdminCheck.text:
            print ("[!] Detected: Potential Joomla administrator login page: " + websiteToScan + '/administrator/')
        else:
            print (" |  Not Detected: Joomla administrator login page: " + websiteToScan + '/administrator/')

        joomlaReadMeCheck = get(websiteToScan + '/readme.txt')
        if joomlaReadMeCheck.status_code == 200 and "joomla" in joomlaReadMeCheck.text and "404" not in joomlaReadMeCheck.text:
            print ("[!] Detected: Joomla Readme.txt: " + websiteToScan + '/readme.txt')
        else:
            print (" |  Not Detected: Joomla Readme.txt: " + websiteToScan + '/readme.txt')

        joomlaTagCheck = get(websiteToScan)
        if joomlaTagCheck.status_code == 200 and 'name="generator" content="Joomla' in joomlaTagCheck.text and "404" not in joomlaTagCheck.text:
            print ("[!] Detected: Generated by Joomla tag on index")
        else:
            print (" |  Not Detected: Generated by Joomla tag on index")

        joomlaStringCheck = get(websiteToScan)
        if joomlaStringCheck.status_code == 200 and "joomla" in joomlaStringCheck.text and "404" not in joomlaStringCheck.text:
            print ("[!] Detected: Joomla strings on index")
        else:
            print (" |  Not Detected: Joomla strings on index")

        joomlaDirCheck = get(websiteToScan + '/media/com_joomlaupdate/')
        if joomlaDirCheck.status_code == 403 and "404" not in joomlaDirCheck.text:
            print ("[!] Detected: Joomla media/com_joomlaupdate directories: " + websiteToScan + '/media/com_joomlaupdate/')
        else:
            print (" |  Not Detected: Joomla media/com_joomlaupdate directories: " + websiteToScan + '/media/com_joomlaupdate/')

        ####################################################
        # Magento Scans
        ####################################################

        print("")
        print ("[+] Running the Magento scans...")
        print ("    ----------------------------")
        print("")

        magentoAdminCheck = get(websiteToScan + '/index.php/admin/')
        if magentoAdminCheck.status_code == 200 and 'login' in magentoAdminCheck.text and "404" not in magentoAdminCheck.text:
            print ("[!] Detected: Potential Magento administrator login page: " + websiteToScan + '/index.php/admin')
        else:
            print (" |  Not Detected: Magento administrator login page: " + websiteToScan + '/index.php/admin')

        magentoRelNotesCheck = get(websiteToScan + '/RELEASE_NOTES.txt')
        if magentoRelNotesCheck.status_code == 200 and 'magento' in magentoRelNotesCheck.text:
            print ("[!] Detected: Magento Release_Notes.txt: " + websiteToScan + '/RELEASE_NOTES.txt')
        else:
            print (" |  Not Detected: Magento Release_Notes.txt: " + websiteToScan + '/RELEASE_NOTES.txt')

        magentoCookieCheck = get(websiteToScan + '/js/mage/cookies.js')
        if magentoCookieCheck.status_code == 200 and "404" not in magentoCookieCheck.text:
            print ("[!] Detected: Magento cookies.js: " + websiteToScan + '/js/mage/cookies.js')
        else:
            print (" |  Not Detected: Magento cookies.js: " + websiteToScan + '/js/mage/cookies.js')

        magStringCheck = get(websiteToScan + '/index.php')
        if magStringCheck.status_code == 200 and '/mage/' in magStringCheck.text or 'magento' in magStringCheck.text:
            print ("[!] Detected: Magento strings on index")
        else:
            print (" |  Not Detected: Magento strings on index")

            # print magStringCheck.text

        magentoStylesCSSCheck = get(websiteToScan + '/skin/frontend/default/default/css/styles.css')
        if magentoStylesCSSCheck.status_code == 200 and "404" not in magentoStylesCSSCheck.text:
            print ("[!] Detected: Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css')
        else:
            print (" |  Not Detected: Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css')

        mag404Check = get(websiteToScan + '/errors/design.xml')
        if mag404Check.status_code == 200 and "magento" in mag404Check.text:
            print ("[!] Detected: Magento error page design.xml: " + websiteToScan + '/errors/design.xml')
        else:
            print (" |  Not Detected: Magento error page design.xml: " + websiteToScan + '/errors/design.xml')

        ####################################################
        # Drupal Scans
        ####################################################

        print("")
        print ("[+] Running the Drupal scans...")
        print ("    ---------------------------")
        print("")

        drupalReadMeCheck = get(websiteToScan + '/readme.txt')
        if drupalReadMeCheck.status_code == 200 and 'drupal' in drupalReadMeCheck.text and '404' not in drupalReadMeCheck.text:
            print ("[!] Detected: Drupal Readme.txt: " + websiteToScan + '/readme.txt')
        else:
            print (" |  Not Detected: Drupal Readme.txt: " + websiteToScan + '/readme.txt')

        drupalTagCheck = get(websiteToScan)
        if drupalTagCheck.status_code == 200 and 'name="Generator" content="Drupal' in drupalTagCheck.text:
            print ("[!] Detected: Generated by Drupal tag on index")
        else:
            print (" |  Not Detected: Generated by Drupal tag on index")

        drupalCopyrightCheck = get(websiteToScan + '/core/COPYRIGHT.txt')
        if drupalCopyrightCheck.status_code == 200 and 'Drupal' in drupalCopyrightCheck.text and '404' not in drupalCopyrightCheck.text:
            print ("[!] Detected: Drupal COPYRIGHT.txt: " + websiteToScan + '/core/COPYRIGHT.txt')
        else:
            print (" |  Not Detected: Drupal COPYRIGHT.txt: " + websiteToScan + '/core/COPYRIGHT.txt')

        drupalReadme2Check = get(websiteToScan + '/modules/README.txt')
        if drupalReadme2Check.status_code == 200 and 'drupal' in drupalReadme2Check.text and '404' not in drupalReadme2Check.text:
            print ("[!] Detected: Drupal modules/README.txt: " + websiteToScan + '/modules/README.txt')
        else:
            print (" |  Not Detected: Drupal modules/README.txt: " + websiteToScan + '/modules/README.txt')

        drupalStringCheck = get(websiteToScan)
        if drupalStringCheck.status_code == 200 and 'drupal' in drupalStringCheck.text:
            print ("[!] Detected: Drupal strings on index")
        else:
            print (" |  Not Detected: Drupal strings on index")

        ####################################################
        # phpMyAdmin Scans
        ####################################################

        print("")
        print ("[+] Running the phpMyAdmin scans...")
        print ("    -------------------------------")
        print("")

        phpMyAdminCheck = get(websiteToScan)
        if phpMyAdminCheck.status_code == 200 and 'phpmyadmin' in phpMyAdminCheck.text:
            print ("[!] Detected: phpMyAdmin index page")
        else:
            print (" |  Not Detected: phpMyAdmin index page")

        pmaCheck = get(websiteToScan)
        if pmaCheck.status_code == 200 and 'pmahomme' in pmaCheck.text or 'pma_' in pmaCheck.text:
            print ("[!] Detected: phpMyAdmin pmahomme and pma_ style links on index page")
        else:
            print (" |  Not Detected: phpMyAdmin pmahomme and pma_ style links on index page")

        phpMyAdminConfigCheck = get(websiteToScan + '/config.inc.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print ("[!] Detected: phpMyAdmin configuration file: " + websiteToScan + '/config.inc.php')
        else:
            print (" |  Not Detected: phpMyAdmin configuration file: " + websiteToScan + '/config.inc.php')

        print("")
        print ("Scan completed")
        print("")


# main process of the program 
url = urlinput()
int = filter() 
match int: 
    case '1':       
       filter1(url)

    case '2': 
       filter2(url)

    case '3': 
       filter3(url)

    case '4':
       filter4(url)

    case '5':      
       filter5(url)

    case '6': 
       filter6(url)

    case '7': 
       filter7(url)

    case '8':
       filter8(url)
      
       
print("")

banner = ''' 

░█─░█ ─█▀▀█ ░█▀▀█ ░█▀▀█ ░█──░█ 　 ░█─░█ ─█▀▀█ ░█▀▀█ ░█─▄▀ ▀█▀ ░█▄─░█ ░█▀▀█ 
░█▀▀█ ░█▄▄█ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ 　 ░█▀▀█ ░█▄▄█ ░█─── ░█▀▄─ ░█─ ░█░█░█ ░█─▄▄ 
░█─░█ ░█─░█ ░█─── ░█─── ──░█── 　 ░█─░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄█

'''
GREEN, RED = '\033[1;32m', '\033[91m'
print(GREEN + banner)

SystemExit
