# Stage 1:

## Create the dialogflow Agent

1. Create a weatherbot agent in dialogflow.com

2. Create one Intent to check weather info
- Intent Name: "GetWeatherIntent"

3. Add some training phrase as follows
- "whats the weather in Singapore"
- "what is the weather in India"

4. Annotate `Singapore`, `India` with Action and parameters
- Name: location
- Type: any

5. Enable Fulfillment for the Intent "GetWeatherIntent"

6. Run ngrok tunnel and get a https url, update the fulfillment url in dialogflow for your weatherbot agent.
## To run this backend with ngrok tunnel

- Download the ngrok tunnel binary from ngrok.com

For mac/linux
```
ngrok http 5000
```

For Windows
```
ngrok.exe http 5000
```

**Remember to update the ngrok tunnel to dialogflow agent.**


# Stage 2:

1. Now complete the coding exercises to finish the bot
- Refer to app.py for starting point.
- It includes few hits & comments to complete the dialogflow backend code for weather bot.

The steps are as follows:
- ## TODO: STEP 1 # Place your API KEY Here... 
- ## TODO: STEP 2 # Check for intent name and call handler function
- ## TODO: STEP 3 # Complete the logic for handler function

## Install Dependencies
```
pip install -r requirements.txt
```

## Run python app file
```
python app.py
```

# ISSChatbot
