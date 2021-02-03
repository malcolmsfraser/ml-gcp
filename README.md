# ml-gcp
Source code for a continuously delivered Flask Application on Google Cloud Platform. App build is coordinated using Cloud Build with a listener to this repository.

### Setting up this application on your own  

Create a new Google Cloud project

In the Cloud Shell run the following:

Set the new project
```{bash}
gcloud config set project $GOOGLE_CLOUD_PROJECT
```
Clone this repository and set it as the working directory
```{bash}
git clone https://github.com/malcolmsfraser/ml-gcp.git
cd ml-gcp
```
Create a virtual environment and source it
```{bash}
virtualenv --python $(which python3) venv
source venv/bin/activate
```
Make sure the flask application spplication is working properly
```{bash}
python main.py
```
Create an application with Google App Engine
```{bash}
make setup
```
Install requirements, lint, and deploy application
```{bash}
make all
```

