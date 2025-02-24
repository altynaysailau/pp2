
import re 

with open("/Users/altynajsajlau/Documents/GitHub/pp2/lab05/row.txt", encoding="utf-8") as file:
    data = file.read()

m = re.findall(r"a+.b", data)
print(m)
