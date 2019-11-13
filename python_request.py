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