"""
     Utisl for the json file
"""

import json


def josn_to_dict(json_file:str) -> list:
    """
    josn_to_dict is used to scan a json file and return the dict
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        if "subscriptions" not in json_data.keys():
            print("json not in new pipe format.")
            return None
        return json_data["subscriptions"]

if __name__ == '__main__':
    subs_list = josn_to_dict("subs.json")
    for subs in subs_list:
        print(subs["name"], subs["url"], sep=" :")
