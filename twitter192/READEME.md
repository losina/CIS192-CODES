### Twitter 192

To run the app
'''
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
'''

    path('accounts/', accounts, name='accounts'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup_view, name='signup_view'),
    path('like/', like, name='like'),
    path('unlike/', unlike, name='unlike'),
    path('delete/', delete, name='delete'),
    path('profile/', profile, name='profile'),
    path('hashtag/', hashtag, name='hashtag'),
    path('', splash, name='splash'),

You can access the Twitter page via ```http://localhost:8000/```
Click "Log In or Create Account"
Signing up, you will be redirected to the main splash page of 192 Twitter.
You can make new tweets with hashtags and delete ones you've created. 
Clicking on the username of each tweet or the hashtag, you can filter the list of tweets. 

####Routes Description
'/login' url takes in username and password and changes the request user to be authenticated.
'/signup' url takes in username, password and email to create new user.
'/' POST request for this url creates new tweet
'/delete?=id' takes in the tweet id and removes the tweet 
'/like?=id' or '/unlike?=id' takes in the tweet id and creates or removes a "Like" object connecting the user and the tweet.
'/profile?=username' takes in the username and displays only the tweets made by the certain user. 
'/hashtag?=hashtag' takes in the hashtag and displays only the tweets with that tags
