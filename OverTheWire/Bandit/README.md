# OverTheWire Bandit

## Bandit Level 0
* Given: 
	* ssh login
	  user: bandit0
	  server: labs.overthewire.org
	  port: 2220
	  password: bandit0
* required to get to level 1: 
	* content of file readme ~/readme
* commands: ls, cd, cat, file, du, find

### Process
1. login
2. pwd -> check for ~
3. cat readme
-> boJ9jbbUNNfktd78OOpsqOltutMc3MY1

## Lvl 1
### Problem
Retrieve password for lvl 2 from lvl 1 
### Solution
As the file with the password is supposed to be called - we can just try that out and voila it works
cat ./- 
-> CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

## Lvl 2
### Problem
Retrieve password from file 'spaces in this filename'
## Solution
cat spaces\ in\ this\ filename
Tip: use tab
-> UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

## Lvl 3
### Problem
get password from hidden file
### Solution
-> pIwrPrtPN36QITSp3EQaw936yaFoFgAB

## Lvl 4
### Problem
get password from one of 9 files -> criteria: human-readable content
### Solution
file ./* | grep "text"
-> koReBOKuIDDepwhWk7jZC0RTdopnAYKh

## Lvl 5
### Problem
get filename of password file; criteria:
  human-readable
  1033 bytes size
  not executable
### Solution
find . -size 1033c -not -executable -> returns only one file: ./inhere/maybehere07/.file2
now run 'file ./inhere/maybehere07/.file2' and check that it is text

Tip find uses following sizes
  b -> 512-byte blocks
  c -> bytes
  w -> two byte words
  k -> kilobytes
  M -> Megabytes
  G -> Gigabytes

-> DXjZPULLxYr17uwoI01bNLQbtFemEgo7

## Lvl 6
### Problem 
get file owned by user bandit7 and group bandit6 which is 33 bytes of size
### Solution
find / -user bandit7 -group bandit6 -size 33c -> /var/lib/dpkg/info/bandit7.password
-> HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzis

## Lvl 7
### Problem 
password is in data.txt besides the word millionth
### Solution
grep "millionth" data.txt -> gets line with millionth in it 
-> cvX2JJa4CFALtqS87jk27qwqGhBM9plV

## Lvl 8
### Problem
password is the only line that is not duplicate
### Solution
cat data.txt | sort | uniq -u -> displays values -> sorts them -> filters them
-> UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

## Lvl 9
### Problem
retrieve passord from binary with multiple = preceeding the password
### Solution
strings data.txt | grep "=="
-> truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

## Lvl 10echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
### Problem
retrieve password from base64 encoded
### Solution
base64 -d data.txt
-> IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

## Lvl 11
### Problem
get password from shift cypher 
### Solution
-> Rot13 decoder online
-> 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

## Lvl 12
### Goal
get password from hexdump of compressed binary
### Solution
1. Get compressed binary from hexdump -> xxd -r hexdump compressed
2. Determine compression used on binary -> file compressed
3. rename compressed binary to match compression -> tar for tar, gz for gzip, bz2 for bzip2
4. now repeat step 2 and 3 until it shows ascii text instead of compressed
-> 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

## Lvl 13 
### Goal
get access to lvl 14 user to get lvl 134 password 
## Solution
ssh-add sshkey.private
ssh bandit14@bandit.labs.overthewire.org 
cat /etc/bandit_pass/bandit14
-> 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

## Lvl 14
### Goal
make somekind of connection to localhost:30000 that returns password
### Solution
nc localhost 30000 -> after that input your password and enter
-> BfMYroe26WYalil77FoDi9qh59eK5xNr

## Lvl 15
### Goal
connect to localhost 30001 with ssl 
### Solution use s_client
openssl s_client -host localhost -port 30001 -> then input your current password and enter
-> cluFn7wTiGryunymYOu4RcffSxQluehd

## Lvl 16
### Goal
connect to server somewhere between localhost port 31000-32000
### Solution
nmap localhost -p 31000-32000
after that try which one accepts your password
-> returns ssh private key

## Lvl 17 
### Goal 
get diffs between two files
### Solution
diff passwords.old passwords.new | grep ">"
-> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

## Lvl 18
### Goal
.bashrc kicks you out of ssh
### Solution
ssh bandit18@bandit.labs.overthewire.org cat readme
-> IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

## Lvl 19
### Goal
use setuid script to get lvl 20 password
### Solution
./bandit20-do cat /etc/bandit_pass/bandit20
-> GbKksEFF4yrVs6il55v6gwY5aVje5f0j


## Lvl 20
### Goal
start netcat listener and setuid command on same connection
### Solution
use tmux to create 2 windows and then use one for netcat and the other for the binary
-> gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr


## Lvl 21
### Goal
get infos about a cronjob
### Solution
ls /etc/cron.d/
cat /etc/cron.d/cronjob_bandit22
-> executed a shell script
cat /usr/bin/cronjob_bandit22.sh
-> puts password in a tmp file
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
-> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI


## Lvl 22
### Goal
look at a cronjob
### Solution
ls /etc/cron.d/
cat /etc/cron.d/cronjob_23
cat /usr/bin/cronjob_bandit23.sh
```bash
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
cat /tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
-> jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n


## Lvl 23
### Goal
analize a cronjob again
### Write-up
ls /etc/cron.d/
ls /etc/cron.d/cronjob_24
cat /usr/bin/cronjob_24.sh
```bash
!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
-> It deletes and executes everything in /var/spool/bandit24
vim /var/spool/bandit24/script.sh
```bash
cat /etc/bandit_pass/bandit24 > /tmp/bandit24
```
cat /tmp/bandit24
-> UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## Lvl 24
### Goal
bruteforce localhost 30002
### Solution
write a simple script 
that uses pythons sockets lib to connect and try everything from 0 to 9999
-> uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG 



## Lvl 25
### Goal
escape more command
### Solution
make terminal height small then press v this puts you into vim from where you can do :e /etc/bandit_pass/bandit26
-> 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

## Lvl 26
### Goal
get shell in vim
### Solution
after logging into bandit26 as described in lvl 25
set your shell -> :set shell=/bin/sh
then run ~/bandit27-do cat /etc/bandit_pass/bandit27
-> 3ba3118a22e93127a4ed485be72ef5ea#

## Lvl 27
### Goal
clone repo
### Solution
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
-> repo contains README
-> 0ef186ac70e04ea33b4c1853d2526fa2

## Lvl 28-29
### Goal
clone repo and find out data
### Solution
after cloning:
cd repo
git log
git checkout <commit> -> where the password still was in the data
-> bbc96594b4e001778eee9975372716b2

## Lvl 29-30
### Goal
find password in git repo
### Solution
README says no passwords in production so i look for other branches
git branch -r
then i switch to origin/dev
git checkout origin/dev
and then cat README
-> 5b90576bedb2cc04c86a9e924ce42faf

## Lvl 30-31
### Goal
find password in git repo
### Solution
git tag
git show secret
-> 47e603bb428404d265f59c42920d81e5

## Lvl 31-32
### Goal
push file to origin
### Solution
create file key.txt with Content "May I come in?"
git add -f key.txt
git commit -m "<commit message>"
git push origin master
-> 56a9bf19c63d650ce78e6ec0354ee45e

## Lvl 32-33
### Goal
escape hell aka the uppercase shell
### Solution
$0
now you have a normal shell
whoami -> bandit33
cat /etc/bandit_pass/bandit33
-> c9c3199ddf4121b10cf581a98d51caee