#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script to download GDELT data-sets and unzip them
"""

import os
import urllib
import datetime
import zipfile

if not os.path.exists("./data/"):
    os.makedirs("./data/")

datafile = urllib.URLopener()

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
sufX = [".export.CSV.zip", ".gkg.csv.zip", ".gkgcounts.csv.zip"]
filenames = [yesterday.strftime("%Y%m%d" + i) for i in sufX]
datafile.retrieve("http://data.gdeltproject.org/events/" + filenames[0], filenames[0])
datafile.retrieve("http://data.gdeltproject.org/gkg/" + filenames[1], filenames[1])
datafile.retrieve("http://data.gdeltproject.org/gkg/" + filenames[2], filenames[2])

for myfile in filenames:
    with zipfile.ZipFile(myfile, "r") as z:
        z.extractall("./data/")
    os.remove(myfile)
