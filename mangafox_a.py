"""A script to download any manga from mangafox"""
#importing modules
import requests
from bs4 import BeautifulSoup
import os
#Checking and creating folder as needed for the parent directory:
def create_folder(x):
    if os.path.exists(x):
        print "Folder already exists"
        os.chdir(x)
    else :
        os.makedirs(x)
        print "Dir created"
        os.chdir(x)
#checking for log file and creating it if necceasry
def check_log(x):
   if os.path.exists(x):
       print "log file already exists "
       return True
   else:
       return False
#creating and updating log
def update_log(x):
   f=open(manga_log,"a")
   f.write("\n")
   f.write(x)
   f.close()
#fetching url from log
def log_fetch(x):
   x = open(x,"r")
   y=[]
   for i in x:                                                      #creating a list of all the item in file
      y.append(i)
   z = y[len(y)-1]                                                  #getting the last item form that list
   return z
#To get valid input for using log fle
def use_log():
   x = True
   while x == True:
      use = raw_input("Use url from log (y/n): ")
      if use == "y":
         x = False
         return True
      elif use == "n":
         x =false 
         return False
      else :
         print "INVALID SELECTION , Enter again ."

#starting the script
print "Hello to manga downloading script ..!"
print "Enter the name of series EXACTLY as shown in mangafox.com ..!"
print "Enjoy"
manga_name = raw_input("Enter the name of manga : ")
manga_log = manga_name
print "Searching for Folder ..."
create_folder(manga_name)
print "Checking for log file ..." 
chapter_list = []     
if check_log(manga_log) == True:
      print "Log File exists."
      if use_log()== True:
         chap= log_fetch(manga_log) 
         chap = int(chap)                                #fetching the number
else:  
   chap = int(raw_input("Enter the episode(number) ,from which download will start: "))
url = "http://mangafox.me/manga/" + manga_name

try:
   for chapter in range(chap,1000) :
        update_log(repr(chapter))
        if os.path.exists(manga_name +" " + repr(chapter) )== True :
            print "Chapter " +repr(chapter) + " exists ..!"
            print "Working on " +repr(chapter) + "..!"
            os.chdir(manga_name +" " + repr(chapter))  
        else:      
            os.makedirs(manga_name +" " + repr(chapter))
            os.chdir(manga_name +" " + repr(chapter))
        print "Working on chapter : " + repr(chapter)
        for page in range(1,100):
            url = ("http://mangafox.me/manga/")+manga_name + "/c" +repr(chapter)+"/"+repr(page) + ".html"
            mrl = ("http://mangafox.me/manga/")+manga_name + "/c" +repr(chapter)+"/"+repr(page+1) + ".html"
            sabo = requests.get(mrl)
            luffy = requests.get(url)
            print "Getting page :" + repr(page)
            print url
            soup1=BeautifulSoup(sabo.content)                                  #creating another soup so that i can end the pages being 
            soup = BeautifulSoup(luffy.content)                                #downloaded .. for the site give the last page of the chapter 
            nami = soup.find(id = "viewer")                                    #even if it has gone page
            sanji = nami.img.get("src")
            nami1 = soup1.find(id = "viewer")                           
            sanji1 = nami1.img.get("src")
            if sanji == sanji1:
                print "Chapter " +repr(chapter)+ " done ..!"
                os.chdir("..")
                break
            else :
                zoro = requests.get(sanji)
                brook = open(repr(page),"w+")
                brook.write(zoro.content)
                brook.close
except AttributeError :
   print "Done"
