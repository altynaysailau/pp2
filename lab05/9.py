
import re

with open("/Users/altynajsajlau/Documents/GitHub/pp2/lab05/row2.txt") as file:
    data = file.read()

print(re.sub(r"([A-Z])", r" \1", data))
