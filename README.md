# Instructions 

1. Create a virtual environment

```
# virtualenv venv
# source venv/bin/activate
```

2. Install the depedent packages 

```
# pip3 install -r requirements.txt
```

3. Start the server

```
# cd api;

# uvicorn main:app --reload
```

4. Validate the APIs 

In the browser naviagte to this path ``` http://localhost:8000/docs```
