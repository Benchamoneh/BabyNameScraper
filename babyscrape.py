import urllib2 #web access
import re      #regexp

site = urllib2.urlopen('http://www.babynames.co.uk/letter-A.htm').read()
names = set(re.compile('name_([A-Z]\w+)').findall(site))

namelist = open('names.txt', 'w')

for name in names:
    #print name    
    namelist.write(name+"\n")

namelist.close()
#print re.compile
