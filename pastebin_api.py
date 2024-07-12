import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'wdAWdgD-kKmNA9subEVzaq_mzpbwtl7F'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin"""
    
    params = {
        'api_dev_key': API_DEV_KEY,
        'api_option': "paste",
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,  # Corrected parameter name
        'api_paste_private': 0 if listed else 1,
    }
    
    print("Creating new paste...")
    resp = requests.post(PASTEBIN_API_POST_URL, data=params)  # Use data=params for POST request
    
    if resp.status_code == 200:  # Corrected equality operator
        print("Success")
        return resp.text
    else:
        print('Failure :(')
        print(f"{resp.status_code} {resp.reason} {resp.text}")
        return
    