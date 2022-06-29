import typer 
import time
import sys
def filter3(url):
        print("  "+"Sensitive Directories...1/1")
        print("  "+"---------------------------")
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
        FilePath = 'ouput.txt'
        sys.stdout = open(FilePath, 'w')
        print("  "+"Sensitive Directories")
        print("  "+"---------------------")
        print(' | inurl:/database* ext:sql intext:index of -site:'+(url))
        print(' | inurl:"/drive/folders/" site:'+(url))
        print(' | site:'+(url)+' shared by')
        print(' | intitle:index.of ios -site:'+(url))
        print(' | inurl:"folderview?id=" site:'+(url))
        print(' | intitle:"index of" "parent directory" "desktop.ini" site:'+(url))