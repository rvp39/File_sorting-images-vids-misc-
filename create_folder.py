import os
import time

def movcmd(fil,dst):
    scr=os.getcwd()+"\\"+fil
    dstn=os.getcwd()+"\\"+dst
    
    movecmd="move \"{}\" \"{}\"".format(scr,dstn)
    return (movecmd)
#exrtact src dir from the file
with open("OperationDir.txt",encoding="utf-8") as f:
    src=f.read()
print (src)

os.chdir(src)

rootTree=os.listdir()

folder  = []
videos  = []
pictures= []
Zip     = []
misc    = []

for i in rootTree:
    if not( "." in i):
        folder.append(i)
    elif i[-4:] == ".mp4":
        videos.append(i)
    elif (i[-5:] == ".jpeg") or (i[-4:] ==".png") or (i[-4:] == ".jpg"):
        pictures.append(i)
    elif i[-4:]==".zip":
        Zip.append(i)
    else:
        misc.append(i)

# print (videos)
# print(pictures)

#creating folder if it doent exist

if folder.count("images")==0:
    os.system("mkdir images")
if folder.count("videos")==0:
    os.system("mkdir videos")
if folder.count("misc")==0:
    os.system("mkdir misc")
if folder.count("zip")==0:
    os.system("mkdir zip")    

for i in pictures:
    os.system(movcmd(i,"images"))
    time.sleep(5)

for i in videos:
    os.system(movcmd(i,"videos"))
    time.sleep(30)
for i in Zip:
    os.system(movcmd(i,"zip"))
    time.sleep(15)
for i in misc:
    os.system(movcmd(i,"misc"))
    time.sleep(90)




#print (folder)
# print(rootTree)

#print(os.getcwd())
