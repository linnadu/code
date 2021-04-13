from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import re
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
tables = soup.findChildren('table')
number=len(tables)
print soup.title
##################################
def split_data(string):
    string=str(string).lstrip().rstrip()
    string=remove_symb(string)
    string=string.split(';',2)
    lat=string[0][0:8].lstrip().rstrip().replace(',','')
    lon=string[0][9:18].lstrip().rstrip().replace(',','')
    address=string[1][2:].lstrip().rstrip().replace('>','')
    return lat, lon, address

def remove_symb(string):
    string=str(string).lstrip().rstrip().replace('\'', '')
    string=string.replace('<a class="showStreetViewLink" href="javascript:showGoogleSView(', '')
    string=string.replace('</a>','')
    string=string.replace('<br/>]','')
    string=string.replace('[u','')
    string=re.sub('[\[\]]', '',string)
    return string
def change_month(string):
    if string.upper()=='JAN' or 'JANUARY':
        string='01'
    elif string.upper()=='FEB' or 'FEBRUARY':
        string='02'
    elif string.upper()=='MAR' or 'MARCH':
        string='03'
    elif string.upper()=='APR' or 'APRIL':
        string='04'
    elif string.upper()=='MAY' or 'MAY':
        string='05'
    elif string.upper()=='JUN.' or 'JUNE':
        string='06'
    elif string.upper()=='JULY':
        string='07'
    elif string.upper()=='AUGUST' or 'AUG':
        string='08'
    elif string.upper()=='SEP' or 'SEPTEMBER':
        string='09'
    elif string.upper()=='OCT' or 'OCTOBER':
        string='10'
    elif string.upper()=='NOV' or 'NOVEMBER':
        string='11'
    elif string.upper()=='DECEMBER' or 'DEC':
        string='12'
    return string
        
def change_day(string):
    if len(string)<2:
        string='0'+string
    return string

def change_date(string):
    string=str(string).lstrip().rstrip().replace(',', '')
    string=string.split(' ',5)
    month=change_month(string[0])
    day=change_day(string[1])
    year=string[2]
    hour=string[3][0:2]
    mins=string[3][3:5]
    seds='00'
    try:
        last=string[4]
        if last.upper()=='PM':
            hour=str(int(hour)+12)
    except:
        hour='00'
    date=year+'-'+month+'-'+day+ ' ' + hour+':'+mins+':'+seds
    return date

def remove_dash(string):
    string=str(string).lstrip().rstrip().replace(',', '')
    string=re.sub('[-]', '', string)
    return string
###################retrive the 
cleandata={}

cleandata['1location']=[]
cleandata['2city']=[]
cleandata['3state']=[]
cleandata['4date']=[]
cleandata['5Latidute']=[]
cleandata['6Longitude']=[]
cleandata['7Vehicles']=[]
cleandata['8DrunkenPersons']=[]
cleandata['9Fatalites']=[]
cleandata['91Persons']=[]
cleandata['92Pedestrians']=[]

for i in xrange(1, number):
    my_table=tables[i]
    for i, rows in enumerate(my_table.findChildren(['td'])):
        row=rows.contents
        row=remove_symb(row)
         
        if i%8==1:
            
            cleandata['4date'].append(change_date(row))
        elif i%8==2:
            try:
                lat, lon, address=split_data(row)
                cleandata['5Latidute'].append(lat)
                cleandata['6Longitude'].append(lon)
                cleandata['1location'].append(address)
            except:
                cleandata['5Latidute'].append('')
                cleandata['6Longitude'].append('')
                cleandata['1location'].append(row)
        elif i%8==3:
            cleandata['7Vehicles'].append(remove_dash(row.replace(',','')))
        elif i%8==4:
            cleandata['8DrunkenPersons'].append(remove_dash(row.replace(',','')))
        elif i%8==5:
            cleandata['9Fatalites'].append(remove_dash(row.replace(',','')))
        elif i%8==6:
            cleandata['91Persons'].append(remove_dash(row.replace(',','')))
        elif i%8==7:
            cleandata['92Pedestrians'].append(remove_dash(row.replace(',','')))
        else:
            cleandata['2city'].append(city)
            cleandata['3state'].append(state)
    
    
    
cleandata=pd.DataFrame(cleandata, dtype=str)
file_name=state +'_'+city+'_'+'crash.csv'
cleandata.to_csv('/home/byandfor/Desktop/web_crash/'+state+'/'+file_name, index=False)



########################################

        if not s or k == 0: return 0
        dic = {}  
        maxLength = 0 # length 
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            while j <= i and len(dic) > k:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    del dic[s[j]] 
                j += 1
            maxLength = max(maxLength, i - j + 1) 
        return maxLength
        


        dic = {}
        j = 0
        maxLength = 0
        for i in range(len(s)):   
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]] + 1) # dic[s[i]] may be outside of j
                dic[s[i]] = i
            maxLength = max(maxLength, i - j + 1)
        return maxLength
   
