from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import re
import os
import time
from time import gmtime, strftime
import sys
url0=raw_input('url')
path = r'/home/byandfor/Desktop/web_crash/'
content0 = urllib2.urlopen(url0).read()
soup0 = BeautifulSoup(content0)
print soup0.title
state=raw_input('state')
os.makedirs(path+state)

##########################################3

##############################################
columns=['1location','2city','3state','4date','5Latidute','6Longitude','7Vehicles','8DrunkenPersons','9Fatalites', '91Persons','92Pedestrians']
statedata=pd.DataFrame(columns=columns)


for link in soup0.findAll('a', attrs={'href': re.compile("/accidents/acc-")}):
    url='http://www.city-data.com'+link['href']
    city=link.text[48:]
    execfile('/home/byandfor/Desktop/datascrap.py')
    statedata=statedata.append(cleandata)
##################################
statedata.reset_index()
statedata=pd.DataFrame(statedata, dtype=str)
statedata.to_csv('/home/byandfor/Desktop/web_crash/All_data/'+state+'accident.csv', index=False)
address_columns=['2Address', '3City','4State']
address=pd.DataFrame(columns=address_columns)
address['2Address']=statedata['1location']
address['3City']=statedata['2city']
address['4State']=statedata['3state']
address=pd.DataFrame(address,dtype=str)
address['1Index']=[i for i in xrange(1, len(statedata)+1)]
address.to_csv('/home/byandfor/Desktop/web_crash/All_data_address/'+state+'accident_address.csv', index=False)


length=len(statedata)
dic_pt={}
dic_pt['aReportID']=['' for i in xrange(1,length+1)]
dic_pt['bUserId']=[2 for i in xrange(length)]
dic_pt['cReportTypeId']=[2 for i in xrange(length)]# parking ticket 1, accident 2
dic_pt['dAddedBy']=[2 for i in xrange(length)]
dic_pt['eHostId']=[2 for i in xrange(length)]
dic_pt['fLatitude']=statedata['5Latidute']
dic_pt['gLongitude']=statedata['6Longitude']
dic_pt['hRdiusOfImpact']=[5 for i in xrange(length)]
dic_pt['iDescription']=['' for i in xrange(length)]
dic_pt['jPrice2']=[0 for i in xrange(length)]
dic_pt['kReportStatusId']=[1 for i in xrange(length)]
dic_pt['lCreatedTime']=statedata['4date']
dic_pt['mLastModifiedTime']=[strftime("%Y-%m-%d %H:%M:%S", time.localtime()) for i in xrange(length)]
dic_pt['nTotalNumberinjured']=statedata['91Persons']
dic_pt['okilled']=statedata['9Fatalites']
dic_pt['pVehicletypecode']=['' for i in xrange(length)]
data=pd.DataFrame(dic_pt,dtype=str)

data.to_csv('/home/byandfor/Desktop/web_crash/Data_mapping/'+state+'datamapping.csv', index=False, header=False)
