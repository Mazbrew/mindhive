### FRONTEND
---
+ Ensure that you have the Node Package Manager Installed (npm)
+ Change into the frontend-repo directory
```
cd frontend-repo
```
+ Run npm install to download all of the relevant packages
```
npm install
```
+ Run npm run dev to start the frontend server
```
npm run dev
```
+ go to your localhost port 5173 to view the front end
```
http://localhost:5173/
```

### BACKEND
---
+ Ensure that you have pip and python installed
+ Install virtualenv if you don't already have it
```
pip install virtualenv
```
+ Move into the backend-repo directory and create a virtual env 
```
cd backend-repo
virtualenv env
```
+ Activate the virtualenv
```
env\Scripts\activate.bat
```
+ Install the python modules in requirements.txt
```
pip install -r requirements.txt
```
+ Move into the backend_code directory and run the backend server
```
cd backend_code 
py manage.py runserver
```

### PREPROCESS
---
> This code not need to be ran, a copy of the preprocessed dataset is already within the backend-repo

+ Ensure that you have pip and python installed
+ Install virtualenv if you don't already have it
```
pip install virtualenv
```
+ Move into the preprocessing directory and create a virtual env 
```
cd preprocessing
virtualenv env
```
+ Activate the virtualenv
```
env\Scripts\activate.bat
```
+ Install the python modules in requirements.txt
```
pip install -r requirements.txt
```
+ run the preprocess.py file to create the preprocessed dataset


