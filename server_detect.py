def filter4(url):
        print("  "+"web Server Detection")
        print("  "+"--------------------")
        print(' | site:ftp.'+(url)+' "Web File Manager"')
        print(' | inurl:oraweb -site:'+(url))
        print("")