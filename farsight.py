import yaml
import os
import requests
import json
import datetime


path = os.environ["WORKDIR"]

with open(path+"/lookup_plugins/farsight/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    headers = {
    'Accept': 'application/json',
    'X-API-Key':cfg['lookup_plugin']['FS_API_KEY']
     }



def get_url_report(inward_array,var_array):
    lst=[]
    for i in inward_array:
        if var_array[0] in i:
            url='https://api.dnsdb.info/lookup/rrset/name/'
            tmp_dict={}
            try:
                response = requests.get(url=url+str(i[var_array[0]]) , headers=headers)
            except Exception as e:
                print("API Error : %s", e)
            for line in response.iter_lines():
                 try:
                    json_store=json.loads(line)
                    tmp_dict.update(i)
                    try:
                        tmp_dict['$FSCount']=json_store['count']
                    except:
                        pass
                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSFirstseen']=time_store
                    except:
                        pass
                    try:
                        time_store_last = datetime.datetime.utcfromtimestamp(json_store['time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSLastseen']=time_store_last
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRname']=json_store['rrname']
                    except:
                        pass
                    try:
                        tmp_dict['$FSBailiwick']=json_store['bailiwick']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRdata']=json_store['rdata']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRtype']=json_store['rrtype']
                    except:
                        pass
                 except:
                     pass
                 if tmp_dict:
                     lst.append(tmp_dict)
                 else:
                     lst.append(i)
            tmp_dict={}
    return lst



def get_ipv4_report(inward_array,var_array):
    lst=[]
    for i in inward_array:
        if var_array[0] in i:
            url = 'https://api.dnsdb.info/lookup/rdata/ip/'
            tmp_dict = {}
            try:
                response = requests.get(url=url + str(i[var_array[0]]), headers=headers)
            except Exception as e:
                print("API Error : %s", e)
            for line in response.iter_lines():
                try:
                    json_store = json.loads(line)
                    tmp_dict.update(i)
                    try:
                        tmp_dict['$FSCount'] = json_store['count']
                    except:
                        pass
                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['zone_time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSZonefirstseen'] = time_store
                    except:
                        pass
                    try:
                        time_store_last= datetime.datetime.utcfromtimestamp(json_store['zone_time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSZonelastseen'] = time_store_last
                    except:
                        pass

                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSFirstseen'] = time_store
                    except:
                        pass
                    try:
                        time_store_last = datetime.datetime.utcfromtimestamp(json_store['time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSLastseen'] = time_store_last
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRname'] = json_store['rrname']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRdata'] = json_store['rrdata']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRtype'] = json_store['rrtype']
                    except:
                        pass
                except:
                    pass
                if tmp_dict:
                    lst.append(tmp_dict)
                else:
                    lst.append(i)
            tmp_dict = {}
    return lst


def get_ipv6_report(inward_array, var_array):
    lst=[]
    for i in inward_array:
        if var_array[0] in i:
            url='https://api.dnsdb.info/lookup/rdata/ip/'
            tmp_dict={}
            try:
                response = requests.get(url=url + str(i[var_array[0]]), headers=headers)
            except Exception as e:
                print("API Error : %s", e)
            for line in response.iter_lines():
                try:
                    json_store = json.loads(line)
                    tmp_dict.update(i)
                    try:
                        tmp_dict['$FSCount'] = json_store['count']
                    except:
                        pass
                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSFirstseen'] = time_store
                    except:
                        pass
                    try:
                        time_store_last = datetime.datetime.utcfromtimestamp(json_store['time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSLastseen'] = time_store_last
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRname'] = json_store['rrname']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRdata'] = json_store['rdata']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRtype'] = json_store['rrtype']
                    except:
                        pass
                except:
                    pass
                if tmp_dict:
                    lst.append(tmp_dict)
                else:
                    lst.append(i)
            tmp_dict = {}
    return lst


def get_nameserver_report(inward_array,var_array):
    lst=[]
    for i in inward_array:
        if var_array[0] in i:
            url='https://api.dnsdb.info/lookup/rdata/name/'
            tmp_dict={}
            try:
                response = requests.get(url=url+str(i[var_array[0]]), headers=headers)
            except Exception as e:
                print("API Error : %s", e)
            for line in response.iter_lines():
                try:
                    json_store = json.loads(line)
                    tmp_dict.update(i)
                    try:
                        tmp_dict['$FSCount'] = json_store['count']
                    except:
                        pass
                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['zone_time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSZonefirstseen'] = time_store
                    except:
                        pass
                    try:
                        time_store_last= datetime.datetime.utcfromtimestamp(json_store['zone_time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSZonelastseen'] = time_store_last
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRname'] = json_store['rrname']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRtype'] = json_store['rrtpe']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRdata'] = json_store['rdata']
                    except:
                        pass
                except:
                    pass
                if tmp_dict:
                    lst.append(tmp_dict)
                else:
                    lst.append(i)
            tmp_dict={}
    return lst


def get_mailexchange_report(inward_array,var_array):
    lst=[]
    for i in inward_array:
        if var_array[0] in i:
            url='https://api.dnsdb.info/lookup/rdata/name/'
            tmp_dict={}
            try:
                response = requests.get(url=url+str(i[var_array[0]]), headers=headers)
            except Exception as e:
                print("API Error : %s", e)
            for line in response.iter_lines():
                try:
                    json_store = json.loads(line)
                    tmp_dict.update(i)
                    try:
                       tmp_dict['$FSCount'] = json_store['count']
                    except:
                        pass
                    try:
                        time_store = datetime.datetime.utcfromtimestamp(json_store['time_first']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSFirstseen'] = time_store
                    except:
                        pass
                    try:
                        time_store_last = datetime.datetime.utcfromtimestamp(json_store['time_last']).strftime('%Y-%m-%d %H:%M:%S')
                        tmp_dict['$FSLastseen'] = time_store_last
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRname'] = json_store['rrname']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRdata']=json_store['rdata']
                    except:
                        pass
                    try:
                        tmp_dict['$FSRRtype']=json_store['rrtpe']
                    except:
                        pass
                except:
                    pass
                if tmp_dict:
                    lst.append(tmp_dict)
                else:
                    lst.append(i)
            tmp_dict={}
    return lst
