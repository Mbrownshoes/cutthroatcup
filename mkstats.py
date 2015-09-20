# import csv

# with open('player.csv', 'rb') as csvfile:
#     dat = csv.reader(csvfile)
#     for row in dat:
#         print row

# import csv
# import json

# csvfile = open('player.csv', 'r')
# jsonfile = open('player.json', 'w')

# fieldnames = ("First Name","Last Name","End Team","Teams","OGP","Pos","GP","G","A","A1","PTS","+/-","Sh","Misses","Blocked","SHG","SHA","SHP","HitF","BkS","SOG","PPP","GWG")
# reader = csv.DictReader( csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write(',')


import csv
import sys
import json

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
fieldnames = ["First Name","Last Name","End Team","Teams","OGP","Pos","GP","G","A","A1","PTS","plsmin","Sh","Misses","Blocked","SHG","SHA","SHP","HitF","BkS","SOG","PPP","GWG",'Total']
def convert(filename):
 csv_filename = filename[0]
 print "Opening CSV file: ",csv_filename 
 f=open(csv_filename, 'r')
 csv_reader = csv.DictReader(f,fieldnames)
 json_filename = csv_filename.split(".")[0]+".json"
 print "Saving JSON to file: ",json_filename
 jsonf = open(json_filename,'w') 



 data = json.dumps([r for r in csv_reader])
 jsonf.write(data) 
 f.close()
 jsonf.close()
 
if __name__=="__main__":
 convert(sys.argv[1:])
