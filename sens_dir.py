import typer 
import time
import sys
from typing import Counter
import requests
import progressbar 
import progressbar
from progressbar import ProgressBar
import sys
from googlesearch import search 

def filter3(url): 
        print("  "+"Sensitive Directories....1/6")
        print("  "+"----------------------------")
        #progress bar display part
        with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
                for value in progress:
                    time.sleep(0.03)
                print("")
        
        #web search for dorks =
        ws = []
        print(' | site:'+(url)+ ' inurl:/database* ext:sql intext:index of')
        q = 'site:'+(url)+ ' inurl:/database* ext:sql intext:index of'
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")

        #web search for dorks =
        print(' | site:'+(url)+' inurl:"/drive/folders/"' )
        q = 'site:'+(url)+' inurl:"/drive/folders/"'
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")

        #web search for dorks =
        print(' | site:'+(url)+' shared by')
        q = 'site:'+(url)+' shared by'
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")
        
        #web search for dorks =
        print(' | site:'+(url)+' intitle:index.of ios')
        q = 'site:'+(url)+' intitle:index.of ios'
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")

        #web search for dorks =
        print(' | site:'+(url)+' inurl:"folderview?id="')
        q = 'site:'+(url)+' inurl:"folderview?id="'
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")
        
        #web search for dorks =
        print(' | intitle:"index of" "parent directory" "desktop.ini" + site:'+(url))
        q = 'intitle:"index of" "parent directory" "desktop.ini" + site:'+(url)
        query = q
        count = 0 
        print("")
        for i in search(query, tld="com", num=10, stop=10, pause=5): 
            print(i)
            ws.append(i)   
            count += 1 
        print("   Result =",count)
        print("   -----------")
        print("")
        
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
           print ("[+] Running the WordPress scans.....2/6")
           print ("    -----------------------------------")
           Counter_Wordpress = 0    
           # Use requests.get allowing redirects otherwise will always fail
           wpLoginCheck = requests.get(websiteToScan + '/wp-login.php', headers=user_agent)
           if wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/wp-login.php')
          
           wpLoginCheck = requests.get(websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php', headers=user_agent)
           if wpLoginCheck.status_code == 200 and "404" not in wpLoginCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php')

           wpLoginCheck = requests.get(websiteToScan + '/cms/app/webroot', headers=user_agent)
           if wpLoginCheck.status_code == 200 and "webroot" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/cms/app/webroot')

           wpLoginCheck = requests.get(websiteToScan + '/login.jsp', headers=user_agent)
           if wpLoginCheck.status_code == 200 and "404" not in wpLoginCheck.text:
               Counter_Wordpress  += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/login.jsp')

           # Use requests.get allowing redirects otherwise will always fail
           wpAdminCheck = requests.get(websiteToScan + '/wp-admin', headers=user_agent)
           if wpAdminCheck.status_code == 200 and "user_login" in wpAdminCheck.text and "404" not in wpLoginCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/wp-admin')
  
           wpAdminUpgradeCheck = get(websiteToScan + '/wp-admin/upgrade.php')
           if wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/wp-admin/upgrade.php')

           wpAdminReadMeCheck = get(websiteToScan + '/readme.html')
           if wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append(websiteToScan + '/readme.html')
    
           wpLinksCheck = get(websiteToScan)
           if 'wp-' in wpLinksCheck.text:
               Counter_Wordpress += 1
               wp_counter = Counter_Wordpress
               wp.append('WordPress wp- style links detected on index')

           ####################################################
           # Joomla Scans
           ####################################################
         
           print("")
           print ("[+] Running the Joomla scans........3/6")
           print ("    -----------------------------------")
           Counter_Joomla = 0
           joomlaAdminCheck = get(websiteToScan + '/administrator/')
           if joomlaAdminCheck.status_code == 200 and "mod-login-username" in joomlaAdminCheck.text and "404" not in joomlaAdminCheck.text:
               Counter_Joomla += 1
               jm_counter = Counter_Joomla
               jm.append(websiteToScan + '/administrator/')

           joomlaReadMeCheck = get(websiteToScan + '/readme.txt')
           if joomlaReadMeCheck.status_code == 200 and "joomla" in joomlaReadMeCheck.text and "404" not in joomlaReadMeCheck.text:
               Counter_Joomla += 1
               jm_counter = Counter_Joomla  
               jm.append(websiteToScan + '/readme.txt')
 
           joomlaTagCheck = get(websiteToScan)
           if joomlaTagCheck.status_code == 200 and 'name="generator" content="Joomla' in joomlaTagCheck.text and "404" not in joomlaTagCheck.text:
               Counter_Joomla += 1
               jm_counter = Counter_Joomla
               jm.append('Generated by Joomla tag on index')

           joomlaStringCheck = get(websiteToScan)
           if joomlaStringCheck.status_code == 200 and "joomla" in joomlaStringCheck.text and "404" not in joomlaStringCheck.text:
               Counter_Joomla += 1
               jm_counter = Counter_Joomla
               jm.append('Joomla strings on index')

           joomlaDirCheck = get(websiteToScan + '/media/com_joomlaupdate/')
           if joomlaDirCheck.status_code == 403 and "404" not in joomlaDirCheck.text:
               Counter_Joomla += 1
               jm_counter = Counter_Joomla
               jm.append(websiteToScan + '/media/com_joomlaupdate/')

           ####################################################
           # Magento Scans
           ####################################################

           print("")
           print ("[+] Running the Magento scans.......4/6")
           print ("    -----------------------------------")
           Counter_Magento = 0
           magentoAdminCheck = get(websiteToScan + '/index.php/admin/')
           if magentoAdminCheck.status_code == 200 and 'login' in magentoAdminCheck.text and "404" not in magentoAdminCheck.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/index.php/admin/')

           magentoRelNotesCheck = get(websiteToScan + '/RELEASE_NOTES.txt')
           if magentoRelNotesCheck.status_code == 200 and 'magento' in magentoRelNotesCheck.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/RELEASE_NOTES.txt')

           magentoCookieCheck = get(websiteToScan + '/js/mage/cookies.js')
           if magentoCookieCheck.status_code == 200 and "404" not in magentoCookieCheck.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/js/mage/cookies.js')

           magStringCheck = get(websiteToScan + '/index.php')
           if magStringCheck.status_code == 200 and '/mage/' in magStringCheck.text or 'magento' in magStringCheck.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/index.php')

             # print magStringCheck.text

           magentoStylesCSSCheck = get(websiteToScan + '/skin/frontend/default/default/css/styles.css')
           if magentoStylesCSSCheck.status_code == 200 and "404" not in magentoStylesCSSCheck.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/skin/frontend/default/default/css/styles.css')

           mag404Check = get(websiteToScan + '/errors/design.xml')
           if mag404Check.status_code == 200 and "magento" in mag404Check.text:
               Counter_Magento += 1
               mg_counter = Counter_Magento
               mg.append(websiteToScan + '/errors/design.xml') 
           
           ####################################################
           # Drupal Scans
           ####################################################

           print("")
           print ("[+] Running the Drupal scans........5/6")
           print ("    -----------------------------------")
           Counter_Drupal = 0 
           drupalReadMeCheck = get(websiteToScan + '/readme.txt')
           if drupalReadMeCheck.status_code == 200 and 'drupal' in drupalReadMeCheck.text and '404' not in drupalReadMeCheck.text:
               Counter_Drupal += 1
               dp_counter = Counter_Drupal
               dp.append(" "+websiteToScan + '/readme.txt')

           drupalTagCheck = get(websiteToScan)
           if drupalTagCheck.status_code == 200 and 'name="Generator" content="Drupal' in drupalTagCheck.text:
               Counter_Drupal += 1
               dp_counter = Counter_Drupal
               dp.append(" "+'Generated by Drupal tag on index')

           drupalCopyrightCheck = get(websiteToScan + '/core/COPYRIGHT.txt')
           if drupalCopyrightCheck.status_code == 200 and 'Drupal' in drupalCopyrightCheck.text and '404' not in drupalCopyrightCheck.text:
               Counter_Drupal += 1
               dp_counter = Counter_Drupal
               dp.append(" "+websiteToScan + '/core/COPYRIGHT.txt')
        
           drupalReadme2Check = get(websiteToScan + '/modules/README.txt')
           if drupalReadme2Check.status_code == 200 and 'drupal' in drupalReadme2Check.text and '404' not in drupalReadme2Check.text:
               Counter_Drupal += 1
               dp_counter = Counter_Drupal
               dp.append(" "+websiteToScan + '/modules/README.txt')

           drupalStringCheck = get(websiteToScan)
           if drupalStringCheck.status_code == 200 and 'drupal' in drupalStringCheck.text:
               Counter_Drupal += 1
               dp_counter = Counter_Drupal
               dp.append(" "+'Drupal strings on index')
        
           ####################################################
           # phpMyAdmin Scans
           ####################################################

           print("")
           print ("[+] Running the phpMyAdmin scans....6/6")
           print ("    -----------------------------------")
           Counter_php = 0
           phpMyAdminCheck = get(websiteToScan)
           if phpMyAdminCheck.status_code == 200 and 'phpmyadmin' in phpMyAdminCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append('phpMyAdmin index page')
          
           pmaCheck = get(websiteToScan)
           if pmaCheck.status_code == 200 and 'pmahomme' in pmaCheck.text or 'pma_' in pmaCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append('phpMyAdmin pmahomme and pma_ style links on index page')

           phpMyAdminConfigCheck = get(websiteToScan + '/config.inc.php')
           if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append(websiteToScan+'/config.inc.php')

           phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/server_databases.php')
           if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append(websiteToScan+'/phpmyadmin/server_databases.php')

           phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/user_password.php')
           if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append(websiteToScan+'/phpmyadmin/user_password.php')

           phpMyAdminConfigCheck = get(websiteToScan + '/phpmyadmin/changelog.php')
           if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
               Counter_php += 1
               php_counter = Counter_php
               php.append(websiteToScan+'/phpmyadmin/changelog.php')

           print ("Scan completed")
           print("")
           print("")
           print("*************************")
           print("** Summary on CMS scan **")
           print("*************************")
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
        sys.stdout = open('D:/'+url+'_ouput_sens_dir.txt', 'w')
        print("***************************")
        print("** Sensitive Directories **")
        print("***************************")
        print(*ws, sep=' \n')
        print("")
        
        print("*************************")
        print("** Summary on CMS scan **")
        print("*************************")
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
        
        sys.stdout = open('D:/'+url+'_sensitive_dir_dorks.txt', 'w')
        print("*******************************")
        print("** Sensitive Directory Dorks **")
        print("*******************************")
        print("")
        print('site:'+(url)+ ' inurl:/database* ext:sql intext:index of')
        print('site:'+(url)+' inurl:"/drive/folders/"')
        print('site:'+(url)+' shared by')
        print('site:'+(url)+' intitle:index.of ios')
        print('site:'+(url)+' inurl:"folderview?id="')
        print('intitle:"index of" "parent directory" "desktop.ini" + site:'+(url))