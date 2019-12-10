### CIS 192 Final Project 

#### What2Eat 
I personally have difficulty in deciding what to eat when go out with my friends for lunch or dinner. Often we have something we definitely do not want to eat but cannot decide what we really want to eat. What2Eat is a Django-supported webapp that helps a user to decide what to have for lunch/dinner.

#### To Run the App
in the what2eat directory, run: 

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Access the website via ```localhost:8000```

**Selection Mode**
1. Select your company 
: select users from the list of friends that you're going to have dinner with. 
2. Category Selection
: remove any category that you certainly don't want to have today. 
3. Selection Result
: What2East gives you few suggestions based on the saved restaurants you and your friends have. It will also provide few more recommendations from the custom categories that were highly rated on Yelp.

#### Code Structure 
The project utilizes Django, Yelp API, django-friendship module and few more basic libraries/packages. 

The project contains one main django app call "core"
```core/views.py``` manages all functionalities regarding signup/signout/login and adding restaurants to the list 
```core/yelp.py``` interacts with yelp API to fetch the search result. 
```core/selection.py``` manages all selection processes in deciding what restaurant to go. 

Also, I've used django-friendship package (https://github.com/revsys/django-friendship) to implement friend request functionalities. 

#### Class definition 
1.  ```core/models.py``` defines various django models used in the app. Uses magic method ```__str__``` so that it can be represented with names in admin page 
2. ```core/yelp.py``` has a class ```YelpAPIManager``` so that the parameters for the API request can be easily modified. 

#### non-trivial first-party packages
```core/yelp.py``` uses ```requests, json``` and ```random```
#### non-trivial third-party packages
```Django```, (Yelp api?) and ```django-friendship``` package  (https://github.com/revsys/django-friendship)