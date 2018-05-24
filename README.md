=====================
 
 Project name: ‘virtufib’
  
 OS: Centos 7.5
   
   Dependencies:
   Python3.4 or higher
   pip3 (pip)
   pipenv
   Python modules automatically installed with pipenv; Flask, flask_restful, json

Prerequisites:
 
Install python 3.4 or higher:  yum install python34
  
Install python pip3:  yum install python34-pip
   
Install git:  yum install git

Install pipenv: pip3 install pipenv
 
Download mini-app: git clone https://github.com/tanyavariel/virtufib.git virtufib

cd to virtufib
   
Install Flask:  pipenv install flask

Install flask_restful:  pipenv install flask_restful
 
Run: pipenv update
  
Run: pipenv run python run_app.py
     
The app should display something to the following:
   * Serving Flask app "api.fib" (lazy loading)
   * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
   * Debug mode: on
   * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 295-845-806
                    
                     
To test and validate:
                     
Use CURL or your browser to access the URLs:
                       
To view a fibonacci sequence up to a given number:
                        
  curl http://localhost:8080/adfib/<SEQNUM>  - Where <SEQNUM> is a valid postitive integer
                         
To view all requested sequences:
                          
  curl http://localhost:8080/swfib/
                           
To remove a sequence from the history:
                            
  curl http://localhost:8080/defib/2
