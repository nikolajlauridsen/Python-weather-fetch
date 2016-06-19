import requests
import bs4
import os
import datetime
import sys


def get_soup():
    url = 'http://www.dmi.dk/vejr/til-lands/byvejr/by/vis/DK/7000/' \
          'Fredericia,%20Danmark'

    # Download page
    res = requests.get(url)
    res.raise_for_status()

    # Create soup
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Return soup
    return soup


def get_image(css_selector, path_modifier):
    """Downloads the weather forecast as an image from DMI.dk"""
    os.makedirs('images', exist_ok=True)

    soup = get_soup()

    # Find the url to the weather image
    weather_img = soup.select(css_selector)

    if not weather_img:
        print("Kunne desværre ikke finde vejrudsigten.")
    else:
        img_url = weather_img[0].get('src')

        # Download image
        res = requests.get(img_url)
        res.raise_for_status()

        # Save image
        file_name = str(datetime.date.today()) + path_modifier + ".png"
        path = os.path.join('images', file_name)
        image_file = open(path, 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        return path


def get_warning():
    # Get soup object
    soup = get_soup()
    # Select warning text
    warning_status = soup.select('.warning-content a')
    # Return it
    return warning_status[0].text


def bindings(root):
    """Sets exit key bindings"""
    root.bind('<Escape>', sys.exit)
    root.bind('<Return>', sys.exit)
