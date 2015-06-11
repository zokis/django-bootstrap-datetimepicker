from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe

from datetime import date, datetime


DATETIME_INPUT_FORMATS = getattr(settings, 'DATETIME_INPUT_FORMATS', None)
if DATETIME_INPUT_FORMATS:
    DATETIME_INPUT_FORMATS = DATETIME_INPUT_FORMATS[0]


class BootstrapDateTimeInput(forms.DateTimeInput):

    class Media:
        js = (
            settings.STATIC_URL + 'datepicker/js/bootstrap-datetimepicker.min.js',
        )
        lang = translation.get_language()
        lang = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang
        if lang != 'en-US':
            js = js + (
                settings.STATIC_URL + 'datepicker/js/locales/bootstrap-datetimepicker.%s.js' % lang,
            )
        js = js + (
            settings.STATIC_URL + 'datepicker/js/init_datepicker.js',
        )
        css = {
            'all': (
                settings.STATIC_URL + 'datepicker/css/bootstrap-datetimepicker.min.css',
            )
        }

    format_map = (
        ('dd', r'%d'),
        ('MMMM', r'%B'),
        ('MMM', r'%b'),
        ('MM', r'%m'),
        ('yyyy', r'%Y'),
        ('yy', r'%y'),
        ('HH', r'%H'),
        ('hh', r'%I'),
        ('mm', r'%M'),
        ('ss', r'%S'),
    )

    def conv_datetime_format_py2js(self, input_format):
        for js, py in self.format_map:
            input_format = input_format.replace(py, js)
        return input_format

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            if isinstance(value, datetime):
                if DATETIME_INPUT_FORMATS:
                    value = value.strftime(DATETIME_INPUT_FORMATS)
                else:
                    value = value.strftime('%d/%m/%Y %H:%M:%S')
        else:
            value = ''
        return mark_safe('''
            <div id="id_%s" class="input-append date" data-bootstrap-widget="datetimepicker">
              <input value="%s" name="%s" type="text" data-format="%s"></input>
              <span class="add-on">
                <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
              </span>
            </div>
            ''' % (name, value, name, self.conv_datetime_format_py2js(DATETIME_INPUT_FORMATS))
        )
