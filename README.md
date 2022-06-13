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



Enumerated URL:  facebook.com


  Files containing username
  -------------------------
 | site:facebook.com inurl:"login="


  Files containing passwords
  --------------------------
 | site:facebook.com intext:"password"
 | site:facebook.com "password"
 | site:facebook.com "admin password"
 | site:facebook.com intext:pass.txt


  Sensitive Directories
  ---------------------
 | inurl:/database* ext:sql intext:index of -site:facebook.com
 | inurl:"/drive/folders/" site:facebook.com
 | site:facebook.com shared by
 | intitle:index.of ios -site:facebook.com
 | inurl:"folderview?id=" site:facebook.com
 | intitle:"index of" "parent directory" "desktop.ini" site:facebook.com


  web Server Detection
  --------------------
 | site:ftp.facebook.com "Web File Manager"
 | inurl:oraweb -site:facebook.com


  Files Containing Juicy Info
  ---------------------------
 | "site:facebook.com"/""
 | intext:"password" | "passwd" | "pwd" site:facebook.com
 | allintext:facebook.com filetype:log
 | intext:"SECRET_KEY=" site:facebook.com
 | site:facebook.com "*.pdf"
 | intext:"private_key=" site:facebook.com


  Pages Containing Login Portals
  ------------------------------
 | site:"facebook.com" inurl:admin/index.php
 | inurl:("admin/password.php") +site:facebook.com
 | site:facebook.com inurl:("administrator/login.php" OR "admin/login.php")
 | site:conf.facebook.com/signin/
 | site:login.facebook.com/signin/
 | site:admin.facebook.com/signin/
 | site:portal.facebook.com/signin/
 | site:social.facebook.com/signin/
 | site:accounts.facebook.com/signin/


  Content Management System Scan
  ------------------------------

[+] Checking to see if the site is online...
 |  http://facebook.com appears to be online.
Beginning scan...
[+] Checking to see if the site is redirecting...
[!] The site entered appears to be redirecting, please verify the destination site to ensure accurate results!
[!] It appears the site is redirecting to https://www.facebook.com/
[+] Attempting to get the HTTP headers...
 | Location : https://facebook.com/
 | Content-Type : text/html; charset="utf-8"
 | X-FB-Debug : GGTrpNvW4FjeX11T3ATQHI0yHMJUN5kx7/qxRgnxE5RJA6Wtwr2VZKnxSIMV+40u8QhjAHNAs0XJ9Hv0uADIGw==
 | Date : Mon, 13 Jun 2022 06:55:32 GMT
 | Alt-Svc : h3=":443"; ma=86400, h3-29=":443"; ma=86400
 | Connection : keep-alive
 | Content-Length : 0

[+] Running the WordPress scans...
    ------------------------------

 |  Not Detected: WordPress WP-Login page: http://facebook.com/wp-login.php
 |  Not Detected: WordPress WP-Admin page: http://facebook.com/wp-admin
 |  Not Detected: WordPress WP-Admin/upgrade.php page: http://facebook.com/wp-admin/upgrade.php
 |  Not Detected: WordPress Readme.html: http://facebook.com/readme.html
 |  Not Detected: WordPress wp- style links detected on index

[+] Running the Joomla scans...
    ---------------------------

 |  Not Detected: Joomla administrator login page: http://facebook.com/administrator/
 |  Not Detected: Joomla Readme.txt: http://facebook.com/readme.txt
 |  Not Detected: Generated by Joomla tag on index
 |  Not Detected: Joomla strings on index
 |  Not Detected: Joomla media/com_joomlaupdate directories: http://facebook.com/media/com_joomlaupdate/

[+] Running the Magento scans...
    ----------------------------

 |  Not Detected: Magento administrator login page: http://facebook.com/index.php/admin
 |  Not Detected: Magento Release_Notes.txt: http://facebook.com/RELEASE_NOTES.txt
 |  Not Detected: Magento cookies.js: http://facebook.com/js/mage/cookies.js
 |  Not Detected: Magento strings on index
 |  Not Detected: Magento styles.css: http://facebook.com/skin/frontend/default/default/css/styles.css
 |  Not Detected: Magento error page design.xml: http://facebook.com/errors/design.xml

[+] Running the Drupal scans...
    ---------------------------

 |  Not Detected: Drupal Readme.txt: http://facebook.com/readme.txt
 |  Not Detected: Generated by Drupal tag on index
 |  Not Detected: Drupal COPYRIGHT.txt: http://facebook.com/core/COPYRIGHT.txt
 |  Not Detected: Drupal modules/README.txt: http://facebook.com/modules/README.txt
 |  Not Detected: Drupal strings on index

[+] Running the phpMyAdmin scans...
    -------------------------------

 |  Not Detected: phpMyAdmin index page
 |  Not Detected: phpMyAdmin pmahomme and pma_ style links on index page
 |  Not Detected: phpMyAdmin configuration file: http://facebook.com/config.inc.php

Scan completed
```
### Further Improvement 
1. Add more CMS Google Dork scan from GHDB