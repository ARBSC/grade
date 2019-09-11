import os
from sodapy import Socrata
from ago import time_ago

def get_json_data(search):
    client = Socrata("data.cityofnewyork.us", os.environ['sodapy_key'])

    results = client.get("43nn-pn8j", limit = 200, dba = search, order = 'inspection_date')
    if results:
        results = fix_data(results)
        return results
    return None


def fix_data(data):
    my_dict = {}
    my_list = []

    for i in data:
        try:
            my_dict["d"+i['inspection_date']]['score'] = i['score']
            my_dict["d"+i['inspection_date']]['grade'] = i['grade']
        except:
            pass  

        if "d"+i['inspection_date'] not in my_dict:
            my_dict["d"+i['inspection_date']] = {"date" : i['inspection_date']}
            my_dict["d"+i['inspection_date']]['time_ago'] = time_ago(i['inspection_date'])
            my_dict["d"+i['inspection_date']]['id'] = i.get('camis', None)
            my_dict["d"+i['inspection_date']]['phone'] = i.get('phone', None)
            my_dict["d"+i['inspection_date']]['name'] = i.get('dba', None)
            my_dict["d"+i['inspection_date']]['addr'] = i.get('building', None) + " " + i.get('street', None) + ", " + i.get('boro', None) + " " + i.get('zipcode', '') 
            my_dict["d"+i['inspection_date']]['phone'] = i.get('phone', None)
            my_dict["d"+i['inspection_date']]['cuisine_description'] = i.get('cuisine_description', None)
            my_dict["d"+i['inspection_date']]['critical_flag'] = []
            my_dict["d"+i['inspection_date']]['critical_flag'].append(i.get('critical_flag', None))
            my_dict["d"+i['inspection_date']]['v_code'] = []
            my_dict["d"+i['inspection_date']]['v_code'].append(i.get('violation_code', None))
            my_dict["d"+i['inspection_date']]['v_description'] = []  
            my_dict["d"+i['inspection_date']]['v_description'].append(i.get('violation_description', None))
            my_dict["d"+i['inspection_date']]['inspection_type'] = i.get('inspection_type', None)
        else:
            my_dict["d"+i['inspection_date']]['v_code'].append(i.get('violation_code', None))
            my_dict["d"+i['inspection_date']]['v_description'].append(i.get('violation_description', None))
            my_dict["d"+i['inspection_date']]['critical_flag'].append(i.get('critical_flag', None))

    for i in my_dict.values():
        my_list.append(i)

    my_list.reverse()
    return my_list
