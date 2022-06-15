# Google Dork Automation Tool

### Description
An automation tool that enumerates the url given by user by utilizing Google Dork as enumeration tool 

### Available Dorks supported
1.  site:url inurl:"login=" 
2.  site:url intext:"password"
3.  site:url "admin password
4.  site:url "password"
5.  site:url intext:pass.txt 
6.  inurl:/database* ext:sql intext:index of -site:url
7.  inurl:"/drive/folders/" site:ur
8.  site:url shared by
9.  intitle:index.of ios -site:url
10. inurl:"folderview?id=" site:url 
11. intitle:"index of" "parent directory" "desktop ini" site:url
12. site:ftp.url "Web File Manager" 
13. inurl:oraweb -site:oraweb.org 
14. "site:url " / " "
15. intext:"password" | "passwd" | "pwd" site:url
16. allintext:url filetype:log
17. intext:"SECRET_KEY=" site:url
18. site:url "*.pdf"
19. intext:"API KEY site:url
20. intext:"private_key=" site:url
21. site:"url" inurl: admin/index.php
22. site:"url" inurl: admin/index.php
23. inurl:("admin/password.php") +site:url 
24. site:url inurl:("administrator/login.php" OR "admin/login.php")
25. site:conf.url/signin/
26. site:login.url/signin/
27. site:admin.url/signin/
28. site:portal.url/signin/
29. site:social.url/signin/
30. site:accounts.url/signin/
31. url/wp-login.php
32. url/wp-admin
33. url/upgrade.php
34. url/readme.html
35. wp style links on index 
36. url/administrator/
37. url/readme.txt
38. Joomla tag on Index 
39. url/media/com_joomlaupdate/
40. url/index.php/admin
41. url/RELEASE_NOTES.txt
42. url/js/mage/cookies.js 
43. Magento strings on Index
44. url/skin/frontend/default/default/css/styles.css
45. url/design.xml 
46. url/readme.txt
47. Drupal tag on Index 
48. url/core/COPYRIGHT.txt
49. url/modules/README.txt
50. Drupla strings on index 
51. phpMyAdmin index page 
52. phpMyAdmin pmahomme and pma_ style links on index page
53. url/config.inc.php
54. url/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php
55. url/cms/app/webroot 
56. url/login.jsp 
57. url/phpmyadmin/server_databases.php
58. url/phpmyadmin/user_password.php 
59. url/phpmyadmin/changelog.php

### How to use
```
python.exe GoogleDorkAutomationTool.py --help 

 
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


Usage: GoogleDorkAutomationTool.py [OPTIONS] [URL] [FILTER]

  Example : python.exe Typer1.py geeksforgeeks.com 3       

  Filter Available:

  1.  Files containing username

  2.  Files containing passwords

  3.  Sensitive Directories

  4.  Web Server Detection

  5.  Files Containing Juicy Info

  6.  Pages Containing Login Portals

  7.  Content Management System Scan

  8.  No Filter(Display all)

Arguments:
  [URL]     URL for enumeration
  [FILTER]  Filter number: 1...8

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.


python.exe GoogleDorkAutomationTool.py facebook.com 8 


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



Enumerated URL:  geeksforgeeks.com


  Files containing username
  -------------------------
 | site:geeksforgeeks.com inurl:"login="


  Files containing passwords
  --------------------------
 | site:geeksforgeeks.com intext:"password"
 | site:geeksforgeeks.com "password"
 | site:geeksforgeeks.com "admin password"
 | site:geeksforgeeks.com intext:pass.txt


  Sensitive Directories
  ---------------------
 | inurl:/database* ext:sql intext:index of -site:geeksforgeeks.com
 | inurl:"/drive/folders/" site:geeksforgeeks.com
 | site:geeksforgeeks.com shared by
 | intitle:index.of ios -site:geeksforgeeks.com
 | inurl:"folderview?id=" site:geeksforgeeks.com
 | intitle:"index of" "parent directory" "desktop.ini" site:geeksforgeeks.com


  web Server Detection
  --------------------
 | site:ftp.geeksforgeeks.com "Web File Manager"
 | inurl:oraweb -site:geeksforgeeks.com


  Files Containing Juicy Info
  ---------------------------
 | "site:geeksforgeeks.com"/""
 | intext:"password" | "passwd" | "pwd" site:geeksforgeeks.com
 | allintext:geeksforgeeks.com filetype:log
 | intext:"SECRET_KEY=" site:geeksforgeeks.com
 | site:geeksforgeeks.com "*.pdf"
 | intext:"private_key=" site:geeksforgeeks.com


  Pages Containing Login Portals
  ------------------------------
 | site:"geeksforgeeks.com" inurl:admin/index.php
 | inurl:("admin/password.php") +site:geeksforgeeks.com
 | site:geeksforgeeks.com inurl:("administrator/login.php" OR "admin/login.php")
 | site:conf.geeksforgeeks.com/signin/
 | site:login.geeksforgeeks.com/signin/
 | site:admin.geeksforgeeks.com/signin/
 | site:portal.geeksforgeeks.com/signin/
 | site:social.geeksforgeeks.com/signin/
 | site:accounts.geeksforgeeks.com/signin/


  Content Management System Scan
  ------------------------------

[+] Checking to see if the site is online...
 |  http://geeksforgeeks.com appears to be online.
Beginning scan...
[+] Checking to see if the site is redirecting...
 | Site does not appear to be redirecting...
[+] Attempting to get the HTTP headers...
 | Server : openresty
 | Date : Wed, 15 Jun 2022 01:19:49 GMT
 | Content-Type : text/html; charset=UTF-8
 | Transfer-Encoding : chunked
 | Connection : keep-alive
 | Set-Cookie : parking_session=f1f413fd-7bbf-5241-f47e-7b85489113f8; expires=Wed, 15-Jun-2022 01:34:49 GMT; Max-Age=900; path=/; HttpOnly
 | X-Adblock-Key : MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANDrp2lz7AOmADaN8tA50LsWcjLFyQFcb/P2Txc58oYOeILb3vBw7J6f4pamkAQVSQuqYsKx3YzdUHCvbVZvFUsCAwEAAQ==_WKpgsLEiP5FxqyCFQuaC8x59QyFceKQq/M70T7k/umXTRhKtTuiiDDQQ91Yx7K/K8ijq5y3Of+RFFepNJ6CsGA==
 | Cache-Control : no-cache, no-store, must-revalidate, post-check=0, pre-check=0
 | Expires : Thu, 01 Jan 1970 00:00:01 GMT
 | Pragma : no-cache
 | Content-Encoding : gzip

[+] Running the WordPress scans...
    ------------------------------

 |  Not Detected: WordPress WP-Login page: http://geeksforgeeks.com/wp-login.php
[!] Detected: WordPress file manager http://geeksforgeeks.com/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php
 |  Not Detected: WordPress WP-Webroot: http://geeksforgeeks.com/cms/app/webroot
[!] Detected: WordPress WP-Login page: http://geeksforgeeks.com/login.jsp
 |  Not Detected: WordPress WP-Admin page: http://geeksforgeeks.com/wp-admin
[!] Detected: WordPress WP-Admin/upgrade.php page: http://geeksforgeeks.com/wp-admin/upgrade.php
[!] Detected: WordPress Readme.html: http://geeksforgeeks.com/readme.html
 |  Not Detected: WordPress wp- style links detected on index

[+] Running the Joomla scans...
    ---------------------------

 |  Not Detected: Joomla administrator login page: http://geeksforgeeks.com/administrator/
 |  Not Detected: Joomla Readme.txt: http://geeksforgeeks.com/readme.txt
 |  Not Detected: Generated by Joomla tag on index
 |  Not Detected: Joomla strings on index
 |  Not Detected: Joomla media/com_joomlaupdate directories: http://geeksforgeeks.com/media/com_joomlaupdate/

[+] Running the Magento scans...
    ----------------------------

 |  Not Detected: Magento administrator login page: http://geeksforgeeks.com/index.php/admin
 |  Not Detected: Magento Release_Notes.txt: http://geeksforgeeks.com/RELEASE_NOTES.txt
[!] Detected: Magento cookies.js: http://geeksforgeeks.com/js/mage/cookies.js
 |  Not Detected: Magento strings on index
[!] Detected: Magento styles.css: http://geeksforgeeks.com/skin/frontend/default/default/css/styles.css
 |  Not Detected: Magento error page design.xml: http://geeksforgeeks.com/errors/design.xml

[+] Running the Drupal scans...
    ---------------------------

 |  Not Detected: Drupal Readme.txt: http://geeksforgeeks.com/readme.txt
 |  Not Detected: Generated by Drupal tag on index
 |  Not Detected: Drupal COPYRIGHT.txt: http://geeksforgeeks.com/core/COPYRIGHT.txt
 |  Not Detected: Drupal modules/README.txt: http://geeksforgeeks.com/modules/README.txt
 |  Not Detected: Drupal strings on index

[+] Running the phpMyAdmin scans...
    -------------------------------

 |  Not Detected: phpMyAdmin index page
 |  Not Detected: phpMyAdmin pmahomme and pma_ style links on index page
[!] Detected: phpMyAdmin configuration file: http://geeksforgeeks.com/config.inc.php
[!] Detected: phpMyAdmin server database: http://geeksforgeeks.com/phpmyadmin/server_databases.php
[!] Detected: phpMyAdmin user password: http://geeksforgeeks.com/phpmyadmin/user_password.php
[!] Detected: phpMyAdmin changelog: http://geeksforgeeks.com/phpmyadmin/changelog.php

Scan completed
```
### Further Improvement 
1. Add more CMS Google Dork scan from GHDB