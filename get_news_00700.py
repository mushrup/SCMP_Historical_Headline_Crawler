import urllib2
import html2text
import re
import os
import sys
import pandas as pd
import time



def get_news(token,name,date1,date2):
  days = ['01','31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
  months = ['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#  url = 'http://www.hko.gov.hk/cgi-bin/hko/yes.pl?year='+str(year)+'&month='+months[month]+'&day='+days[date]+'&language=english&B1=Confirm'
  os.system('wget -qO- http://www.scmp.com/content/search/articles/'+name+'?f[0]=ds_created%3A%5B'+date1+'T00%3A00%3A00Z%20TO%20'+date2+'T23%3A59%3A59Z%5D > '+str(token)+'.csv')

def to_list(symbol,name):
  file_name = symbol+'.csv'
  news = [] 
  with open(file_name) as input_data:
    for line in input_data:
      if line.startswith('    <h3 class="title">') :
        segments = line.split('>')
        words = segments[2].split('<')
        news.append(words[0])
  return news

months_df = pd.DataFrame(pd.io.parsers.read_csv('Months.csv',dtype = {
  'Symbol':str,
  'News1':str,
  'News2':str,
  'News3':str,
  'News4':str,
  'News5':str,
  'News6':str,
  'News7':str,
  'News8':str,
  'News9':str,
  'News10':str}))
for index,row in months_df.iterrows():
  date1 = row[0]
  date2 = row[1]
  get_news('00700','Tencent',date1,date2)
  news = to_list('00700','Tencent')
  print news
  idx = 0
  while idx < len(news):
    column = 'News'+str(idx+1)
    months_df.set_value(index,column,news[idx])
    idx = idx + 1
  os.system('rm 00700.csv')
  months_df.to_csv('News_Dataset_Tencent.csv', encoding='utf-8')






