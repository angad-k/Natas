# Natas

0)Password was stored as a comment in a div with id "content". Basic inspect element solved this.<br>
  Password : gtVrDuiDfck831PqWsLEZy5gyDz1clto<br><br>
1)Well, right-clicking was blocked but ctrl+shift+i will always bring up the developer tools<br>
	Password : ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi<br><br>
2)Fist idea was to perform a string on files/pixel.png. That didn't yield anything. 
  Trying to access the files folder showed that it had a file named users which had the password.<br>
	Password : sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14<br><br>
3)Comment mentioned google. Having done picoCTF. 
  Mention of a search engine made me try robots.txt which yielded disallow s3cr3t . 
  Inside it, was users.txt with the password.<br>
	Password : Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ<br><br>
4)The referer in the request header is the site from where we came. 
  I used a chrome plugin to send a request with a custom header<br>
	Password : iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq<br><br>
5)Lolwa. Had the cookie plugin already installed. Set the loggedin parameter to 1.<br>
	Password : aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1<br><br>
6)Maro muze maro. Spent a lot of time on this thinking kya karu idhar. 
  The source code showed an includes/secret.inc I had thought of putting it in the URL but the same thing was done in 2) 
  So, was thinking of something else. Finally, did it and there was the password.<br>
	Password : 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9<br><br>
7)Who's the effin' OG? I'm the effin' OG!!! URL was showing a get request. 
  A comment described that the password is stored at a certain place. 
  Put the same place in the GET request through the URL.<br>
	Password : DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe<br><br>
8)PHP code showed how the string was encoded. Reversed the encoding using python.<br>
	Password : W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl<br><br>
9)Passthru function allows code to be run on terminal. So, a; cat /etc/natas_webpass/natas10 did the magic.<br>
	Password : nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu<br><br>
10)Couln't use ';'. Had to think about it. Slept on it, literally. Woke up in the evening and did this. 
  Passed 'a /etc/natas_webpass/natas11' as the parameter. Didn't do the trick.
  Tried for 'b', no use. 'd' made the cut and gave the answer<br>
	Password : U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK<br><br>
11)Wrote index.php. Commented out code is for getting the key. Next code is for getting the cookie.<br>
	Password : EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3<br><br>
12)Okay, I first did this complicated thing of making an index.php.
  JPEG file and so on, which was not needed at all. Here is what I had to do. 
    Make a natas12.php file which runs cat on the natas13 file remotely on the server. 
    For some reason, the site trusts that the people will only upload JPEGs but allows uploading other type of files. 
    So, I uploaded the natas12 file, and through the developer tools in chrome, 
    changed a form attribute which stored <randomvalue>.jpg to <randomvalue>.php and it worked.<br>
	Password : jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY<br><br>
13)This one was easy as it mostly added a little bit more constraints to the previous one. 
A quick google search on how to bypass the exif function in php told me that I have to just have the magic no. s of a jpg at the start of the file. 
I tried manually putting the no.s at the start of the file with vscode but that didn't work. 
So, I copied this python function I found online which also does the same thing and writes to the file the magic no. followed by the php code. 
bypass_exif.py is included in the repository.  
The password obtained also had four unprintable characters as shown in the attached screenshot. 
Guess what they were? Well, I'll tell the answer myself like Dora the explorer, they were the four magic no.s that we had put at the start of the file. <br>
	Password : Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1<br><br>
14)I completed this one pretty quickly as I already had a little bit idea of sql injection. I put     " or ""="     in both fields to get the password.
	<br>Password : AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J<br><br>
15)Isme voh hecker vala feel aya na! So, I used the LIKE operator in sql to build the password character by character using python and the rquests library in python. n15.py has the code for the same.
	<br>Password : WaIHEacj63wnNIBROHeqi3p9t0m5nhmh<br>
16)This took a lot of time. Not to code but to think what to do. Code toh mostly pichla hi copy kiya. So, turns out, you can run a bash command within a bash command. So, mei sasta Nolan ban gaya aur chala BASH command ke andar command aur build kiya password character by character.
	<br>Password : 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw<br><br>
17)sleep(10) added to 15's code did the trick here. Had to use sleep(10) because smaller no.s would let in random characters and the code would get stuck in an infinite loop.
	<br>Password : xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP <br><br>
18)Systematically going through the source code tells us all this. Session ids range from 1 to 640 and are store in a cookie called PHPSESSID. If we have the session id corresponding to the admin's session, Yeah!!! So, we try for all the session ids through python. id 119 makes the cut.
	<br>Password : 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs<br><br>
19)The Session id cookie in this one looked like a hex decoded something. Logged in with username admin and hex decoded the session id to 630-admin. I tried for the most obvious options then. ie - 1-admin and 0-admin. None of them worked. So, coded a program and brute forced the no.
<br>Password : eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF<br><br>
20)I got done with this one much quicker than I expected. So, looking through the code, what I understood was that they were storing the session variables in a very easy way . "key" "value" on each line for each session variable. So, if my name variable is admin /n admin 1, well you get it.
	<br>Password : IFekPyrQXftziDEsUr3x21sYuahypdgJ<br><br>
21)Okay, this one was something I myself experienced while doing the backend assignment. Setting up a session variable for username on the client side would set the same for the admin side. On these same ideas, setting admin = 1 through the experimenter site and copying the session id onto the main site did the trick.
	<br>Password : chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ<br><br>
