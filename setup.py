from setuptools import setup, find_packages

CLASSIFIERS = [
    'Framework :: Django',
    'Environment :: Web Environment',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Natural Language :: Portuguese (Brazilian)',
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Marcelo Fonseca Tambalo",
    author_email="marcelo.zokis@gmail.com",
    version='1.0',
    name='django-bootstrap-datetimepicker',
    description='DateTime Picker to Django using Bootstrap Twitter and bootstrap-datetimepicker',
    url='https://github.com/zokis/django-bootstrap-datetimepicker',
    license='MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.4',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
