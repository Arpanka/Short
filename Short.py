
#!/data/data/com.termux/files/usr/bin/python3

#imprort module

import pyshorteners
#Take input from user

link = input("Enter a url: ")
short  = pyshorteners.Shortener()
gurl = short.tinyurl.short(link)
print("your short url is : ")
print(gurl)
