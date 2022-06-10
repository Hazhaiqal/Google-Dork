def filter2(url):
        print("  "+"Files containing passwords")
        print("  "+"--------------------------")
        print(' | site:'+(url)+' intext:"password"')
        print(' | site:'+(url)+' "password"')
        print(' | site:'+(url)+' "admin password"')
        print(' | site:'+(url)+' intext:pass.txt')
        print("")