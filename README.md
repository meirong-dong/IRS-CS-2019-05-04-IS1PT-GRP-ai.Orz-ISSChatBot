# Stage 1:

1. Enable Fulfillment for the Intent "ISSCourseIntent"

6. Run ngrok tunnel and get a https url, update the fulfillment url in dialogflow for iss chatbot agent.
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

Remember to update the ngrok tunnel to dialogflow agent.**
Remember to update the iframe src from in /templates/index.html with the url in "Integration" web demo.
## Install Dependencies
```
pip install -r requirements.txt
```

## Run python app file
```
python app.py
```

# ISSChatbot
