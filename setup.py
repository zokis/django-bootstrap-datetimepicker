from setuptools import setup, find_packages

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Natural Language :: Portuguese (Brazilian)',
    'Programming Language :: JavaScript',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Utilities',
]

setup(
    author="Marcelo Fonseca Tambalo",
    author_email="marcelo.zokis@gmail.com",
    version='1.1',
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
