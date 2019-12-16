import requests
import json
from pprint import pprint 
import os 
from os import path

#Javascript Object Notation

print("********** WELCOME SARAL COURSES **********")

coursesId_list=[]
def courses_and_Id_Data():
        if os.path.exists("courses.json"):
                readFile=open("courses.json","r")
                read=readFile.read()
                loadsData=json.loads(read) 
                print(type(loadsData))
                count=0
                courses_Data=loadsData["availableCourses"]
                for index in courses_Data: 
                        print (count,index["name"],index["id"])
                        coursesId_list.append(index["id"]) 
                        count=count+1
                return(courses_Data)
        else:
                url="http://saral.navgurukul.org/api/courses"  #courses url
                response=requests.get(url)
                data=response.text
                # print(type(data))
                writeFile=open("courses.json","w")
                write=writeFile.write(data)
                dumpData=json.dumps(write)
                writeFile.close() 
        # return(coursesId_list)
        return(courses_Data)
coursesData=courses_and_Id_Data()
# print(coursesData)
# print(coursesId_list)

user=eval(input("select your course no-\n"))
available_Courses_Id=(coursesId_list[user])
print (available_Courses_Id)  

parentExercise_Idlist=[]  
# childExercise_Idlist=[]
def getExercise():
        fileName=("exercises/exercise"+str(available_Courses_Id)+".json") 
        if os.path.exists(fileName): 
                file=open(fileName,"r")
                readFile=file.read()
                loadData=json.loads(readFile)
                parentExercise = loadData["data"]
                count=0 
                for index in parentExercise:
                        print (count, index["name"],index["id"])
                        parentExercise_Idlist.append(index["id"])
                        count=count+1 
                        child_exercise=index["childExercises"]
                        count1=0
                        for j in child_exercise:
                                print("\t",count1,j["name"],j["id"],)
                                count1=count1+1 
                return(parentExercise_Idlist)
        else:
                url2=("http://saral.navgurukul.org/api/courses/"+str(available_Courses_Id)+"/exercises")
                response=requests.get(url2)
                data=response.text 
                print(type(data))
                writeFile=open("exercises/exercise"+str(available_Courses_Id)+".json","w")
                write=writeFile.write(data)
                dumpData=json.dumps(write)
                print(type(dumpData))
                writeFile.close()
Exercise=getExercise()
# print(Exercise)

user=eval(input("enter your exercise"))
content=Exercise[user]
# print(content)

childIdList=[]
slugList=[]
dic={}
def getData_childExercise():
        fileName=("exercises/exercise"+str(available_Courses_Id)+".json")
        if os.path.exists(fileName):
                file=open(fileName,"r")
                readFile=file.read()
                # print(type(readFile))
                loadData=json.loads(readFile)
                # print(type(loadData))   
                parentExercise = loadData["data"]
                # print(parentExercise)
                count=0
                for index in parentExercise:
                        if index["id"]==content:
                                print(count,index["name"],index["id"])
                                childIdList.append(index["id"])
                                slugList.append(index["slug"])
                                count=count+1
                                count1=1
                                childExercise=index["childExercises"]
                                for j in childExercise:
                                        print("\t",count1,j["name"],j["id"])
                                        childIdList.append(j["id"])
                                        slugList.append(j["slug"])
                                        count1=count1+1
                dic["slug"]=slugList
                dic["child_id"]=childIdList
                return (dic)
        else:
                url2=("http://saral.navgurukul.org/api/courses/"+str(available_Courses_Id)+"/exercises")
                response=requests.get(url2)
                data=response.text
                print(type(data))
                writeFile=open("exercises/exercise"+str(available_Courses_Id)+".json","w")
                write=writeFile.write(data)
                dumpData=json.dumps(write) 
                print(type(dumpData))
                writeFile.close()
child=getData_childExercise() 
# print(child)

# print(len(child["child_id"]))


def thirdUrl():
        while True:
                fileName=("content/content"+str(exerciseId)+".json")
                if os.path.exists(fileName):
                        file=open(fileName,"r")
                        readFile=json.load(file)
                        print(readFile)
                        break
                else:
                
                        # print (len(child["slug"][user1]))
                        url3=("http://saral.navgurukul.org/api/courses/"+str(exerciseId)+"/exercise/getBySlug?slug="+str(slug))
                        response=requests.get(url3)
                        data=response.json()
                        print(type(data))
                        print(data)
                        writeFile=open("content/content"+str(exerciseId)+".json","w")
                        writeData=(data["content"])
                        write=json.dump(writeData,writeFile) 
                        writeFile.close() 
user1=eval(input("choose exercise"))
if user1<(len(child["child_id"])):
        slug= child["slug"][user1]
        exerciseId=child["child_id"][user1]
        print(len(child["child_id"]))
        thirdUrl()
else:
        print("page not found") 
