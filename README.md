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
python.exe GoogleDorkAutomationTool.py URL FILTER

URL : URL for enumeration purposes 
FILTER : Numbers based on the available filter

Filters available
 -----------------
 1. Files containing username     
 2. Files containing passwords    
 3. Sensitive Directories
 4. Web Server Detection
 5. Files Containing Juicy Info   
 6. Pages Containing Login Portals
 7. Content Management System  Scan 
 8. No Filter(Display All)

Example : python.exe Typer1.py geeksforgeeks.com
 
 Enumeration results 
 ..........
 ..........
 ..........
```
### Further Improvement 
1. Add more CMS Google Dork scan from GHDB