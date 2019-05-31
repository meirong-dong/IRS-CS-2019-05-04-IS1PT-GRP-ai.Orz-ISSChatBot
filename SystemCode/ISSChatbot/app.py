from flask import Flask, request, make_response, jsonify
from flask import render_template
import requests
import json

app = Flask(__name__)
## TODO: STEP 1


# ***************************
# Intent Handlers funcs : END
# ***************************

## Decision Table Filter Course Name ##
def getCourseNameTree(coursename):
    courselist = []
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if coursename in course["coursename"]:
            courselist.append(course["coursename"])
    return courselist
## end ##

def getCourseTypeTree(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if coursename in course["coursename"]:
            coursetype = course["coursetype"]
            return coursetype
    return "Something wrong ..."

def getGraduateTypeTree(anyname):
    courselist = []
    resp_text = "We have the following courses which are "+anyname+" courses:\n"
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if anyname in course["coursetype"]:
            for coursename in course["coursename"]:
                courselist.append(coursename)
    if not courselist:
        return False,"Next Step"
    else:
        for item in courselist:
            resp_text = resp_text+item+", "
        resp_text=resp_text+"\nPlease type in the course name for more detrails."
        return True,resp_text

def getCourseDurationYear(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if coursename in course["coursename"]:
            durationyear = course["durationyear"]
            return json.dumps(durationyear)
    return "Something wrong ..."

def getCourseDurationSemester(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if coursename in course["coursename"]:
            durationsemester = course["durationsemester"]
            return json.dumps(durationsemester)
    return "Something wrong ..."

def getCourseFee(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if coursename in course["coursename"]:
            fee = course["fee"]
            return json.dumps(fee)
    return "Something wrong ..."

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
   req = request.get_json(silent=True, force=True)
   intent_name = req["queryResult"]["intent"]["displayName"]
   print(req)

   ## TODO: STEP 2
   # Write your code here..
   # write some if/else to check for the correct intent name.
   # Write code to call the getWeatherIntentHandler function with appropriate input

   if intent_name == "ISSCourseIntent" : ##
        any_name = req["queryResult"]["parameters"]["coursename"].lower()
        #any_name = req["queryResult"]["parameters"]["graduatetype"].lower()

        result1,resp = getGraduateTypeTree(any_name)
        if result1:
            respose_text = resp
        else:
            if not getCourseNameTree(any_name):
                respose_text = "Please refer to the NUS ISS offical website."
            else:
                respose_text = "Yes, we have the course :\n" + any_name + " and it's a " + getCourseTypeTree(any_name) + ".\n"
                #for item in getCourseNameTree(any_name):
                    #respose_text = respose_text + item +" and it's a "+getCourseTypeTree(item)+".\n"
   elif intent_name == "ISSCourseDurantion" :
       any_name = req["queryResult"]["parameters"]["coursename"].lower()

       resp1 = getCourseDurationYear(any_name)
       durationYear = json.loads(resp1)
       resp2 = getCourseDurationSemester(any_name)
       durationSemester = json.loads(resp2)

       if resp1 and resp2:
           respose_text = "The Full-time Program is " + durationYear["fulltime"] + " and " + durationSemester["fulltime"] + "."
           respose_text =  respose_text + " The Part-time Program is " + durationYear["parttime"] + " and " + durationSemester["parttime"] + "."
   elif intent_name == "ISSCourseFee" :
       any_name = req["queryResult"]["parameters"]["coursename"].lower()

       resp3 = getCourseFee(any_name)
       fee = json.loads(resp3)
       if resp3:
           respose_text = "The Full-time Program fee for Singaporean is" + fee["fulltime"]["singaporean"] + ". For SPR is " + fee["fulltime"]["singapore permanent resident"] + ". For International Student is " + fee["fulltime"]["international student"] + "."
   else:
        respose_text = "No intent matched here"
   # Branching ends here

   # Finally sending this response to Dialogflow.
   return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************
@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
