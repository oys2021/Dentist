from django.apps import AppConfig


class FitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fit'

# Does your mobile app need to save anything specific to users?
# Does your app need to display dynamic data that is based on user behavior
# Does your app have to authenticate a user?
# Does the app have admin-driven configuration functionality?

# It is the database that makes an application or website dynamic. Whenever any user makes a request from the app, the database accepts the query, processes the query, fetches the data, and gives it to the app user. The database is also responsible to accept new data and edit the old data, as desired by the user.
# https://www.masteringbackend.com/posts/backend-development-the-ultimate-guide
# https://enlear.academy/roadmap-for-your-mobile-app-development-process-e167e3659723