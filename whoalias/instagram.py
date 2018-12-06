import os
import re
import shutil
import json

import requests




async def scrape(all_aliases):
    print(" [*] Searching Instagram footprint ..")

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f'https://instagram.com/{alias}/'

        response = requests.get(URL)

        if response.status_code == 404:
            print(f" [*] https://instagram.com/{alias}/ returned nothing ..")

        elif response.status_code == 200:
            print(f" [!] https://instagram.com/{alias}/ HIT! Logging to output ..\n")

            # Get Instagram JSON from HTML because their frontend disallows traditional scraping
            json_match = re.search(r'window\._sharedData = (.*);</script>', response.text)

            profile_json = json.loads(json_match.group(1))['entry_data']['ProfilePage'][0]['graphql']['user']

            # Followage and Bio
            print(f" [+] {alias} alledged real name: {profile_json['full_name']} ..")
            print(f" [+] {alias} has {profile_json['edge_owner_to_timeline_media']['count']} instagram posts ..")
            print(f" [+] {alias} follows {profile_json['edge_follow']['count']} users and has {profile_json['edge_followed_by']['count']} instagram followers ..")
            print(f" [+] {profile_json['biography']}\n")

            # Begin saving instagram photoa
            print(f" [*] Saving instagram library of {alias} to /output/{alias}")
            count = 0
            for image_link in profile_json['edge_owner_to_timeline_media']['edges']:
                count += 1
                # Try to download, ignore if error is thrown
                try:
                    # Get image with http request
                    image = requests.get(image_link['node']['display_url'], stream=True)
                    image.raw.decode_content = True

                    # Set output format
                    image_path = f"output/{alias}/{str(count)}.jpg"

                    print(f" [+] Downloading photo: {image_path} ..")
                    # Make dirs if needed
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)

                    # Open and write
                    with open(image_path, 'wb') as out_file:
                        shutil.copyfileobj(image.raw, out_file)
                    del image

                except Exception as e:
                    print(" [!] Ignoring error: "+str(e)+"")
                    pass
