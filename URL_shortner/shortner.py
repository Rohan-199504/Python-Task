import pyshorteners as ps

link = 'https://netzwerkacademy.com/python-development-course/'

shortener = ps.Shortener()

x = shortener.tinyurl.short(link)

print(x)
