## TMP leaker for CTF/Wargames

Developed by Harold Kim (root@stypr.com)

### How does it work?

1. Users and Teams are crawled from https://ctftime.org/ and made into wordlist.

2. Search temporary directory based on the wordlist.

3. List the directory if the given folder exists.

### Usage

Very simple, just type the following command on your bash!

* Python 2
`$ curl -s https://raw.githubusercontent.com/stypr/tmpleak/master/ctftime.py | python -u`

* Python 3
`$ curl -s https://raw.githubusercontent.com/stypr/tmpleak/master/ctftime.py | python3 -u`

### About

Released it for being the #1 team in CTFTime 2016. 

(I actually solved a lot of local exploitation challenges with this tool)

### Warning

1. Do not mess up the challenge server.

2. Do not do excessive scanning
