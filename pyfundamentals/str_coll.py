str = r'This \ is a raw string \ \ \ \ \  all back slashes'
print(str)

s1 = "debabrata patnaik"
print(s1.capitalize())
print(s1.title())
print(s1.upper())
print(s1.lower())

'''String to Byte conversion with encode and decode'''

s2 = "Un guineu marró ràpid va saltar sobre el gos mandrós"
print(s2.encode("utf-8"))
print(s2.encode("utf-8").decode("utf-8"))

"""List with details"""
a=[]
a.append(1)
a.append(2)
print(a)
print(list("Debabrata Patnaik"))

b = [1,
     2,
     3,
     4,
     5,
     None,]  # We can leave comma at the end python will not complain



print(b)

dc = {}
dc1 = {"k1":"v1","k2":2,"k3":3}
print(dc1["k3"])

dc1["k2"] = "v2"

print(dc1)

for d in dc1:
    print(d,dc1[d])

for v in dc1.values():
    print(v)


from urllib.request import urlopen

with urlopen("http://www.icndb.com/about/") as webdata:
    webwordlist = []
    webworddict = {}
    for line in webdata:
        line_words =  line.decode("utf-8").split()
        for word in line_words:
            webwordlist.append(word)
            webworddict[word] = webworddict.setdefault(word,0)+1

print(len(webworddict))
print(len(webwordlist))
