
import meraki
API_key='6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

dashboard= meraki.DashboardAPI(API_key)

response= dashboard.organizations.getOrganizations()


print(response)


organization_id = '681155'


import requests
import json
import csv

print('appliance')

url = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=appliance"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)
print(response.text.encode('utf8'))
print(response.raise_for_status())


with open('names.csv', 'a+', newline='') as csvfile:

    fieldnames = ['TIPO','MODELO_EQUIPO','NOMBRE','DIRECCION_MAC','DIRECCION_IP_PUBLICA','SERIAL','STADTUS']


    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({'TIPO':'wired','MODELO_EQUIPO':'MX65','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b0:c2:dc','DIRECCION_IP_PUBLICA':'192.168.128.4','SERIAL':'2QN-Q6EY-NP7J','STADTUS':'2021-11-19T08:18:53Z'})
   
    writer.writerow({'TIPO':'wired','MODELO_EQUIPO':'MX65','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b0:c3:44','DIRECCION_IP_PUBLICA':'192.168.128.5','SERIAL':'Q2QN-UTMQ-ZJQA','STADTUS':'2021-11-25T17:02:38Z'})
    
    writer.writerow({'TIPO':'wired','MODELO_EQUIPO':'MX65','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b0:c4:55','DIRECCION_IP_PUBLICA':'null','SERIAL':'Q2QN-Y5ED-P57W','STADTUS':'2017-11-01T17:07:32Z'})
  
    writer.writerow({'TIPO':'wired','MODELO_EQUIPO':'MX65','NOMBRE':'','DIRECCION_MAC':'ac:17:c8:24:4f:68','DIRECCION_IP_PUBLICA':'192.168.1.74','SERIAL':'Q2SW-SWQ2-HZ9L','STADTUS':'2021-11-12T22:57:10Z'})




print('wireless')
url = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=wireless"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)
print(response.text.encode('utf8'))
print(response.raise_for_status())

with open('names.csv', 'a+', newline='') as csvfile:
   fieldnames = ['TIPO','MODELO_EQUIPO','NOMBRE','DIRECCION_MAC','DIRECCION_LAN','SERIAL','STADTUS']


   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   writer.writeheader()

   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR84','NOMBRE':'Alex\'s MR84 - 1','DIRECCION_MAC':'e0:55:3d:10:56:8a','DIRECCION_LAN':'null','SERIAL':'Q2EK-2LYB-PCZP','STADTUS':'2018-02-03T11:02:37Z'})
   
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR84','NOMBRE':'Vegas Living Room MR84','DIRECCION_MAC':'e0:55:3d:10:5a:ca','DIRECCION_LAN':'192.168.0.20','SERIAL':'Q2EK-3UBE-RRUY','STADTUS':'018-09-29T12:23:21Z'})
   
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR84','NOMBRE':'','DIRECCION_MAC':'e0:55:3d:10:5b:d8','DIRECCION_LAN':'null','SERIAL':'Q2EK-ACGE-URXL','STADTUS':'2017-11-01T17:07:32Z'})
		
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR84','NOMBRE':'Vegas Balcony MR84','DIRECCION_MAC':'ee0:55:3d:10:5c:48','DIRECCION_LAN':'null','SERIAL':'Q2EK-D4XP-235S','STADTUS':'2018-09-28T09:19:44Z'})
	
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR84','NOMBRE':'Sun Room','DIRECCION_MAC':'e0:55:3d:10:5e:b2','DIRECCION_LAN':'192.168.128.99','SERIAL':'Q2EK-UKGM-XSD9','STADTUS':'2021-12-16T20:09:01Z'})
      
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR32','NOMBRE':'Alex\xe2\x80\x99s MR32','DIRECCION_MAC':'e0:55:3d:b8:3e:70','DIRECCION_LAN':'192.168.1.16','SERIAL':'Q2JD-7RNY-EB7Z','STADTUS':'2021-07-07T20:22:45Z'})
 
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR42','NOMBRE':'','DIRECCION_MAC':'e0:cb:bc:8c:1f:fe','DIRECCION_LAN':'192.168.0.2','SERIAL':'Q2KD-KWMU-7U92','STADTUS':'2021-12-16T19:07:49Z'})
  
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'Basement AP','DIRECCION_MAC':'e0:55:3d:c0:73:56','DIRECCION_LAN':'192.168.128.17','SERIAL':'Q2EK-3UBE-RRUY','STADTUS':'018-09-29T12:23:21Z'})
   
   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'2nd Floor AP','DIRECCION_MAC':'e0:55:3d:c0:5e:2e','DIRECCION_LAN':'92.168.128.15','SERIAL':'Q2LD-AN9B-S6AJ','STADTUS':'2021-06-03T20:05:20Z'})

   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b2:2f:2c','DIRECCION_LAN':'192.168.128.4','SERIAL':'Q2LD-D932-NRPU','STADTUS':'2021-12-16T15:13:59Z'})

   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b2:77:f8','DIRECCION_LAN':'1192.168.128.7','SERIAL':'Q2LD-3Y7V-7Y2X','STADTUS':'021-12-10T21:30:13Z'})

   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'V1st Floor AP','DIRECCION_MAC':'e0:55:3d:c0:76:f4','DIRECCION_LAN':'192.168.128.202','SERIAL':'Q2LD-GYL3-KEHX','STADTUS':'2021-12-06T07:03:38Z'})

   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b2:8a:5a','DIRECCION_LAN':'24.144.215.84','SERIAL':'Q2LD-N2U5-D83H','STADTUS':'2018-10-25T14:41:08Z'})


   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'','DIRECCION_MAC':'0c:8d:db:b2:8c:f0','DIRECCION_LAN':'null','SERIAL':'Q2LD-X2S2-AG2U','STADTUS':'2018-10-10T01:09:22Z'})


   writer.writerow({'TIPO':'wireless','MODELO_EQUIPO':'MR52','NOMBRE':'Office AP','DIRECCION_MAC':'e0:55:3d:c0:72:d8','DIRECCION_LAN':'192.168.128.16','SERIAL':'Q2LD-ZWCZ-UA77','STADTUS':'021-12-02T22:10:43Z'})




































	
