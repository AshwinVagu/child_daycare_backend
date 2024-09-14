# child_daycare_backend

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
anshul@Anshuls-MacBook-Air childCareBackend % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 18, 2024 - 22:48:26
Django version 4.1.13, using settings 'childCareBackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[18/Feb/2024 22:48:30] "GET / HTTP/1.1" 200 10681
[18/Feb/2024 22:48:30] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[18/Feb/2024 22:48:30] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[18/Feb/2024 22:48:30] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[18/Feb/2024 22:48:30] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
^C%                                                                                                                                                
anshul@Anshuls-MacBook-Air childCareBackend % python3 manage.py migrate  
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
This version of djongo does not support "NULL, NOT NULL column validation check" fully. Visit https://nesdis.github.io/djongo/support/
  Applying contenttypes.0001_initial...This version of djongo does not support "schema validation using CONSTRAINT" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying auth.0001_initial...This version of djongo does not support "schema validation using KEY" fully. Visit https://nesdis.github.io/djongo/support/
This version of djongo does not support "schema validation using REFERENCES" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name...This version of djongo does not support "COLUMN DROP NOT NULL " fully. Visit https://nesdis.github.io/djongo/support/
This version of djongo does not support "DROP CASCADE" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK