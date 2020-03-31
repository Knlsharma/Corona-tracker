from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
import pandas as pd
import sqlalchemy as sq
from urllib.request import urlopen, Request

# Slack and Table
import requests 
from tabulate import tabulate
import json
import logging


# Create your views here.

def slack_update(request):
   headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                       'AppleWebKit/537.11 (KHTML, like Gecko) '
                       'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
  
   reg_url = 'https://www.worldometers.info/coronavirus/'
   req = Request(url=reg_url, headers=headers) 
   html = urlopen(req).read() 
   d = pd.read_html(html)

   print('d is' , d)
   d1 = d[0]
   s = d1.to_string(index=False)
   print("Incoming data" ,s)
   engine = sq.create_engine("mysql+pymysql://root:root@localhost:3306/corona")
   db_frame = pd.read_sql_table("total_cases", engine)
   sdb = db_frame.to_string(index=False)
   print("Database fetch" ,sdb)
   d1.to_sql('total_cases' , con = engine , index = False , if_exists = 'replace')
   d1.to_csv('my data.csv')
   return HttpResponse(' <h1>Page was found </h1>')


HEADERS = {
    'Content-type': 'application/json'
}

 # slack_bot
def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
    def slackit(msg):
        logging.info('Sending {msg} to slack'.format(msg=msg))
        payload = { 'text': msg }
        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))
    return slackit

https://hooks.slack.com/services/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


table = tabulate(d0 , tablefmt='psql')
 msg = {'text' : table}
requests.post(web_hook_url, headers=HEADERS, data=json.dumps(msg))
