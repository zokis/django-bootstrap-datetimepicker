django-bootstrap-datetimepicker
===============================

DateTime Picker to Django using [Bootstrap Twitter](http://twitter.github.com/bootstrap/ "Bootstrap") and [bootstrap-datetimepicker](http://tarruda.github.com/bootstrap-datetimepicker/ "datetimepicker")


This package uses Bootstrap v2.x datetimepicker widget provided by the following project:
 http://tarruda.github.com/bootstrap-datetimepicker/

It works only with Bootstrap2.x. If you are using Bootstrap3 in your Django project, 
visit https://github.com/nkunihiko/django-bootstrap3-datetimepicker/


Install
-------------------------------

* Run `pip install django-bootstrap-datetimepicker`
* Add `'django_bootstrap_datetimepicker'` to your `INSTALLED_APPS`


Example
--------------------------------

###### forms.py
```python
from django import forms
from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput

class ToDoForm(forms.Form):
    todo = forms.CharField()
    date = forms.DateTimeField(
        widget=BootstrapDateTimeInput()
    )
    reminder = forms.DateTimeField(
        widget=BootstrapDateTimeInput()
    )
```
###### template.html
```html
<!DOCTYPE HTML>
<html>
  <head>
    <link
        href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap.min.css"
        rel="stylesheet">
    {{ form.media.css }}
  </head>
  <body>
    {{ form }}
    <script type="text/javascript"
     src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js">
    </script> 
    <script type="text/javascript"
     src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js">
    </script>
    {{ form.media.js }}
  </body>
<html>
```
