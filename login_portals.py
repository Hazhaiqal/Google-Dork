import typer 
import time
import sys
def filter6(url): 
        print("  "+"Pages Containing Login Portals...1/1")
        print("  "+"------------------------------------")
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
        FilePath = 'ouput.txt'
        sys.stdout = open(FilePath, 'w')
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