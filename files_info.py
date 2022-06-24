import typer 
import time
import sys
def filter5(url): 
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
        FilePath = 'ouput.txt'
        sys.stdout = open(FilePath, 'w')
        print("  "+"Files Containing Juicy Info")
        print("  "+"---------------------------")
        print(' | "site:'+(url)+'"/""')
        print(' | intext:"password" | "passwd" | "pwd" site:'+(url))
        print(' | allintext:'+(url)+' filetype:log')
        print(' | intext:"SECRET_KEY=" site:'+(url))
        print(' | site:'+(url)+' "*.pdf"')
        print(' | intext:"private_key=" site:'+(url))