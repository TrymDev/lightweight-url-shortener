# Lightweight URL Shortener

A simple URL shortener built in Python

## Features
- Shortens long URLs
- Redirects to original URL
- Local storage

## Tech
- Python
- Flask

## How to run
```bash
pip install -r requirements.txt
py main.py
```

## Usage
This service is a minimal HTTP API.

### Create a shortened URL
`GET /add/<url>`

Returns a shortened URL identifier.

### Redirect
`GET /<short_code>`

Redirects to the original URL if it exists.