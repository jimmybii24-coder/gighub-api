# GigHub API

## Description

This is a FastAPI-based REST API developed for the GigHub project assignment. The API allows clients and freelancers to manage freelance job listings (gigs).

**Admission Number:** C027-01-0887/2024

## Features

- View all gigs
- Filter gigs by category and budget
- Search gigs by title
- View a gig by ID
- Create a new gig
- Update a gig's budget or status
- Delete a gig

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Running the Project

1. Create a virtual environment:

   ```bash
   py -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

4. Run the API:

   ```bash
   py -m uvicorn main:app --reload
   ```

5. Open Swagger documentation:
   ```
   http://127.0.0.1:8000/docs
   ```
