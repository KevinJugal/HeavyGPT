# HeavyGPT
Built a Python API using FastAPI and integrate it with OpenAI's ChatGPT. Deployed on AWS EC2


Before getting into it, we need to initialize a virtual environment, make sure you have venv installed if not : pip install venv<br><br>
Initialize by: python -m venv fastapi<br>
fastapi is the name of the environment that I have taken and then follow the below steps:<br><br>

Step 1: Setup <br>
First, we'll need to install the required packages. For this project, we're going to use FastAPI and Uvicorn for creating and running our API, and OpenAI to use the GPT-3 model for text generation.
<br>
<br>
<br>
Step 2: Creating the API<br>
We start by initializing our FastAPI app in the main.py file. Additionally, we import the Pydantic BaseModel, which allows us to define how our data should be modeled.
<br>
<br>
<br>
Step 3: Integrating with OpenAI ChatGPT<br>
We're going to use OpenAI's GPT-3 model to generate product descriptions.<br>
In utils.py, we're initializing the OpenAI API key and defining a function generate_description which takes in product details and returns a generated description.
<br>
<br>
<br>
Step 4: Running the API and Making Requests<br>
Run your API using Uvicorn:<br>
uvicorn main:app --reload
<br>
<br>
<br>
Once you are done with this, in order to connect to the Amazon EC2 server connect with the following code on your bash terminal<br>
<br>
<br>
SSH Client : chmod 400 "HeavyGPT.pem"<br>
<br>
Run this to go on to the EC2 terminal:<br>
<br>
ssh -i "HeavyGPT.pem" ec2-user@ec2-13-232-41-169.ap-south-1.compute.amazonaws.com<br>
<br>
