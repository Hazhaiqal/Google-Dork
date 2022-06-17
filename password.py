import typer 
import time
def filter2(url):
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