# python_jenkins_project

Python project with GitHub and Jenkins (container):

**1.Either install jenkins on a separate linux or you can run jenkins as a contianer:**
In linux server where docker is installed and running perform below steps:

docker pull jenkins/jenkins
docker run -p 8080:8080 --name=jenkins-master -d jenkins/jenkins

You can access Jenkins web from below URL:
<Server_IP>:8080


**2.Create account in GitHub:**
Create a repo: python_jenkins_project
Copy the github repo https URL for cloning in local:
https://github.com/abhiraturi/python_jenkins_project.git


**3.Now in your local system perform the below steps:**
using cmd perform below:

go to any directory:
git clone https://github.com/abhiraturi/python_jenkins_project.git

cd python_jenkins_project

install pyenv: 
pip install virtualenv

create a virtual env: 
virtualenv myenv

Activate virtual env:
myenv\Scripts\activate

Now install necessary libraries:
e.g. pip install flask

Create a hello.py file for Hello world program:
hello.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This is version 1'
	
**4.Now, run the below git commands:**
git branch (will showcase which branch it is set to)

Create a branch:
git branch python

checkout to the branch created:
git checkout python

to check the status of the file or untracked files
git status

add the files to staging 
git add .

push the changes locally:
git commit -m "Adding first version of code"

to push the files to github remote:
git push origin python



**5.Integrate GitHub with Jenkins:**
Go to jenkins -> create a new item -> freestyle project -> git hub -> enter repo url and branch name


Once u commit changes to github, you can run build again in jenkins for the new code



====================================================================================

**Devops Project with GitHub and Jenkins on Linux instance:**


****1. Setting up Jenkins:****
Create EC2 in AWS and perform below steps:

install java:
yum install java

check java version:
java - version

install firewalld command:
yum install firewalld

start firewalld service:
systemctl start firewalld

download the jenkins repo
sudo wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo

import the jenkins key:
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

upgrade dnf:
sudo dnf upgrade

iinstall jenkins:
sudo dnf install jenkins

enable jenkins:
sudo systemctl enable jenkins

start jenkins:
sudo systemctl start jenkins

check jenkins status:
systemctl status jenkins

allow/enable port to linux firewall
firewall-cmd --add-port=8080/tcp --permanent

reload firewall:
firewall-cmd --reload

list firewall ports that are enabled:
firewall-cmd --list-all

Access the web UI:
password is located at:
cat /var/lib/jenkins/secrets/initialAdminPassword


**2. Install git on Jenkins server and install plugin on UI**
install git:
yum install git

check git version:
git version


**3. Create a repo in GitHub**
Create app.py with print hello
Create Jenkins file that contains running the app.py

**4. Creating pipeline in Jenkins for the build**
In Jenkins Create new -> pipeline -> pipleline script from scm -> provide git repo url and branch name -> provide script file (jenkinsfile)
Save and run build
