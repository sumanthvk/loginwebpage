# loginwebpage
This is a Python Flask based web application with Mongo DB, which allows a user to login and logout. Once a user is logged in, the application saves the user session in a cookie so that the user does not have to login if he visits the web app again. The cookie is cleared at logout.

When a user tries to login on the home page, it checks if the user is registered and the credentials are valid. 
If it's a valid request, user is taken to the login page where the user stays logged and the cookie is in session. The user will stay logged in until he logs out and then the coookie is cleared. 
Suppose if the authentication is failed, a new page opens up indicating that the account is not found and he will be redirected to the registeration page. The new user can register here and is automatically logged in. This data will be saved in the database succesfully.
