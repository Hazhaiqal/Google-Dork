import typer 
import time
def filter4(url):
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
                for value in progress:
                    time.sleep(0.02)
                print("")
        print(' | site:ftp.'+(url)+' "Web File Manager"')
        print(' | inurl:oraweb -site:'+(url))
        print("")