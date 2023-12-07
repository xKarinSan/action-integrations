#  🚜 Farm Stack Test 
This is a simple sample of a FARM stack applcation built from ground up, inclusive of github actions, automated testings and deployment to AWS. 

**NOTE: this is still under construction**

## Services used
AWS Lambda
AWS API Gateway

## Dependencies
Here are the list of dependencies or requirements needed to run the project.

### Frontend Dependencies
- ReactJS
- Vite

### Backend Dependencies
- FastAPI for the API
- PyMongo to allow MongoDB interactions between API and the database
- Mangum to allow the API to handle lambda function events 

## Deployment Infrastructure
- AWS Lambda for FastAPI deployments
- AWS Gateway for API security
- MongoDB Atlas for the database
- AWS Amplify to deploy the frontend UI

## Setting Up
**FIRST and FOREMOST, clone this repository**
```
   git clone https://github.com/xkarinsan/action-integrations.git
```

### Frontend Setup
1. Go to the frontend directory and install the dependencies
```
cd frontend && npm i
```
2. Run the frontend (Your current directory should be in the frontend folder
```
npm run dev
```

### Backend Setup
1. Go to the backend directory
```
cd backend
```

2. Install pipreqs (this will allow you to list the dependencies used in requirements.txt) and uvicorn (this allows you to run the FastAPI server)
```
pip install pipreqs uvicorn
```

3. Run the command (this sets the dependencies used in the current project
```
pipreqs --force
```

4. Install the dependencies from requirements.txt
```
pip install -r requirements.txt
```

5. Run the application (be in the root folder while doing this)

**Note the following:**
- backend.app.main is basically the package directory for python packages
- :app refers to the FastAPI instance declared in main.py
- --reload enables hot reload - whenever you make changes in the backend folder, the server automatically reloads
```
uvicorn backend.app.main:app --reload
```

## Testing

### Backend Testing
Type this in your terminal. This goes to the backend folder and then run all the test cases in pytest 
```
cd backend && pytest
```
**NOTE:**
- Just type 'pytest' if you are already in the backend folder
- Run this before you push anything to main. This reduces the chances of the tests being messed up in the github actions.

## Github Actions


## Contributor
[<img src="https://github.com/xkarinsan.png" width="60px;"/>](https://github.com/xKarinSan)
