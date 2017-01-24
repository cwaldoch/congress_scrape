# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver
import pdb
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

results = []
state_districts_dict = {
	1:[7,'AL'],
     2:[1,'AQ'],
     3:[1,'AK'],
	4:[9,'AZ'],
	5:[4,'AR'],
	6:[53,'CA'],
	7:[7,'CO'],
	8:[5,'CT'],
	9:[1,'DE'],
     10:[1,'DC'],
	11:[27,'FL'],
	12:[14,'GA'],
     13:[1,'GU'],
     14:[2,'HI'],
	15:[2,'ID'],
	16:[18,'IL'],
	17:[9,'IN'],
	18:[4,'IA'],
	19:[4,'KS'],
	20:[6,'KY'],
	21:[6,'LA'],
	22:[2,'ME'],
	23:[8,'MD'],
	24:[9,'MA'],
	25:[14,'MI'],
	26:[8,'MN'],
	27:[4,'MS'],
	28:[8,'MO'],
	29:[1,'MT'],
	30:[3,'NE'],
	31:[4,'NV'],
 	32:[2,'NH'],
 	33:[12,'NJ'],
 	34:[3,'NM'],
 	35:[27,'NY'],
 	36:[13,'NC'],
 	37:[1,'ND'],
     38:[1, 'MP'],
	39:[16,'OH'],
	40:[5,'OK'],
	41:[5,'OR'],
	42:[18,'PA'],
     43:[1,'PR'],
 	44:[2,'RI'],
 	45:[7,'SC'],
 	46:[1,'SD'],
	47:[9,'TN'],
	48:[36,'TX'],
	49:[4,'UT'],
	50:[1,'VT'],
     51:[1,'VI'],
	52:[11,'VA'],
	53:[10,'WA'],
 	54:[3,'WV'],
	55:[8,'WI'],
	56:[1,'WY']
}


areas = range(1,57)

columns = ['state', 'name', 'district', 'party', 'room', 'phone', 'committees']
driver = webdriver.Chrome()
base_url = 'http://www.house.gov/representatives/'
total_time = 0
start = time.clock()
driver.get(base_url)


"""
Notes on how the site structure works:
    

state 1, district 2
//*[@id="byState"]/table[1]/tbody/tr[2]/td[1]


state2, 1 district district 1
//*[@id="byState"]/table[2]/tbody/tr/td[1]

state 4, district 1, multiple districts
//*[@id="byState"]/table[4]/tbody/tr[1]/td[1]

state 4, district 2
//*[@id="byState"]/table[4]/tbody/tr[2]/td[1]

state lkast, district 1
//*[@id="byState"]/table[56]/tbody/tr/td[1]
"""


table = 1
for key in state_districts_dict.keys():
    district_count = state_districts_dict[key][0]
    state = state_districts_dict[key][1]
    
    #print(district_count)
    print(state)
    #//*[@id="byState"]/table[1]/tbody/tr[7]/td[1]
    if district_count == 1:
        district = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[1]').text
        name =driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[2]').text
        party = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[3]').text
        room = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[4]').text
        phone = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[5]').text
        committees = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr/td[6]').text
        results.append([state, name, district, party, room, phone, committees])
        
    else:
        for district_ct in range(1,district_count+1):
            #print('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[1]')
            district = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[1]').text
            name =driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[2]').text
            party = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[3]').text
            room = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[4]').text
            phone = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[5]').text
            committees = driver.find_element_by_xpath('//*[@id="byState"]/table['+str(table)+']/tbody/tr['+str(district_ct)+']/td[6]').text
            
    
            results.append([state, name, district, party, room, phone, committees])
    table +=1
    
driver.close()
driver.quit()
    
df_results = pd.DataFrame(results, columns=  columns, encoding="utf-8")

df_results.to_csv('congress_results.csv')
    
