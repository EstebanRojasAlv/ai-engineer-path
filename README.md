# AI Engineer Path

This repository documents my learning path to become an AI engineer. Each module contains the software that I have built to improve my skills.

## Module 1: Python Fundamentals

### Token Cost Calculator

A command-line tool that estimates the cost of using language models.

It calculates the cost per request, per day and per month.

It validates the user input and shows a clear error message when the input is invalid.

### How to run

```
python modulo1/costos_tokens.py
```

### How to test

To run the automated tests for this project, first install the dependencies and then run pytest:

1. `pip install -r requirements.txt`
2. `pytest` 

### Example

```
Model (quick/medium/max): medium
Input tokens per request: 2000
Output tokens per request: 500
Requests per day: 1000
Cost per request: $0.0135
Daily cost: $13.5000
Monthly cost: $405.0000
```

### Weather CLI

A command-line tool that gives the weather information.

You enter a city name and it shows the current temperature and wind speed.

It validates the user input and shows a clear error message when the input is invalid.


### How to run

```
pip install -r requirements.txt
python modulo1/weather.py
```


### Example

```
City: Bogota
Bogotá, Colombia: 12.6°C, wind2.5km/h
```