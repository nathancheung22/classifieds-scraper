# you will need to do the following to properly run these scripts:
# pip install bs4
# pip install requests
# pip install pytz
# pip install smtplib
# pip install pandas


from os.path import abspath, dirname
from os import makedirs
import pandas as pd


# DO NOT EDIT
location = abspath(__file__)
root_directory = dirname(location)
pd.set_option("display.max_colwidth", 10000)
kijiji = "http://kijiji.ca"
fieldnames = ["Listing Name", "Price", "Link"]
# DO NOT EDIT


# config file for your sending and receiving email
# sending email must be a gmail account, configure on the link below
# EDIT THE STUFF BELOW

email_address = "your email"  # myaccount.google.com/lesssecureapps
password = "your password"
recipient = "recipient email"
email_protocol = "smtp.gmail.com:587"  # change based on email service

# csv save file directory
slash = "\\"  # windows users put "\\", ubuntu users put "/"
directory = root_directory + slash + "pkl" + slash  # edit the part in quotes

# kijiji area for search, change depending on search area
# https://www.kijiji.ca/b-city-of-toronto/ipad-6th-generation/k0l1700273?dc=true
link_part_1 = "/b-city-of-toronto/"
link_part_2 = "/k0l1700273"

# timezone for emails, reference pytz for syntax
my_timezone = "US/Eastern"


# DO NOT EDIT
temp_dir = directory + "temp" + slash

try:  # makes the proper save locations
    makedirs(directory)
    makedirs(temp_dir)
except FileExistsError:
    pass
