from flask import Flask, request, make_response, jsonify
import requests
import json

app = Flask(__name__)
## TODO: STEP 1 
APIKEY = "??" # Place your API KEY Here... 
#"8a81d247d650cb16469c4ba3ceb7d265"

# **********************
# UTIL FUNCTIONS : START
# **********************

def getjson(url):
    resp =requests.get(url)
    return resp.json()

def getWeatherInfo(location):
    API_ENDPOINT = f"http://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&q={location}"
    data = getjson(API_ENDPOINT)
    code = data["cod"]
    if code == 200:
        return data["weather"][0]["description"]

# **********************
# UTIL FUNCTIONS : END
# **********************

# *****************************
# Intent Handlers funcs : START
# *****************************

## TODO Step 3:
def getWeatherIntentHandler(req):
    """
    Get location parameter from dialogflow and call the util function `getWeatherInfo` to get weather info
    """
    # HINT: req.get("queryResult").get("parameters").get("some-example-parameter")

    location = "??" #write code here
    
    location = "??" # Make sure location is lower case

    # Call the getWeatherInfo function with `location` as input, and store the result in `info`
    info = "??"
    
    return f"Currently in {location} , its {info}"

# ***************************
# Intent Handlers funcs : END
# ***************************

## Decision Table ##
def getDecisionTree(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if course["coursename"] == coursename:
            return True
    return False
## end ##

def getCourseDuration(coursename):
    with open("s.json","r") as f:
        temp = json.loads(f.read())
        data = temp["data"]
    for course in data:
        if course["coursename"] == coursename:
            coursetype = course["coursetype"]
            return coursetype
    return "Something wrong ..."


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
        #respose_text = "Yes,"+course_name+"."
        if getDecisionTree(course_name):
            #respose_text = "Yes, we have "+course_name+"."
            respose_text = "Yes, we have "+course_name+". And it's a "+getCourseDuration(course_name)+"."
        else:
            respose_text = "Sorry, we don't have "+course_name+" so far." ## Call your getWeatherIntentHandler with req object as input. 
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