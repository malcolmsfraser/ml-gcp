# ml-gcp
Source code for a continuously delivered ML Flask Application on Google Cloud Platform. App build is coordinated using Cloud Build with a listener to this repository.

### Setting up this application on your own  

Create a new Google Cloud project

Set the new project
```{bash}
gcloud config set project $GOOGLE_CLOUD_PROJECT
```
Clone this repository and set it as the working directory
Create a virtual environment and source it
```{bash}
virtualenv --python $(which python3) venv
source venv/bin/activate
```
Create an application with Google App Engine
```{bash}
make setup
```
Install requirements, lint, and deploy application
```{bash}
make all
```

