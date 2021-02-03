# ml-gcp
Source code for a continuously delivered Flask Application on Google Cloud Platform. The application is built and deployed using Google App Engine and the continuous deployment is coordinated with Cloud Build.

**Demo Video**  
[![alt text](https://github.com/malcolmsfraser/ml-gcp/blob/main/CDproject-thumbnail.jpg)](https://youtu.be/cK-KkWaCG9Y)  
[[See this setup on AWS]](https://github.com/malcolmsfraser/EB-FlaskApp-CD-CI)

### Setting up this application on your own  

Create a new Google Cloud project

In the Cloud Shell run the following:

>Set the new project
>```{bash}
>gcloud config set project $GOOGLE_CLOUD_PROJECT
>```
>Clone this repository and set it as the working directory
>```{bash}
>git clone https://github.com/malcolmsfraser/ml-gcp.git
>cd ml-gcp
>```
>Create a virtual environment and source it
>```{bash}
>virtualenv --python $(which python3) venv
>source venv/bin/activate
>```
>Install dependencies
>```{bash}
>make install
>```
>Make sure the flask application spplication is working properly
>```{bash}
>python main.py
>```
>Create an application with Google App Engine
>```{bash}
>make setup
>```
>Install, lint, and deploy application
>```{bash}
>make all
>```

### Setting up continuous delivery to your own repository

Create a new repository on GitHub

In the Cloud Shell run the following:

>If needed: create new ssh keys:
>```{bash}
>ssh-keygen -t rsa
>```
>Initiate git and re-assign remote repo origin
>```{bash}
>git init
>git remote rm origin
>git remote add origin <path-to-your-github-repo>
>```
>Follow any other prompts for setting up the connection

Back on the GCP Dashboard

>Navigate to the Cloud Build dashboard
>Navigate to the Settings tab
>>Ensure that App Engine Admin and Service Account User are enabled  

>>Click the link at the bottom for the IAM Section
>>>Ensure that the user ending in <@cloudbuild.gserviceaccount.com> has the following roles:  
>>>>App Engine Admin  
>>>>Cloud Build Service Account  
>>>>Service Account User

Back on the Cloud Build dashboard, navigate to the Triggers tab

>Select "Create Trigger"  
>Follow directions to create a Push trigger linked to your repository.
