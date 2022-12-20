# %%
import requests
from bs4 import BeautifulSoup
import sys
# %%
searchterm = sys.argv[1]
# print(searchterm,end="\n\n")

# %%
url = "https://www.google.com/search?channel=fs&client=ubuntu&q="+\
    searchterm+\
    "+meaning"

# %%
r = requests.get(url)

# %%
soup=BeautifulSoup(r.content, 'html.parser')

# %%
s = soup.find_all("ol")
lis = []
for i in range(len(s)):
    lis += s[i].find_all("li")

# %%
outstring = ""
for i in range(len(lis)):
    synind = lis[i].text.find('synon')
    t = lis[i].text[:synind]
    
    quoind = t.find("'")
    if quoind != -1:
        outstring+=(t[:quoind]+'\n')       
        outstring+=('_'+t[quoind:]+'_'+'\n\n')
    else:
        outstring+=(t+'\n\n')

# %%
print(outstring)
