from setuptools import setup

setup(
    name='lektor-gulp',
    version='0.1',
    author=u'Maurizio Turatti',
    author_email='maurizio@softinstigate.com',
    description=u'A simple Lektor plugin for gulp',
    url = "https://github.com/SoftInstigate/lektor-gulp",
    license='BSD',
    py_modules=['lektor_gulp'],
    entry_points={
        'lektor.plugins': [
            'gulp = lektor_gulp:GulpPlugin',
        ]
    }
)
