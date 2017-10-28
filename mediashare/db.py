# # Full path and name to your csv file
# csv_filepathname="/home/megaaccount004/Movies.csv"
# Full path to your django project directory
your_djangoproject_home="/home/megaaccount004/mediashare/mediashare/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from megalinks.models import Link

# import csv
# f=open('/home/megaaccount004/Movies.csv', encoding='utf-8', errors='ignore')
# dataReader = csv.reader(f, delimiter=',', quotechar='"')


# for row in dataReader:
#     torrent = Torrent()
#     torrent.hash = row[0]
#     torrent.title = row[1]
#     torrent.category = row[2]
#     torrent.id = row[3]
#     torrent.save()

f = open("links.txt", "a+")

for i in Link.objects.all():
    f.write(str(i.id) + "|" + i.link + "\n")
