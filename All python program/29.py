import requests
import csv
import json
import os

CSV_URL = 'https://rules.emergingthreats.net/blockrules/compromised-ips.csv' #here this url have no data so its gives 404 eror 

OUTPUT_DIR = 'compromised_ips_feeds'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def fetch_csv_data(url):
    """Fetch CSV data from a URL and return it as a list of rows."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.content.decode('utf-8')
        reader = csv.reader(content.splitlines())
        return list(reader)
    except requests.RequestException as e:
        print(f"Error fetching CSV data: {e}")
        return []

def save_json_file(filename, data):
    """Save data to a JSON file with the given filename."""
    file_path = os.path.join(OUTPUT_DIR, filename + '.json')
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    rows = fetch_csv_data(CSV_URL)
    
    if not rows:
        print("No data fetched. Exiting.")
        return
    
    headers = rows[0]
    

    for row in rows[1:]:

        feed_data = dict(zip(headers, row))
        
        filename = feed_data.get('IP Address', 'unknown_feed')  # Adjust if necessary
        

        save_json_file(filename, feed_data)
    
    print("JSON files have been created.")

if __name__ == "__main__":
    main()
