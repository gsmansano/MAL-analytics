import os
import requests
import pandas as pd
import time
import json
from datetime import datetime

# this function will clean a few attributes that come in array of objects
# creating a single string with just the name, example "Action, Adventure, etc"
def clean_nested_list(item_list):
    if not item_list:
        return None
    return ", ".join([item['name'] for item in item_list])

# function to fetch a batch of anime from page n
def fetch_anime(page):
    
    # jikan has a pagination of 25 items per page
    # we get the 25 top anime of page n
    api_url = f"https://api.jikan.moe/v4/top/anime?page={page}"
    response = requests.get(api_url)
    
    all_records = []
    
    if response.status_code == 200:
        data = response.json()['data']
        for item in data:
            
            display_title = next((t['title'] for t in item['titles'] if t['type'] == 'Default'), item.get('title'))

            record = {
                'mal_id': item.get('mal_id'),
                'title': display_title,
                'type': item.get('type'),
                'source': item.get('source'),
                'episodes': item.get('episodes'),
                'status': item.get('status'),
                'year': item.get('year'),
                'season': item.get('season'),
                'aired_from': item.get('aired', {}).get('from'), 
                'rating': item.get('rating'),
                'score': item.get('score'),
                'scored_by': item.get('scored_by'),
                'rank': item.get('rank'),
                'popularity': item.get('popularity'),
                'members': item.get('members'),
                'favorites': item.get('favorites'),
                'synopsis': item.get('synopsis'),
                'image_url': item.get('images', {}).get('jpg', {}).get('image_url'),
                'studios': clean_nested_list(item.get('studios')),
                'genres': clean_nested_list(item.get('genres')),
                'themes': clean_nested_list(item.get('themes')),
                'demographics': clean_nested_list(item.get('demographics')),
            }

            all_records.append(record)
                   
    else:
        print(f"Error on page {page}: {response.status_code}")
        return None
        
    # we return the 25 animes from this page
    return all_records

# fuction to load the data fetched from page n        
def load_anime(data, date, page):

    # check if directory exists
    os.makedirs(f"data/raw/{date}", exist_ok=True)
    
    filename = f"data/raw/{date}/top_anime_page{page}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        
        # we dump the 25 items from the page into a file
        # this is so we have a local physical version of the data
        # before we hit up the db
        json.dump(data, f, ensure_ascii=False, indent=4)

def fetch_load_loop():
    
    # total pages is the number that defines the data scope
    # every page gets 25 records.
    total_pages = 100
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # create the directory for the current date    
    os.makedirs(f"data/raw/{current_date}", exist_ok=True)
    
    for page in range(1, total_pages + 1): # +1 to fix the range
        
        # a check if the file already exists. if so, skips
        # this ensures if the script fails at any point and is rerun
        # it does not start from scratch duplicating files
        filename = f"data/raw/{current_date}/top_anime_page{page}.json"
        if os.path.exists(filename):
            print(f"Page {page} already exists, skipping...")
            continue
        
        current_record = []
        
        print(f"Fetching page {page}...")
        # we use the fetch function to add the first page.
        current_record = fetch_anime(page)
        
        if current_record: # Only save if we actually got data
            print(f"Page {page} fetched, loading files...")
            # then we load this into the local files
            load_anime(current_record, current_date, page)
        
            print(f"Page {page} loaded, moving to next page...")
            time.sleep(1.5) # add a sleep function to not hit jikan rate limit
        
        else:
            print(f"There was a issue fetching the data, please review the script.")
            break

if __name__ == "__main__":
    fetch_load_loop()
