from distutils.core import setup

setup(
    name='BusScraper',
    version='0.2.2',
    author='Matthew Owen',
    author_email='matthew.owen95@gmail.com',
    py_modules=['busscraper'],
    packages=['test'],
    url='http://pypi.python.org/pypi/BusScraper/',
    license='LICENSE.txt',
    description='Scraper for ACIS based bus time sites',
    long_description=open('README.txt').read(),
    install_requires=[
        "httplib2",
        "BeautifulSoup"
    ],
)
