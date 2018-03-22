import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Package dependencies
install_requires = [
    'wagtail>=1.8',
]

# Testing dependencies
testing_extras = [
]

# Documentation dependencies
documentation_extras = [
]

setup(
    name='wagtailcommonblocks',
    version='0.1',
    packages=['commonblocks'],
    include_package_data=True,
    license='MIT',
    description='Common StreamField blocks for Wagtail',
    long_description=README,
    url='https://github.com/springload/wagtailcommonblocks/',
    author='Springload',
    author_email='hello@springload.co.nz',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)
