# Python EPCIS Subscription

### Introduction

EPCIS stands for Electronic Product Code Information Services. It is a global standard developed by GS1, an international organization that develops and maintains standards for business communication. EPCIS provides a standardized way to capture and share information about the movement and status of physical or digital objects (such as goods and assets) throughout the supply chain.


### EPCIS Query

In EPCIS standard, users can define custom queries based on their requirements. These queries can target specific locations, values, codes or time frames, allowing for precise monitoring of products 
throughout the supply chain.

Users can leverage the benefits of EPCIS query subscription, upon capturing an event that matches a subscribed query, the system triggers real-time notifications. These notifications can be configured to alert via email, SMS, or through other communication channels, ensuring timely updates.

### About Project

This python based project can be used to subscribe to EPCIS  query and get messages when new event matching the query is captured into the EPCIS repository.

#### Prerequisites
It is assumed that an existing EPCIS repository is set up and running in either local environment or remote environment. Also, required query has been already built and saved into the EPCIS 
repository. In this project we are making use of the query named `TemperatureAlert` which provides us with subscription messages when eventType `ObjectEvent` is captured with action as `OBSERVE` 
and temperature value more than `25 degree`. 


### Set up

1. Modify the `config.py` file as per our credentials associated to EPCIS repository. Update the `USERNAME`, `PASSOWRD`, `CLIENT_ID`, etc. 


2. Depending on the PIP version installed on the system, run the following command to download all the required libraries:

```
pip install -r requirements.txt

or

pip3 install -r requirements.txt
```

After that run the `subscription-alert.py` python project to connect to EPCIS query using the subscription and obtain the matching messages directly within the python run window.