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

slugList=[]
slugidList=[] 
dic ={}
def getData_childExercise(IDS): 
        # print(parent)
        response_parent=response("http://saral.navgurukul.org/api/courses/"+str(IDS)+"/exercises")
        # pprint(response_parent) 
        parent_Child_Data=response_parent["data"]
        count=0 
        for index in parent_Child_Data: 
                if index["id"]==parentIndex:
                        print (count, index["name"],index["id"])
                        slugidList.append(index["id"])
                        parent_slug=(index["slug"])
                        # print (parent_slug)
                        slugList.append(parent_slug)
                        count=count+1
                        child_exercise=index["childExercises"]
                        count1=1
                        for child in child_exercise:
                                print ("\t",count1,child["name"],child["id"])
                                slugidList.append(child["id"])
                                # print(child_slug)
                                slugList.append(child["slug"])
                                # print ("                ",j["slug"]) 
                                count1=count1+1 
        dic["slug"]=slugList
        dic["child_id"]=slugidList
        return (dic)
while True:    
        user1=input("enter your choice if you want to go UP enter up or want exercise data-enter execise no")
        if user1=="up":
                load=ReadData()
                course=courses_and_Id_Data(load)
                break
        else:
                user1=int(user1) 
                parentIndex=(Exercise[user1]) 
                # print(parentIndex)
                child = getData_childExercise(coursesId) 
                # print(child)
                break
user1=eval(input("choose exercise"))
choose_slug = child["slug"][user1]
print(choose_slug) 
slug_id = child["child_id"][user1]
print(slug_id)

def thirdUrl(thirdUrl): #in this function get the content 
        thirdUrlResponse=response(thirdUrl) 
        # print (thirdUrlResponse)
        content=thirdUrlResponse["content"]
        return(content)
url3=("http://saral.navgurukul.org/api/courses/"+str(slug_id)+"/exercise/getBySlug?slug="+str(choose_slug))
third=thirdUrl(url3) 
print(third)


def next_and_previous(): 
        while True:
                user=(input("enter *p* for previous and *n* for next \n"))
                if user=="n": 
                        global user1
                        if user1<(len(child["child_id"]))-1:
                                user1=user1+1
                                # print(user1)
                                slug = child["child_id"][user1]
                                print(slug)
                                choose= child["slug"][user1]
                                print(choose)
                                thirdApi=thirdUrl("http://saral.navgurukul.org/api/courses/"+str(slug)+"/exercise/getBySlug?slug="+str(choose))
                                print(thirdApi)
                        else:
                                print ("page not found")
                                break
                else:
                        
                        user1=user1-1
                        # print(user1)
                        if user1<0: 
                                print("page not found")
                                break
                        else:
                                slug= child["child_id"][user1]
                                print(slug)
                                choose= child["slug"][user1]
                                print(choose)
                                thirdApi=thirdUrl("http://saral.navgurukul.org/api/courses/"+str(slug)+"/exercise/getBySlug?slug="+str(choose))
                                print(thirdApi)
                        
next_and_previous()