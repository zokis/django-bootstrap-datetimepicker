from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe
from datetime import date, datetime


class BootstrapDateTimeInput(forms.DateTimeInput):
    class Media:
        js = (
            settings.STATIC_URL + 'datepicker/js/bootstrap-datepicker.js',
        )
        lang = translation.get_language()
        lang = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang
        if lang != 'en':
            js = js + (
                settings.STATIC_URL + 'datepicker/js/locales/bootstrap-datepicker.%s.js' % lang,
            )
        js = js + (
            settings.STATIC_URL + 'bootstrap_toolkit/js/init_datepicker.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'datepicker/css/datepicker.css',
            )
        }

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            if isinstance(value, datetime):
                value = value.strftime('%d/%m/%Y %H:%M:%S')
        else:
            value = ''

        output = '''
        <div id="id_%s" class="input-append date" data-bootstrap-widget="datetimepicker">
            <input value="%s" name="%s" data-format="dd/MM/yyyy hh:mm:ss" type="text"></input>
            <span class="add-on">
                <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
            </span>
        </div>
        ''' % (name, value, name)

        return mark_safe(output)
