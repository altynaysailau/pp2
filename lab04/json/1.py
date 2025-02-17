
import json 


print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open('/Users/altynajsajlau/Documents/GitHub/pp2/lab04/json/sample-data.json') as f:
    data = json.load(f)

request_from_server = data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
speed = data["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]
mtu = data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )
