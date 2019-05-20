from flask import Flask, request, make_response, jsonify
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
            courselist.append(course["coursename"])
    if not courselist:
        return False,"Next Step"
    else:
        for item in courselist:
            resp_text = resp_text+item+", "
        resp_text=resp_text+"\nPlease type in the course name for more detrails."
        return True,resp_text

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
   req = request.get_json(silent=True, force=True)
   intent_name = req["queryResult"]["intent"]["displayName"]

   ## TODO: STEP 2
   # Write your code here..
   # write some if/else to check for the correct intent name.
   # Write code to call the getWeatherIntentHandler function with appropriate input

   if intent_name == "ISSCourseIntent" : ##
        course_name = req["queryResult"]["parameters"]["coursename"].lower()
        any_name = req["queryResult"]["parameters"]["graduatetype"].lower()

        result1,resp = getGraduateTypeTree(any_name)
        if result1:
            respose_text = resp
        else:
            if not getCourseNameTree(any_name):
                respose_text = "Next Step"
            else:
                respose_text = "Yes, we have the following course which you may want have interested in:\n"
                for item in getCourseNameTree(any_name):
                    respose_text = respose_text + item +" and it's a "+getCourseTypeTree(item)+".\n"
   else:
        respose_text = "No intent matched here"
   # Branching ends here

   # Finally sending this response to Dialogflow.
   return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
