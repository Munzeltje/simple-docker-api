######################################
### Steps to test REST web service ###
######################################

-   Make sure Docker is installed
-   Open folder in terminal
-   Run:

        $ docker load -i woz.tar
        $ docker run -d -p 5000:5000 woz:latest


- Open browser and make test request by putting this in the address bar:

        http://0.0.0.0:5000/woz/?m2=80&single=20&married_nokids=20&notmarried_nokids=20&married_kids=20&notmarried_kids=20&single_parent=20&total=120

- If this does not work, check what host the server is on. Run this in terminal:

        $ docker ps

- Replace 0.0.0.0 in the original link with the host the server is on.

- Change the values of the parameters to get different output!

- When done testing, find the container id with:

        $ docker ps

- Then use this id to run the following command and shut down the container:

        $ docker kill [container id]


##################################
### Other files in this folder ###
##################################

Everything else in this folder is what I used to analyze and process data, train a model and test the webservice locally.

Contents:

WOZ
│   README.txt                  - this file
│   requirements.txt            - required python packages
│   data_analysis.py            - script to analyze data, can be used both before and after processing data
│   data_processing.py          - script that processes data, as described in report
│   evaluate_random_forest.py   - script to evaluate the random forest algorithm on train/test split of the data
│   train_random_forest.py      - script to train model on all data
│   utils.py                    - some utilitary functions that are used by other files
│   test_request.py             - script I used for easy local testing of web service
│   woz.tar                     - docker image (not tracked by git because of size)
│   .gitignore
│
└───data
│   │   original .xlsx files with provided data
│   │   .npy files with processed data
│   
└───out
|   │   data_analysis.txt                                               - results of data_analysis.py, before processing
|   │   data_analysis_after_processing.txt                              - results of data_analysis.py, after processing
|   │   trained_model.sav                                               - model trained in train_random_forest.py
|   │   .png files with histograms showing features' distributions      - data visualization obtained with data_processing.py
|
└───RESTWebService
    │   app.ini                - configuration of wsgi
    │   app.py                 - the restful flask api
    │   Dockerfile
    │   requirements.txt       - required python packages
    │   trained_model.sav      - model used by server
    │   wsgi.py                - server's entry point
    │   .dockerignore
