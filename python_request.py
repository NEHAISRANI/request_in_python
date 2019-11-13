import requests
import json
from pprint import pprint 

#Javascript Object Notation
print("********** WELCOME SARAL COURSES **********") 

url="http://saral.navgurukul.org/api/courses"  #courses url
def response(saral_url): 
    response=requests.get(saral_url) 
    data=response.json()
    return (data) 
dataResponse=response(url) 
# pprint (dataResponse)
 
def writeData(responseData):
    with open("courses.json","w") as file1:
        write_data=json.dump(responseData,file1,indent=2, sort_keys=True)
writeData(dataResponse)


def ReadData():
    with open("courses.json","r") as file: 
        loadData =json.load(file)
        return(loadData)  
loadCourses=ReadData() 
# pprint (load_courses)  
courses=loadCourses["availableCourses"] #global variable



saralcoursesId_List=[] 
def courses_and_Id_Data(course):  #in this function saral courses and id will print
        count=0
        courses_Data=course["availableCourses"]
        for i in courses_Data:
                print (count,i["name"],i["id"])
                saralcoursesId_List.append(i["id"])
                count=count+1
        return(saralcoursesId_List)
coursesData=courses_and_Id_Data(loadCourses) 
# print (coursesData) 


def userInputCourses():   
        user=int(input("select your course no-\n"))
        coursesDataId=(coursesData[user])
        return (coursesDataId)
coursesId=userInputCourses()  


for index in courses:
        if index["id"]==coursesId:
                print (index["name"])


parentExercise_Idlist=[]  
def getExercise(secondUrl):
        response_secondUrl=response(secondUrl)
        parentExercise = response_secondUrl["data"] #second url key
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
        return (parentExercise_Idlist) 
url2=("http://saral.navgurukul.org/api/courses/"+str(coursesId)+"/exercises")
Exercise=getExercise(url2) 
# print(Exercise) 


