from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
import pandas as pd
import sqlalchemy as sq


# Create your views here.


def slack_update(request):
   d = pd.read_html('https://www.worldometers.info/coronavirus/')
   d1 = d[0]
   s = d1.to_string(index=False)
   print("Incoming data" ,s)
   engine = sq.create_engine("mysql+pymysql://root:root@localhost:3306/corona")
   db_frame = pd.read_sql_table("total_cases", engine)
   sdb = db_frame.to_string(index=False)
   print("Database fetch" ,sdb)
   d1.to_sql('total_cases' , con = engine , index = False , if_exists = 'replace')
   return HttpResponse(' <h1>Page was found </h1>')

