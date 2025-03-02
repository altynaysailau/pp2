
import os
import string

with open("/Users/altynajsajlau/Documents/GitHub/pp2/lab05/row.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()
