# Homework Assignment #1: 

## Details:
 
Build a simple "hello world" application in Flask. Here are the specs:

1. The application should start an HTTP server that is listening on a port (any port is fine)
2. When you make a request to the base URL (no path), the application should return a 200 response, and a plain text body that says `"Hello World"`.

## Extra Credit:

For extra credit, return a full HTML 5 page instead of plain text. The hello world message should be wrapped in `<h1>` tags and placed within the `<body>` of the page.

## Running the Application Locally

In the terminal, run:
```sh
export FLASK_ENV-development
flask run
```