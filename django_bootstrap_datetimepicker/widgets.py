from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe
from datetime import date, datetime


class BootstrapDateTimeInput(forms.DateTimeInput):
    class Media:
        js = (
            #settings.STATIC_URL + 'datetimepicker/js/bootstrap-datetimepicker.min.js',
            'https://raw.github.com/tarruda/bootstrap-datetimepicker/master/src/js/bootstrap-datetimepicker.js',
        )
        lang = translation.get_language().split('-')[0].lower()
        if lang == 'pt':
            js = js + (
                settings.STATIC_URL + 'datetimepicker/js/bootstrap-datetimepicker.pt-BR.js',
            )
        js = js + (
            settings.STATIC_URL + 'datetimepicker/js/init_datepicker.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'datetimepicker/css/bootstrap-datetimepicker.min.css',
            )
        }

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            value = value.strftime('%d/%m/%Y %H:%M:%S')

        output = '''
        <div id="id_%s" class="input-append date" data-bootstrap-widget="datetimepicker">
            <input value="%s" name="%s" data-format="dd/MM/yyyy hh:mm:ss" type="text"></input>
            <span class="add-on">
                <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
            </span>
        </div>
        ''' % (name, value or '', name)

        return mark_safe(output)
