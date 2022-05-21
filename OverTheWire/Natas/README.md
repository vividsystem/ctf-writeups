# Natas
This file contains my writeups and solutions for Natas

## 0
### Goal
find password for natas1
look trough sourcecode
-> gtVrDuiDfck831PqWsLEZy5gyDz1clto 

## 1
### Solution
Ctrl+Shift+C -> devtools
-> ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi 

## 2
### Solution
look trough source code
-> files/pixel.png 
try to browse files and there is a users.txt
-> sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14


## 3
### Solution
a comment says the following " No more information leaks!! Not even Google will find it this time... "

-> google stops crawling with a robots.txt file
so if i check the robots.txt it leads me to /s3cr3t
that displays /s3cr3t/users.txt
-> Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

## 4
### Writeup
send a request to natas4
where you have Referer: "http://natas5.natas.labs.overthewire.org/"
-> iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

## 5
### Writeup
you have to make a request where cookie "loggedin" is equal 1
-> aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

## 6
### Writeup
browse source code and look at the imports
then input the secret .
-> 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

## 7
### Writeup
when browsing the source code there is a hint: "password for webuser natas8 is in /etc/natas_webpass/natas8" there also is a parameter called page that loads the page via include() -> change parameter page to /etc/natas_webpass/natas8
-> DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 


## 8
### Writeup
the source code is given in it the secret is hard coded as variable and also the function to encode. to decode you have to first convert hex to string then and reverse the string then you get a base64 string that you have to convert from base64 to string and then you have your secret
-> W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

## 9 Writeup
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
input: "test; cat /etc/natas_webpass/natas10"
-> nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu


## 10 Writeup
there now is a filter in place
```php
```
we can get around this by using:
-E [a-z] /etc/natas_webpass/natas11
-> this matches everything containing a-z in /etc/natas_webpass/natas11 and dictionary with the pass being on top because its file got input first into grep

-> U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK