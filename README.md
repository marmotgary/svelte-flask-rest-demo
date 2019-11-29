# README Pre Assignment

My solution to pre-assignment for junior developer positions. Uses a Flask API and Svelte front end to display the contents of a sample status file (Debian and Ubuntu /var/lib/dpkg/status). 

App is running on https://reaktor.rauko.la/


## Installation


Python 3 and Node.js are required for running the development servers locally. Tested on Python 3.7.x and on Node 12.13.1 & 10.15.2. 

To run the Flask server, navigate to project root, create and activate a venv and run:

```sh
pip install -r requirements.txt
flask run -p 5001
```

Then navigate to /frontend, and run:

```sh
npm install
npm run dev
```

Now the app should be running on localhost (On the default port -- 5000?)