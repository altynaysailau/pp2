
import re 

with open("/Users/altynajsajlau/Documents/GitHub/pp2/lab05/row.txt", encoding="utf-8") as file:
    data = file.read()
m = re.findall(r"[A-Z][a-z]+", data)

print(m)
