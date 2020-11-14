#-*- coding: utf-8 -*-
""" Made by stypr, Don't blame me for your system's ignorance! """
import os, sys
try: from urllib.request import urlopen
except: from urllib2 import urlopen
os.popen("rm -rf %s"%(sys.argv[0])).read()
p = "https://raw.githubusercontent.com/stypr/tmpleak/master"
q = ("/var/tmp/","/var/tmp/\~","/var/tmp/.","/tmp/","/tmp/.","/tmp/\~")
k = lambda x:x.decode("utf-8").split("\n")
x = k(urlopen("%s/user.pwn"%(p,)).read())
y = k(urlopen("%s/team.pwn"%(p,)).read())
z = list(set([i for i in x+y if i and i.isalnum()]))
n = 0
m = len(z)
t = 40
c = lambda x:" "*(t-len(x))
for i in z:
 n += 1
 f = "\r[%s/%s] Checking %s...%s"%(n,m,i,c(i))
 sys.stdout.flush()
 sys.stdout.write(f)
 for j in q:
  r = os.popen('ls -al "'+j+i+'" 2>&1').read()
  s = os.popen('ls -al "'+j+i.lower()+'" 2>&1').read()
  e = "No such file or directory"
  if (e not in r) or (e not in s):
   sys.stdout.flush()
   if e in r:
    print("\n[Found: %s]\n%s"%(j+i.lower(),s))
   else:
    print("\n[Found: %s]\n%s"%(j+i,r))
print
