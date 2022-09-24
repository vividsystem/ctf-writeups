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


## 11 Writeup
The website uses xor encryption

We know the plaintext and encrypted text so we can get the key <br>
plaintext ⊕ key = encrypted_text <br>
encrypted_text ⊕ plaintext = key <br>
encrypted_text ⊕ key = plaintext

-> EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

# 12 Writeup
This websites lets you upload a file(max 1KB) to the server and then open via link. While looking at the code however you can see that the extension can be modified client side. <br>
Then I quickly crafted a [payload](./12/payload.php)) that I then uploaded. <br>
After that I modified the POST-request so that the file extension was .php
-> jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

# 13 Writeup
This time when you upload a picture it checks the filetype. It then becomes apparent that this is done using the `exif_imagetype` function. After a bit of reasearch I was able to find out that this function checks the first four bytes of a file.
I then changed the first four bytes to "FF D8 FF E0" in a hex-editor. After that I selected my [payload](./13/payload.php) to then make the POST-request which I again modified as described in [12](#12-writeup)
This then gave back the first four bytes + the password for natas14
-> Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

# 14 Writeup
This time there is a login with a username and password. I then looked through the source code I then saw that the code was making use of a raw SQL Query(
`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; `). This made it extremly apparant that the goal was to achieve a SQL-Injection. I then tried out some basic ones in the password field: `" 1 = 1`, `natas15" #`.
-> AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

# 15 Writeup
This time it didn't explicitly tell you the password upon injecting something into the query. Therefore I had to do blind SQLi's. So I quickly made a [script](./15/main.py) that first gets every character used in the password and then iterates over those characters 32 times to get the password.
-> WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

# 16 Writeup
This time where doing a "blind injection". 
My [script](16/main.py) uses a word from the dictionary + random letters as input so if there is nothing returned in the output it means those letters in the password
-> 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

# 17 Writeup
This time we have the site as in [15](#15-writeup) but this time it doesnt return different outputs depending on the result of the SQLi. This now introduces us with a proplem: How do we still get the result of a query? The solution is time to be exact the time it took a query to run. We can use sleep() to manipulate the time it takes for a query that way we can use a slightly altered version of Injection we used in [15](#15-writeup). In the altered version there is `AND sleep(1)` added before the #. This makes it so that if a query results positive on the thing we tested it on it sleeps 1 second. This made it possible to write a very simple [script](17/main.py) making use of the longer response times.
-> xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

# 18 Writeup
This time there is a session cookie with an id between 1 and 640. As this is a small number I made a [script](18/main.py) that bruteforces every id and returns the right one. 
-> 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

# 19 Writeup
This time the IDs isn't sequential. I tried out some inputs and it returned something that looked like hex. I then converted the Hexadecimal to string and it returned <number>-<username>. So I made [this](19/main.py) script that bruteforces IDs and returns me the right one. 
-> eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

# 20 Writeup
This time there is a custom session handler that stores every session to a file. The important bit: 
```php
foreach($_SESSION as $key => $value) {
    debug("$key => $value");
    $data .= "$key $value\n";
}
file_put_contents($filename, $data);
``` 
This means if we can change one key-value-pair we could add a newline with a new key-value-pair. This would than look somthing like this: `name\nadmin 1`. This will get you admin. I then wrote a [script](20/main.py) to avoid encoding prolems. This script than makes a second request this time as a GET request with the previously created cookie.
-> IFekPyrQXftziDEsUr3x21sYuahypdgJ

# 21 Writeup
Now you are being presented with 2 websites. 1 normal login site which you can retrieve the password from and another one which enables you to store things in the session. I then looked at the source code and found the following 
```php
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
        $_SESSION[$key] = $val;
    }
```
I then changed the url in the browser to contain the following parameters: ?submit=smth&admin=1&debug.
The debug messages then showed that admin = 1 got stored. I then refreshed the other page and got back the password
-> chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ

# 22 Writeup
This time there is a blank page. The source code revels that the URL-parameter "revelio" shows the password. The code also refreshes the page if you're not admin. Using a proxy you can look at the requests and get the password
-> D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE

# 23 Writeup
In 23 your request has to contain a parameter passwd that contains iloveyou and is greater than 10. This works because of the peculiar way strings are compared to ints.
It will look at the first few chars and if they are integers it will take those as value. So passwd=11loveyou works
-> OsRmXFguozKpTZZ5X14zNO43379LZveg


# 24 Writeup
Now we have our password login again but this time you have to bypass strcmp. After a bit of research I found out that comparin a string to an empty array returns null.
So i put the following as passwd: passwd[]=""
-> GHF6X7YwACaYYssHVY05cFq83hRktl4c

# 25 Writeup
**TODO**
-> oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T

# 26
**TODO**
-> 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ

# 27
**TODO**
-> JWwR438wkgTsNKBbcJoowyysdM82YjeF