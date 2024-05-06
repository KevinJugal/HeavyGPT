# HeavyGPT
Built a Python API using FastAPI and integrate it with OpenAI's ChatGPT. Deployed on AWS EC2


Step 1: Setup
First, we'll need to install the required packages. For this project, we're going to use FastAPI and Uvicorn for creating and running our API, and OpenAI to use the GPT-3 model for text generation.

Step 2: Creating the API
We start by initializing our FastAPI app in the main.py file. Additionally, we import the Pydantic BaseModel, which allows us to define how our data should be modeled.

Step 3: Integrating with OpenAI ChatGPT
We're going to use OpenAI's GPT-3 model to generate product descriptions.
In utils.py, we're initializing the OpenAI API key and defining a function generate_description which takes in product details and returns a generated description.

Step 4: Running the API and Making Requests
Run your API using Uvicorn:
uvicorn main:app --reload

Once you are done with this, in order to connect to the Amazon EC2 server connect with the following code on your bash terminal
SSH Client : chmod 400 "HeavyGPT.pem"

Run this to go on to the EC2 terminal:
ssh -i "HeavyGPT.pem" ec2-user@ec2-13-232-41-169.ap-south-1.compute.amazonaws.com
