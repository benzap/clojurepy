#!/usr/bin/env python

from setuptools import setup


setup(name='cljpy',
      version='0.0.1',
      description='Clojure in the Python VM',
      author='Benjamin Zaporzan',
      author_email='benzaporzan@gmail.com',
      url='https://github.com/benzap/clojurepy',
      packages=['cljpy', 'tests', 'doc'],
      package_data={"cljpy": ['data/*',],
                    "doc": ['*.org', '*.html'],},
      entry_points={
          'console_scripts': [
              'cljpy = cljpy.__main__:main',
              ]
      },
      test_suite='nose.collector',
      install_requires=[
          'nose',
          'funcy',
      ],
      tests_require=['nose'],
     )
