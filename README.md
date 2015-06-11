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
    from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput
    from django import forms
    
    class ToDoForm(forms.Form):
        todo = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"}))
        date = forms.DateTimeField(
            widget=BootstrapDateTimeInput()
        )
        reminder = forms.DateTimeField(
            widget=BootstrapDateTimeInput()
        )

###### template.html
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/2.3.2/css/bootstrap.css">
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.js">
            </script>
            <script src="//netdna.bootstrapcdn.com/bootstrap/2.3.2/js/bootstrap.js">
            </script>
            {{ form.media }}
        </head>
        <body>
            <form method="POST">
                {% csrf_token %}
                {% for field in form.visible_fields %}
                <div id="div_{{ field.html_name }}" class="form-group{% if field.errors %} has-error{% endif %}">
                    {{ field.label_tag }}
                    {{ field }}
                    <div class="text-muted pull-right">
                        <small>{{ field.help_text }}</small>
                    </div>
                    <div class="help-block">
                        {{ field.errors }}
                    </div>
                </div>
                {% endfor %}
                {% for hidden in form.hidden_fields %}
                    {{ hidden }}
                {% endfor %}
                <div class="form-actions">
                  <button type="submit" class="btn btn-primary">Save changes</button>
                  <button type="button" class="btn">Cancel</button>
                </div>
            </form>
        </body>
    </html>
