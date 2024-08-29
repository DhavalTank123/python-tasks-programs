import json
import requests
import httplib2


API_KEY = 'your_phishtank_api_key'


def is_phishing_url_requests(url):
    api_url = 'https://checkurl.phishtank.com/checkurl/'
    payload = {'url': url, 'format': 'json', 'apikey': API_KEY}
    
    try:
        response = requests.post(api_url, data=payload)
        response.raise_for_status()
        result = response.json()
   
        if result.get('phish') == 1:  
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error using requests: {e}")
        return None


def is_phishing_url_httplib2(url):
    api_url = 'https://checkurl.phishtank.com/checkurl/'
    payload = {'url': url, 'format': 'json', 'apikey': API_KEY}
    
    http = httplib2.Http()
    
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = json.dumps(payload)
        response, content = http.request(api_url, 'POST', body=body, headers=headers)
        result = json.loads(content)
        
       
        if result.get('phish') == 1:  # PhishTank returns 1 for phishing
            return True
        else:
            return False
    except Exception as e:
        print(f"Error using httplib2: {e}")
        return None

def main():
    url_to_check = 'http://www.travelswitchfly.com/'  


    print("Checking using requests...")
    is_phishing_requests = is_phishing_url_requests(url_to_check)
    if is_phishing_requests is True:
        print(f"The URL {url_to_check} is a phishing site (requests).")
    elif is_phishing_requests is False:
        print(f"The URL {url_to_check} is not a phishing site (requests).")
    else:
        print("Failed to check URL (requests).")

 
    print("\nChecking using httplib2...")
    is_phishing_httplib2 = is_phishing_url_httplib2(url_to_check)
    if is_phishing_httplib2 is True:
        print(f"The URL {url_to_check} is a phishing site (httplib2).")
    elif is_phishing_httplib2 is False:
        print(f"The URL {url_to_check} is not a phishing site (httplib2).")
    else:
        print("Failed to check URL (httplib2).")

if __name__ == "__main__":
    main()
