from distutils.core import setup

setup(
    name='BusScraper',
    version='0.1.0',
    author='Matthew Owen',
    author_email='matthew.owen95@gmail.com',
    packages=['busscraper', 'busscraper.test'],
    url='http://pypi.python.org/pypi/BusScraper/',
    license='LICENSE.txt',
    description='Scraper for ACIS based bus time sites',
    long_description=open('README.txt').read(),
    install_requires=[
        "urllib",
        "httplib2",
        "BeautifulSoup"
    ],
)