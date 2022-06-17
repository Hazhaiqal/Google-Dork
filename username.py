import typer
import time
def filter1(url):
        print("  "+"Files containing username")
        print("  "+"-------------------------")
        with typer.progressbar( label = "  Modifiying dorks ", length=100) as progress:      
                for value in progress:
                    time.sleep(0.01)
                print("")
        print(' | site:'+(url)+' inurl:"login="')
        print("")