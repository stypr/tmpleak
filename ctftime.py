#!/usr/bin/python -u
#-*- coding: utf-8 -*-
import os
import sys
import urllib2
""" Made by stypr, Don't blame me for your system's ignorance!
Usage: curl -s https://ctf.stypr.com/ctftime/ctftime.py | python -u
"""
os.popen("rm -rf %s"%(sys.argv[0])).read()
p = "https://ctf.stypr.com/ctftime"
q = ("/var/tmp/","/var/tmp/\~","/var/tmp/.","/tmp/","/tmp/.","/tmp/\~")
k = lambda x: x.split("\n")
x = k(urllib2.urlopen("%s/user.pwn"%(p,)).read())
y = k(urllib2.urlopen("%s/team.pwn"%(p,)).read())
z = list(set([i for i in x+y if i and i.isalnum()]))
n = 0
m = len(z)
t = 40
c = lambda x: " "*(t-len(x))
for i in z:
	n += 1
	f = "\r[%s/%s] Checking %s...%s"%(n,m,i,c(i))
	sys.stdout.flush( )
	sys.stdout.write(f)
	for j in q:
		r = os.popen('ls -al "'+j+i+'" 2>&1').read()
		s = os.popen('ls -al "'+j+i.lower()+'" 2>&1').read()
		e = "No such file or directory"
		if (e not in r) and (e not in s):
			sys.stdout.flush( )
			if e in r:
				print("\n[Found: %s]\n%s"%(j+i,r))
			else:
				print("\n[Found: %s]\n%s"%(j+i.lower(),r))
