# README Pre Assignment

My simple and sweet solution to pre-assignment for junior developer positions. Uses a Flask API and Svelte front end to display the contents of a sample status file (Debian and Ubuntu /var/lib/dpkg/status). This is a first time im using Flask app as an API endpoint, and first time using svelte (which feels really nice btw. Probably using svelte for my next project as well).

~~App is running on https://reaktor.rauko.la/~~


## Installation


Python 3 (pip) and Node.js (npm) are required for running the development servers locally. Tested on Python 3.7.x, Node 12.13.1 & 10.15.2 and npm 5.8.0 & 6.12.1 

To run the Flask server, we need to install python dependencies. To install them into a working environment specific to this project, navigate to project root, create and activate a venv:
```sh
python3 -m venv venv
source venv/bin/activate # On linux
.\venv\Scripts\activate # On windows
```

Install dependencies and run Flask:

```sh
pip install -r requirements.txt
flask run -p 5001
```

Then open another terminal and navigate to frontend/, and run:

```sh
npm install
npm run dev
```

The url for the app is printed into the terminal, by default it is  http://localhost:5000. 


## What to improve?

Here we have the simple and sweet solution. Here is a bit of "To-do" list of what I'd add if this app was to be further developed:

- Store the package data front end for instant responsiveness ( at least until page refresh)
- Backend caching (Redis or Memcached, no need to read and parse the same file again and again)
- Instead of text file, parse the data into a database (e.g. MySQL). 