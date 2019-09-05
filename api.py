import os
from sodapy import Socrata
from ago import time_ago


client = Socrata("data.cityofnewyork.us", os.environ['sodapy_key'])

results = client.get("43nn-pn8j", limit=50, dba="BE JUICE", order='inspection_date')

my_dict = {}
my_list = []
for i in results:
    try:
        my_dict["d"+i['inspection_date']]['score'] = i['score']
        my_dict["d"+i['inspection_date']]['grade'] = i['grade']
    except:
        pass  


    if "d"+i['inspection_date'] not in my_dict:
        my_dict["d"+i['inspection_date']] = {"date" : i['inspection_date']}
        my_dict["d"+i['inspection_date']]['time_ago'] = time_ago(i['inspection_date'])
        my_dict["d"+i['inspection_date']]['id'] = i['camis']
        my_dict["d"+i['inspection_date']]['phone'] = i['phone']
        my_dict["d"+i['inspection_date']]['name'] = i['dba']
        my_dict["d"+i['inspection_date']]['addr'] = i['building'] + i['street'] + ", " + i['boro'] + " " + i['zipcode'] 
        my_dict["d"+i['inspection_date']]['phone'] = i['phone']
        my_dict["d"+i['inspection_date']]['cuisine_description'] = i['cuisine_description']
        my_dict["d"+i['inspection_date']]['critical_flag'] = []
        my_dict["d"+i['inspection_date']]['critical_flag'].append(i['critical_flag'])
        my_dict["d"+i['inspection_date']]['v_code'] = []
        my_dict["d"+i['inspection_date']]['v_code'].append(i['violation_code'])
        my_dict["d"+i['inspection_date']]['v_description'] = []  
        my_dict["d"+i['inspection_date']]['v_description'].append(i['violation_description'])
        my_dict["d"+i['inspection_date']]['inspection_type'] = i['inspection_type']
    else:
        my_dict["d"+i['inspection_date']]['v_code'].append(i['violation_code'])    
        my_dict["d"+i['inspection_date']]['v_description'].append(i['violation_description'])
        my_dict["d"+i['inspection_date']]['critical_flag'].append(i['critical_flag'])


for i in my_dict.values():
    my_list.append(i)

my_list.reverse()
