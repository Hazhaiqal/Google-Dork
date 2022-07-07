from googlesearch import search
def websearch(q):
    ws = []
    query = q 
    count = 0 
    print("")
    for i in search(query, tld="com", num=10, stop=10, pause=2): 
        print(i)
        ws.append(i)   
        count += 1 
    print("   Result =",count)
    print("   -----------")
    print("")
    