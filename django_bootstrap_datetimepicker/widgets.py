from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe

from datetime import date, datetime


DATETIME_INPUT_FORMATS = getattr(settings, 'DATETIME_INPUT_FORMATS', None)
if DATETIME_INPUT_FORMATS:
    DATETIME_INPUT_FORMATS = DATETIME_INPUT_FORMATS[0]


TIME_INPUT_FORMATS = getattr(settings, 'TIME_INPUT_FORMATS', None)
if TIME_INPUT_FORMATS:
    TIME_INPUT_FORMATS = TIME_INPUT_FORMATS[0]


class BootstrapDateTimeInput(forms.DateTimeInput):
    class Media:
        js = (
            settings.STATIC_URL + 'datepicker/js/bootstrap-datetimepicker.min.js',
        )
        lang = translation.get_language()
        lang = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang
        if lang != 'en-US':
            js = js + (
                settings.STATIC_URL + 'datepicker/js/locales/bootstrap-datepicker.%s.js' % lang,
            )
        js = js + (
            settings.STATIC_URL + 'datepicker/js/init_datepicker.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'datepicker/css/bootstrap-datetimepicker.min.css',
            )
        }

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

        output = '''
        <div id="id_%s" class="input-group date" data-bootstrap-widget="datetimepicker">
            <input class="form-control" value="%s" name="%s" type="text"></input>
            <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
        </div>
        ''' % (name, value, name)

        return mark_safe(output)


class BootstrapTimeInput(forms.TimeInput):
    class Media:
        js = (
            settings.STATIC_URL + 'datepicker/js/bootstrap-timepicker.js',
        )

        js = js + (
            settings.STATIC_URL + 'datepicker/js/init_timepicker.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'datepicker/css/bootstrap-timepicker.min.css',
            )
        }

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            if isinstance(value, datetime):
                if TIME_INPUT_FORMATS:
                    value = value.strftime(TIME_INPUT_FORMATS)
                else:
                    value = value.strftime('%H:%M')
        else:
            value = ''

        output = '''
        <div class="input-append bootstrap-timepicker">
            <input id="id_%s" value="%s" name="%s" type="text" class="form-control">
            <span class="add-on"><i class="icon-time"></i></span>
        </div>

        ''' % (name, value, name)

        return mark_safe(output)
