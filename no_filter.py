from typing import Counter
import requests
import progressbar 
import progressbar
from progressbar import ProgressBar
import sys
import typer 
import time

def filter8(url):
    print("  "+"Files containing username")
    print("  "+"-------------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.01)
            print("")
    print(' | site:'+(url)+' inurl:"login="')
    print("")
    print("  "+"Files containing passwords")
    print("  "+"--------------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.02)
            print("")
    print(' | site:'+(url)+' intext:"password"')
    print(' | site:'+(url)+' "password"')
    print(' | site:'+(url)+' "admin password"')
    print(' | site:'+(url)+' intext:pass.txt')
    print("")
    print("  "+"Sensitive Directories")
    print("  "+"---------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.03)
            print("")
    print(' | inurl:/database* ext:sql intext:index of -site:'+(url))
    print(' | inurl:"/drive/folders/" site:'+(url))
    print(' | site:'+(url)+' shared by')
    print(' | intitle:index.of ios -site:'+(url))
    print(' | inurl:"folderview?id=" site:'+(url))
    print(' | intitle:"index of" "parent directory" "desktop.ini" site:'+(url))
    print("")
    print("  "+"web Server Detection")
    print("  "+"--------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.02)
            print("")
    print(' | site:ftp.'+(url)+' "Web File Manager"')
    print(' | inurl:oraweb -site:'+(url))
    print("")
    print("  "+"Files Containing Juicy Info")
    print("  "+"---------------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.04)
            print("")
    print(' | "site:'+(url)+'"/""')
    print(' | intext:"password" | "passwd" | "pwd" site:'+(url))
    print(' | allintext:'+(url)+' filetype:log')
    print(' | intext:"SECRET_KEY=" site:'+(url))
    print(' | site:'+(url)+' "*.pdf"')
    print(' | intext:"private_key=" site:'+(url))
    print("")
    print("  "+"Pages Containing Login Portals")
    print("  "+"------------------------------")
    with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
            for value in progress:
                time.sleep(0.05)
            print("")
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

    wp_counter = 0
    wp = []
    jm_counter = 0
    jm = []
    mg_counter = 0
    mg = [] 
    dp_counter = 0 
    dp = [] 
    php_counter = 0
    php = []
    pbar = progressbar.ProgressBar()
    pbar = ProgressBar().start()
    total_steps = 5
    def get(websiteToScan):
        global user_agent
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        }
        return requests.get(websiteToScan, allow_redirects=False, headers=user_agent)

    print("  "+"Content Management System Scan")
    print("  "+"------------------------------")
    print("")
    websiteToScan = url
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
        Counter_Wordpress = 0    
        # Use requests.get allowing redirects otherwise will always fail
        wpLoginCheck = requests.get(websiteToScan + '/wp-login.php', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Login page: " + websiteToScan + '/wp-login.php')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/wp-login.php')
        else:
            print (" |  Not Detected: WordPress WP-Login page: " + websiteToScan + '/wp-login.php')

        wpLoginCheck = requests.get(websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress file manager " + websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php')
        else:
            print (" |  Not Detected: WordPress file manager: " + websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php')

        wpLoginCheck = requests.get(websiteToScan + '/cms/app/webroot', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "webroot" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Webroot: " + websiteToScan + '/cms/app/webroot')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/cms/app/webroot')
        else:
            print (" |  Not Detected: WordPress WP-Webroot: " + websiteToScan + '/cms/app/webroot')

        wpLoginCheck = requests.get(websiteToScan + '/login.jsp', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Login page: " + websiteToScan + '/login.jsp')
            Counter_Wordpress  += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/login.jsp')
        else:
            print (" |  Not Detected: WordPress WP-Login page: " + websiteToScan + '/login.jsp')

        # Use requests.get allowing redirects otherwise will always fail
        wpAdminCheck = requests.get(websiteToScan + '/wp-admin', headers=user_agent)
        if wpAdminCheck.status_code == 200 and "user_login" in wpAdminCheck.text and "404" not in wpLoginCheck.text:
            print ("[!] Detected: WordPress WP-Admin page: " + websiteToScan + '/wp-admin')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/wp-admin')
        else:
            print (" |  Not Detected: WordPress WP-Admin page: " + websiteToScan + '/wp-admin')

        wpAdminUpgradeCheck = get(websiteToScan + '/wp-admin/upgrade.php')
        if wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text:
            print ("[!] Detected: WordPress WP-Admin/upgrade.php page: " + websiteToScan + '/wp-admin/upgrade.php')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/wp-admin/upgrade.php')
        else:
            print (" |  Not Detected: WordPress WP-Admin/upgrade.php page: " + websiteToScan + '/wp-admin/upgrade.php')

        wpAdminReadMeCheck = get(websiteToScan + '/readme.html')
        if wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text:
            print ("[!] Detected: WordPress Readme.html: " + websiteToScan + '/readme.html')
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append(websiteToScan + '/readme.html')
        else:
            print (" |  Not Detected: WordPress Readme.html: " + websiteToScan + '/readme.html')

        wpLinksCheck = get(websiteToScan)
        if 'wp-' in wpLinksCheck.text:
            print ("[!] Detected: WordPress wp- style links detected on index")
            Counter_Wordpress += 1
            wp_counter = Counter_Wordpress
            wp.append('WordPress wp- style links detected on index')
        else:
            print (" |  Not Detected: WordPress wp- style links detected on index")
        pbar.update((1/5)*100)
        print("")

         ####################################################
        # Joomla Scans
        ####################################################
         
        print("")
        print ("[+] Running the Joomla scans...")
        print ("    ---------------------------")
        print("")
        Counter_Joomla = 0
        joomlaAdminCheck = get(websiteToScan + '/administrator/')
        if joomlaAdminCheck.status_code == 200 and "mod-login-username" in joomlaAdminCheck.text and "404" not in joomlaAdminCheck.text:
            print ("[!] Detected: Potential Joomla administrator login page: " + websiteToScan + '/administrator/')
            Counter_Joomla += 1
            jm_counter = Counter_Joomla
            jm.append(websiteToScan + '/administrator/')
        else:
            print (" |  Not Detected: Joomla administrator login page: " + websiteToScan + '/administrator/')

        joomlaReadMeCheck = get(websiteToScan + '/readme.txt')
        if joomlaReadMeCheck.status_code == 200 and "joomla" in joomlaReadMeCheck.text and "404" not in joomlaReadMeCheck.text:
            print ("[!] Detected: Joomla Readme.txt: " + websiteToScan + '/readme.txt')
            Counter_Joomla += 1
            jm_counter = Counter_Joomla  
            jm.append(websiteToScan + '/readme.txt')
        else:
            print (" |  Not Detected: Joomla Readme.txt: " + websiteToScan + '/readme.txt')

        joomlaTagCheck = get(websiteToScan)
        if joomlaTagCheck.status_code == 200 and 'name="generator" content="Joomla' in joomlaTagCheck.text and "404" not in joomlaTagCheck.text:
            print ("[!] Detected: Generated by Joomla tag on index")
            Counter_Joomla += 1
            jm_counter = Counter_Joomla
            jm.append('Generated by Joomla tag on index')
        else:
            print (" |  Not Detected: Generated by Joomla tag on index")

        joomlaStringCheck = get(websiteToScan)
        if joomlaStringCheck.status_code == 200 and "joomla" in joomlaStringCheck.text and "404" not in joomlaStringCheck.text:
            print ("[!] Detected: Joomla strings on index")
            Counter_Joomla += 1
            jm_counter = Counter_Joomla
            jm.append('Joomla strings on index')
        else:
            print (" |  Not Detected: Joomla strings on index")

        joomlaDirCheck = get(websiteToScan + '/media/com_joomlaupdate/')
        if joomlaDirCheck.status_code == 403 and "404" not in joomlaDirCheck.text:
            print ("[!] Detected: Joomla media/com_joomlaupdate directories: " + websiteToScan + '/media/com_joomlaupdate/')
            Counter_Joomla += 1
            jm_counter = Counter_Joomla
            jm.append(websiteToScan + '/media/com_joomlaupdate/')
        else:
            print (" |  Not Detected: Joomla media/com_joomlaupdate directories: " + websiteToScan + '/media/com_joomlaupdate/')
        pbar.update((2/5)*100)
        print("")

        ####################################################
        # Magento Scans
        ####################################################

        print("")
        print ("[+] Running the Magento scans...")
        print ("    ----------------------------")
        print("")
        Counter_Magento = 0
        magentoAdminCheck = get(websiteToScan + '/index.php/admin/')
        if magentoAdminCheck.status_code == 200 and 'login' in magentoAdminCheck.text and "404" not in magentoAdminCheck.text:
            print ("[!] Detected: Potential Magento administrator login page: " + websiteToScan + '/index.php/admin')
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/index.php/admin/')
        else:
            print (" |  Not Detected: Magento administrator login page: " + websiteToScan + '/index.php/admin')

        magentoRelNotesCheck = get(websiteToScan + '/RELEASE_NOTES.txt')
        if magentoRelNotesCheck.status_code == 200 and 'magento' in magentoRelNotesCheck.text:
            print ("[!] Detected: Magento Release_Notes.txt: " + websiteToScan + '/RELEASE_NOTES.txt')
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/RELEASE_NOTES.txt')
        else:
            print (" |  Not Detected: Magento Release_Notes.txt: " + websiteToScan + '/RELEASE_NOTES.txt')

        magentoCookieCheck = get(websiteToScan + '/js/mage/cookies.js')
        if magentoCookieCheck.status_code == 200 and "404" not in magentoCookieCheck.text:
            print ("[!] Detected: Magento cookies.js: " + websiteToScan + '/js/mage/cookies.js')
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/js/mage/cookies.js')
        else:
            print (" |  Not Detected: Magento cookies.js: " + websiteToScan + '/js/mage/cookies.js')

        magStringCheck = get(websiteToScan + '/index.php')
        if magStringCheck.status_code == 200 and '/mage/' in magStringCheck.text or 'magento' in magStringCheck.text:
            print ("[!] Detected: Magento strings on index")
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/index.php')
        else:
            print (" |  Not Detected: Magento strings on index")

            # print magStringCheck.text

        magentoStylesCSSCheck = get(websiteToScan + '/skin/frontend/default/default/css/styles.css')
        if magentoStylesCSSCheck.status_code == 200 and "404" not in magentoStylesCSSCheck.text:
            print ("[!] Detected: Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css')
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/skin/frontend/default/default/css/styles.css')
        else:
            print (" |  Not Detected: Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css')

        mag404Check = get(websiteToScan + '/errors/design.xml')
        if mag404Check.status_code == 200 and "magento" in mag404Check.text:
            print ("[!] Detected: Magento error page design.xml: " + websiteToScan + '/errors/design.xml')
            Counter_Magento += 1
            mg_counter = Counter_Magento
            mg.append(websiteToScan + '/errors/design.xml')
        else:
            print (" |  Not Detected: Magento error page design.xml: " + websiteToScan + '/errors/design.xml')
        pbar.update((3/5)*100)
        print("")

        ####################################################
        # Drupal Scans
        ####################################################

        print("")
        print ("[+] Running the Drupal scans...")
        print ("    ---------------------------")
        print("")
        Counter_Drupal = 0 
        drupalReadMeCheck = get(websiteToScan + '/readme.txt')
        if drupalReadMeCheck.status_code == 200 and 'drupal' in drupalReadMeCheck.text and '404' not in drupalReadMeCheck.text:
            print ("[!] Detected: Drupal Readme.txt: " + websiteToScan + '/readme.txt')
            Counter_Drupal += 1
            dp_counter = Counter_Drupal
            dp.append(" "+websiteToScan + '/readme.txt')
        else:
            print (" |  Not Detected: Drupal Readme.txt: " + websiteToScan + '/readme.txt')

        drupalTagCheck = get(websiteToScan)
        if drupalTagCheck.status_code == 200 and 'name="Generator" content="Drupal' in drupalTagCheck.text:
            print ("[!] Detected: Generated by Drupal tag on index")
            Counter_Drupal += 1
            dp_counter = Counter_Drupal
            dp.append(" "+'Generated by Drupal tag on index')
        else:
            print (" |  Not Detected: Generated by Drupal tag on index")

        drupalCopyrightCheck = get(websiteToScan + '/core/COPYRIGHT.txt')
        if drupalCopyrightCheck.status_code == 200 and 'Drupal' in drupalCopyrightCheck.text and '404' not in drupalCopyrightCheck.text:
            print ("[!] Detected: Drupal COPYRIGHT.txt: " + websiteToScan + '/core/COPYRIGHT.txt')
            Counter_Drupal += 1
            dp_counter = Counter_Drupal
            dp.append(" "+websiteToScan + '/core/COPYRIGHT.txt')
        else:
            print (" |  Not Detected: Drupal COPYRIGHT.txt: " + websiteToScan + '/core/COPYRIGHT.txt')
        
        drupalReadme2Check = get(websiteToScan + '/modules/README.txt')
        if drupalReadme2Check.status_code == 200 and 'drupal' in drupalReadme2Check.text and '404' not in drupalReadme2Check.text:
            print ("[!] Detected: Drupal modules/README.txt: " + websiteToScan + '/modules/README.txt')
            Counter_Drupal += 1
            dp_counter = Counter_Drupal
            dp.append(" "+websiteToScan + '/modules/README.txt')
        else:
            print (" |  Not Detected: Drupal modules/README.txt: " + websiteToScan + '/modules/README.txt')

        drupalStringCheck = get(websiteToScan)
        if drupalStringCheck.status_code == 200 and 'drupal' in drupalStringCheck.text:
            print ("[!] Detected: Drupal strings on index")
            Counter_Drupal += 1
            dp_counter = Counter_Drupal
            dp.append(" "+'Drupal strings on index')
        else:
            print (" |  Not Detected: Drupal strings on index")
        pbar.update((4/5)*100)
        print("")

        ####################################################
        # phpMyAdmin Scans
        ####################################################

        print("")
        print ("[+] Running the phpMyAdmin scans...")
        print ("    -------------------------------")
        print("")
        Counter_php = 0
        phpMyAdminCheck = get(websiteToScan)
        if phpMyAdminCheck.status_code == 200 and 'phpmyadmin' in phpMyAdminCheck.text:
            print ("[!] Detected: phpMyAdmin index page")
            Counter_php += 1
            php_counter = Counter_php
            php.append('phpMyAdmin index page')
        else:
            print (" |  Not Detected: phpMyAdmin index page")

        pmaCheck = get(websiteToScan)
        if pmaCheck.status_code == 200 and 'pmahomme' in pmaCheck.text or 'pma_' in pmaCheck.text:
            print ("[!] Detected: phpMyAdmin pmahomme and pma_ style links on index page")
            Counter_php += 1
            php_counter = Counter_php
            php.append('phpMyAdmin pmahomme and pma_ style links on index page')
        else:
            print (" |  Not Detected: phpMyAdmin pmahomme and pma_ style links on index page")

        phpMyAdminConfigCheck = get(websiteToScan + '/config.inc.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print ("[!] Detected: phpMyAdmin configuration file: " + websiteToScan + '/config.inc.php')
            Counter_php += 1
            php_counter = Counter_php
            php.append(websiteToScan+'/config.inc.php')
        else:
            print (" |  Not Detected: phpMyAdmin configuration file: " + websiteToScan + '/config.inc.php')

        phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/server_databases.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print ("[!] Detected: phpMyAdmin server database: " + websiteToScan + '/phpmyadmin/server_databases.php')
            Counter_php += 1
            php_counter = Counter_php
            php.append(websiteToScan+'/phpmyadmin/server_databases.php')
        else:
            print (" |  Not Detected: phpMyAdmin server database: " + websiteToScan + '/phpmyadmin/server_databases.php')

        phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/user_password.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print ("[!] Detected: phpMyAdmin user password: " + websiteToScan + '/phpmyadmin/user_password.php')
            Counter_php += 1
            php_counter = Counter_php
            php.append(websiteToScan+'/phpmyadmin/user_password.php')
        else:
            print (" |  Not Detected: phpMyAdmin user password: " + websiteToScan + '/phpmyadmin/user_password.php')

        phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/changelog.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print ("[!] Detected: phpMyAdmin changelog: " + websiteToScan + '/phpmyadmin/changelog.php')
            Counter_php += 1
            php_counter = Counter_php
            php.append(websiteToScan+'/phpmyadmin/changelog.php')
        else:
            print (" |  Not Detected: phpMyAdmin changelog: " + websiteToScan + '/phpmyadmin/changelog.php')
        pbar.update((5/5)*100)

        print("")
        print ("Scan completed")
        print("")
        print("-------------------------")
        print("-- Summary on CMS scan --")
        print("-------------------------")
        print("Wordpress CMS used   : ",wp_counter)
        print("----------------------------")
        print(*wp, sep=' \n')
        print("")

        print("Joomla CMS used      : ",jm_counter)
        print("----------------------------")
        print(*jm, sep=' \n')
        print("")

        print("Magento CMS used     : ",mg_counter)
        print("----------------------------")
        print(*mg, sep=' \n')
        print("")

        print("Drupal CMS used      : ",dp_counter)
        print("----------------------------")
        print(*dp, sep=' \n')
        print("")

        print("phpMyAdmin CMS used  : ",php_counter)
        print("----------------------------")
        print(*php, sep=' \n')
        print("")
        FilePath = 'ouput.txt'
        sys.stdout = open(FilePath, 'w')
        print("  "+"Files containing username")
        print("  "+"-------------------------")
        print(' | site:'+(url)+' inurl:"login="')
        print("")
        print("  "+"Files containing passwords")
        print("  "+"--------------------------")
        print(' | site:'+(url)+' intext:"password"')
        print(' | site:'+(url)+' "password"')
        print(' | site:'+(url)+' "admin password"')
        print(' | site:'+(url)+' intext:pass.txt')
        print("")
        print("  "+"Sensitive Directories")
        print("  "+"---------------------")
        print(' | inurl:/database* ext:sql intext:index of -site:'+(url))
        print(' | inurl:"/drive/folders/" site:'+(url))
        print(' | site:'+(url)+' shared by')
        print(' | intitle:index.of ios -site:'+(url))
        print(' | inurl:"folderview?id=" site:'+(url))
        print(' | intitle:"index of" "parent directory" "desktop.ini" site:'+(url))
        print("")
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        print(' | site:ftp.'+(url)+' "Web File Manager"')
        print(' | inurl:oraweb -site:'+(url))
        print("")
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(' | "site:'+(url)+'"/""')
        print(' | intext:"password" | "passwd" | "pwd" site:'+(url))
        print(' | allintext:'+(url)+' filetype:log')
        print(' | intext:"SECRET_KEY=" site:'+(url))
        print(' | site:'+(url)+' "*.pdf"')
        print(' | intext:"private_key=" site:'+(url))
        print("")
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
        print("")
        print("-------------------------")
        print("-- Summary on CMS scan --")
        print("-------------------------")
        print("Wordpress CMS used   : ",wp_counter)
        print("----------------------------")
        print(*wp, sep=' \n')
        print("")

        print("Joomla CMS used      : ",jm_counter)
        print("----------------------------")
        print(*jm, sep=' \n')
        print("")

        print("Magento CMS used     : ",mg_counter)
        print("----------------------------")
        print(*mg, sep=' \n')
        print("")

        print("Drupal CMS used      : ",dp_counter)
        print("----------------------------")
        print(*dp, sep=' \n')
        print("")

        print("phpMyAdmin CMS used  : ",php_counter)
        print("----------------------------")
        print(*php, sep=' \n')
        print("")

