import sys
import datetime as dt
import json
import time
def converttojson(dictionary):
    addedtask=json.dumps(dictionary)

    with open("Taskjson.json","a") as f:
        f.write("\n")
        f.write(addedtask)
    f.close()
    print(addedtask)
def taskadd():

    #print(sys.argv[1],sys.argv[2])#debug print

    #formatting for unix math
    month = int(sys.argv[2][0:2])
    day = int(sys.argv[2][2:4])
    year=int(sys.argv[2][4:8])
    duedateunix=dt.datetime(year,month,day)
    
    task={
        "taskname": str({sys.argv[1]}),
        "taskduedate":str({sys.argv[2]}),
        "timetodue":duedateunix.timestamp()-time.time()
        }
    #convert unix math back to readable
    timeleft= task["timetodue"]/100
    task["timeremaining"] = timeleft
    
    converttojson(task)

if len(sys.argv)>1:
    #print("debug if loop")
    taskadd()
#else:
    #print("debug else loop")
