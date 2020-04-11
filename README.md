# Backend for text summarization

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Risto Trajanov 171523  
School project for web development(FINKI).    
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

## Medium posts

https://medium.com/data-county/text-summarization-with-flask-api-and-google-chrome-extension-on-frontend-cbde9b9a36c1  
https://medium.com/data-county/adding-text-summarization-with-sumy-into-flask-api-with-chrome-extension-on-frontend-3bead9329bb6
