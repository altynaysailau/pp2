
import json


 
with open('/Users/altynaysailau/Desktop/Github/pp2/lab04/json/sample-data.json', 'r') as my_file:
    data = json.load(my_file) 
print('Interface Status')
print('=' * 78)

DN = "DN"
Description = 'Description'
Speed = 'Speed'
MTU = 'MTU'

print(f"{DN:<50} {Description:<20}  {Speed:<8} {MTU:<5}") 
print('-' * 50 + " " + '-' * 20 + "  " +  '-' * 6 + "  " +  '-' * 6)


for item in data['imdata']: 
    attributes = item['l1PhysIf']['attributes'] 
   
    dn = attributes.get('dn') 
    description = attributes.get('descr', '') 
    speed = attributes.get('speed', 'inherit') 
    mtu = attributes.get('mtu', '')  
    print(f"{dn:<50} {description:<20} {speed:<9} {mtu:<5}")
