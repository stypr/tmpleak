## TMP leaker for CTF/Wargames

Developed by Harold Kim (root@stypr.com)

### How does it work?

1. Users and teams are crawled from ctftime.org and made into wordlist.

2. Search temporary directory based on the wordlist.

3. List the directory if the given folder is existant.

### Usage

Very simple, just type the following command on your bash!

`$ curl -s https://raw.githubusercontent.com/stypr/tmpleak/master/ctftime.py | python -u`

### About

Released it for being the #1 team in CTFTime 2016. 

(I actually solved a lot of local exploitation challenges with this tool)

Side Note: Do not screw up challenge servers :p
