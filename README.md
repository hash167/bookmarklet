
- AuthenticationMiddleware: Associates users with requests using sessions
- SessionMiddleware: Handles the current session across requests
- the login() method sets the user in the session login(request, user)
- CBVs in django.contrib.auth.views
- Django provides all of above patterns by using include, path('', include('django.contrib.auth.urls')),

- Configure other authentication sources: https:// docs.djangoproject.com/en/3.0/topics/auth/customizing/#other- authentication-sources.

- Whenever you use the authenticate() function of django.contrib.auth, Django tries to authenticate the user against each of the backends defined in AUTHENTICATION_ BACKENDS one by one, until one of them successfully authenticates the user. 

- Django provides a simple way to define your own authentication backends. An authentication backend is a class that provides the following two methods:
• authenticate(): It takes the request object and user credentials as parameters. It has to return a user object that matches those credentials if the credentials are valid, or None otherwise. The request parameter is an HttpRequest object, or None if it's not provided to authenticate().
• get_user(): This takes a user ID parameter and has to return a user object.