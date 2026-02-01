# Flask Deliveries API

A small Flask API project demonstrating how to design a production-style POST endpoint with JSON parsing, input validation, clear error responses, and correct HTTP status codes.

This project models a simple delivery job creation service, similar to what might be used in a logistics or fleet operations system.

## Endpoint

### POST /deliveries  
Creates a new delivery job.

#### Example request
```json
{
  "route_id": "GLA-EDB-021",
  "driver_name": "Abi Connolly",
  "eta_minutes": 45,
  "notes": "Delivery window 14:00–16:00."
}
```

#### Validation rules
- Returns `400` for invalid JSON  
- Returns `400` if required fields are missing (`route_id`, `driver_name`, `eta_minutes`)  
- `route_id` must be a non-empty string  
- `driver_name` must be a string and no longer than 50 characters  
- `eta_minutes` must be an integer and greater than or equal to 0  
- `notes` is optional, but if provided must be a string and no longer than 280 characters  

#### Success response
- Returns `201 Created`  
- Responds with a JSON body containing the saved delivery job object, including a generated ID  

## How to run locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Send a request (example using curl):
```bash
curl -X POST http://127.0.0.1:5000/deliveries \
  -H "Content-Type: application/json" \
  -d '{"route_id":"GLA-EDB-021","driver_name":"Abi Connolly","eta_minutes":45,"notes":"Delivery window 14:00–16:00."}'
```

## Project structure

- `app.py` – Flask application and `/deliveries` endpoint  
- `requirements.txt` – Python dependencies  
- `example_request.json` – Sample request payload  

## Why I built this

I built this project to practise backend API development in Python using Flask.  
It demonstrates how I approach:
- validating external input,  
- handling edge cases,  
- returning meaningful HTTP status codes,  
- writing readable, maintainable code that could be extended to use a database or authentication in a real system.

This project is intended as a small but realistic example of how backend services can be designed for reliability and clarity.
