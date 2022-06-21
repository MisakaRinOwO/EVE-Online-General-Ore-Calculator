import json, requests

def get_item_id(item:str):
    url = f'http://www.fuzzwork.co.uk/api/typeid.php?typename={item}'
    try:
        response = requests.get(url)
        r_obj = response.json()
    except:
        print('Please check yor network settings')
    finally:
        if response != None:
            response.close()
        if type(r_obj) == dict:
            return r_obj
        
def get_item_price(item:str,location:int = 30000142):
    pass