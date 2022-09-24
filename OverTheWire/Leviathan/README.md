# Leviathan

# 0
First I checked the ressources available and came across a suspicious lookin html file .backup/bookmarks.html. I then used `grep "leviathan" .backup/bookmarks.html`.
Which returned the following: 
```html
<DT>
  <A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```
-> rioGegei8m

# 1
There is an executable called `check` in the homedir. Upon executing `file` it returns that the binary is a setuid. I then used ltrace to trace libcalls and voila there it was a strcmp with the word "sex". So I tried that as password and it worked. I then used the shell to get the password.
-> ougahZi8Ta 