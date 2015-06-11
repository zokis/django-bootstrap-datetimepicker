import json
from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe
try:
    from django.utils.encoding import force_unicode as force_text
except ImportError:  # python3
    from django.utils.encoding import force_text

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
        css = {
            'all': (
                settings.STATIC_URL + 'datepicker/css/bootstrap-datetimepicker.min.css',
            )
        }

    format_map = (
        ('dd', r'%d'),
        ('HH', r'%H'),
        ('hh', r'%I'),
        ('MM', r'%m'),
        ('mm', r'%M'),
        ('ss', r'%S'),
        ('yy', r'%y'),
        ('yyyy', r'%Y'),
    )

    def __init__(self, attrs=None, format=None, options=None):
        super(BootstrapDateTimeInput, self).__init__(attrs, format)
        if options is False:
            self.options = False
        else:
            self.options = options and options.copy() or {}
            if 'language' not in self.options:
                lang = translation.get_language()
                self.options['language'] = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang
            if format and not self.options.get('format'):
                self.options['format'] = self.conv_datetime_format_py2js(format)
            elif not format and not self.options.get('format'):
                self.options['format'] = self.conv_datetime_format_py2js(DATETIME_INPUT_FORMATS)

    def conv_datetime_format_py2js(self, input_format):
        for js, py in self.format_map:
            input_format = input_format.replace(py, js)
        return input_format

    def render(self, name, value, attrs=None):
        if value:
            if DATETIME_INPUT_FORMATS:
                value = value.strftime(DATETIME_INPUT_FORMATS)
            else:
                value = value.strftime('%d/%m/%Y %H:%M:%S')
        else:
            value = ''

        html = '''
<div id="id_%(name)s" class="input-append date" data-bootstrap-widget="datetimepicker">
  <input value="%(value)s" name="%(name)s" type="text"></input>
  <span class="add-on">
    <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
  </span>
</div>''' % {'name': name, 'value': value}

        js = '''<script type="text/javascript">
 (function(window) {
  var callback = function() {
   $(function(){$("#id_%(name)s:has(input:not([readonly],[disabled]))").datetimepicker(%(options)s);});
  };
  if(window.addEventListener){window.addEventListener("load", callback, false);}
  else if (window.attachEvent){window.attachEvent("onload", callback);}
  else{window.onload = callback;}
 })(window);
</script>''' % {'name': name, 'value': value, 'options': json.dumps(self.options or {})}
        return mark_safe(force_text(html + js))
