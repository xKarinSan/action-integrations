#  🚜 Farm Stack Test 
This is a simple sample of a FARM stack applcation built from ground up, inclusive of github actions, automated testings and deployment to AWS. 


## Dependencies
Here are the list of dependencies or requirements needed to run the project.

### Frontend Dependencies
<p align="left">
   <img src ="https://cdn.worldvectorlogo.com/logos/react-1.svg" alt="React Logo" height="80px"/>
   <img src="https://vitejs.dev/logo.svg" alt="Vite Logo" height="80px"/>
   <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfFcv7Pkda7A7neO9Z38C0vn1MkMd35_Sb7SF3QcYLOQ&s" alt="ChakraUI Logo" height="80px"/>
   <img src="https://vitest.dev/logo.svg" alt="Vitest Logo" height="80px"/>
</p>

### Backend Dependencies
<p align="left">
   <img src ="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" height="80px"/>
   <img src ="https://www.vectorlogo.zone/logos/mongodb/mongodb-ar21.svg" alt="MongoDB Logo" height="80px"/>
   <img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/1200px-Pytest_logo.svg.png" alt="Pytest Logo" height="80px"/>
</p>


## Services used
<p align="left">
   <img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Amazon_Lambda_architecture_logo.svg/400px-Amazon_Lambda_architecture_logo.svg.png" alt="AWS Lambda Logo" height="80px"/>
   <img src ="https://raw.githubusercontent.com/pulumi/pulumi-aws-apigateway/main/assets/logo.png" alt="Amazon API Gateway Logo" height="80px"/>
   <img src ="https://www.vectorlogo.zone/logos/mongodb/mongodb-ar21.svg" alt="MongoDB Logo" height="80px"/>
   <img src ="https://res.cloudinary.com/practicaldev/image/fetch/s--mkZY0XpP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://day-journal.com/memo/images/logo/aws/amplify.png" alt="AWS Amplify Logo" height="80px"/>
</p>

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

## Github Actions/CICD
### Backend
Refer [here](https://github.com/xKarinSan/action-integrations/tree/main/.github/workflows/backend_cicd.yml). 

**Steps (for backend-continuous-integration)**
1. Dependencies are installed
2. Automatic tests are run
3. Dependencies and the main files are installed in another folder
4. Contents from step 3) are zipped and turned into an artifact which will be used in the  backend-continuous-deployment job.

**Steps (for backend-continuous-deployment)**
1. Install the AWS CLI
2. Download the artifact from Step 3 in the backend-continuous-integration job.
3. Upload the contents from the previous step to Amazon S3
4. Deploy the contents from the previous step to Amazon Lambda


## Environment Variables

### Github actions (this will be in the root of this entire project.
- AWS_ACCESS_KEY_ID: the access key of your account (done via Amazon KMS)
- AWS_SECRET_ACCESS_KEY: the secret access key of your account (done via Amazon KMS)
- AWS_DEFAULT_REGION: your default AWS region
- LAMBDA_FUNCTION_NAME: name of your Lambda function
- BUCKET_NAME: name of your S3 bucket
- DATABASE_NAME: the database which will be used for testing
  
**NOTE: the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY belong to the same key pair** 

### Frontend
- VITE_APP_BACKEND: the deployed link of the FastAPI REST API (this is the AWS Gateway link)

### Backend
- DATABASE_URL: the URL of your MongoDB Database
- DATABASE_NAME: the name of your MongoDB database (names differ in production and development)
- FRONTEND_URL: the URL of the frontend (deployed on AWS Amplify)

## Contributor
[<img src="https://github.com/xkarinsan.png" width="60px;"/>](https://github.com/xKarinSan)
