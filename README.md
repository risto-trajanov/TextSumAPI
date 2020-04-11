## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
School project for web development.
Text summarization on web pages using their urls as input and giving the summary as output. 
	
## Technologies
Project is created with:
* Flask API
* Swagger for API documentation
* Sumy for nlp
	
## Setup

Clone the repo:

    git clone https://github.com/risto-trajanov/TextSumAPI
    cd TextSumAPI

Create virtualenv:

    python -m venv textEnv
    textEnv/Scripts/activate.bat
    pip install -r requirements.txt
    
Run the api

    python.exe -m flask run --host 0.0.0.0

Swagger docs available at `http://localhost:5000/swagger.json`
