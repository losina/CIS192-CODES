### CIS192 HW5 Blog Assignment 

#### To Run 
```
python3 manage.py runserver
```
You can access the page via ```localhost:8000```

#### Create Super user
In order to access admin page, you have to create a super user using the following command:
```
python3 manage.py createsuperuser
```
Follow the prompts to create username and password. Then log in at ```localhost:8000/admin```

#### Blog Posts
The main page (splash page) of the blog can be accessed through  ```localhost:8000```
To see all blog posts, access ```localhost:8000/blog```. Clicking the link to each post leads to individual webpage for each post. 

#### Architecture 
  ```about``` is the app deals with splash page 
   ```post``` app deals with displaying a list of all posts and showing an individual post. 
