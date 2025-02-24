import re



with open("/Users/altynajsajlau/Documents/GitHub/pp2/lab05/row.txt") as file:
    data = file.read()
m = re.findall("a.*b", data)
print(m)
