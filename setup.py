from setuptools import find_packages, setup
import re
import os
import io
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

MODULE = 'authentication_dummy'
PREFIX = 'trytoncalidae'
MODULE2PREFIX = {}


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (
        name, major_version, minor_version,
        major_version, minor_version + 1
    )
    return require


config = ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
version = info.get('version', '0.0.1')
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res)(\W|$)', dep):
        prefix = MODULE2PREFIX.get(dep, 'trytond')
        requires.append(get_require_version('%s_%s' % (prefix, dep)))
requires.append(get_require_version('trytond'))

tests_require = []
dependency_links = []
if minor_version % 2:
    # Add development index for testing with proteus
    dependency_links.append('https://trydevpi.tryton.org/')

setup(
    name='%s_%s' % (PREFIX, MODULE),
    version=version,
    description='Authenticate without password',
    long_description=read('README.md'),
    author='Calidae',
    author_email='dev@calidae.com',
    url='https://github.com/calidae/',
    download_url="https://github.com/calidae/%s" % MODULE,
    keywords='',
    package_dir={'trytond.modules.%s' % MODULE: '.'},
    packages=[
        'trytond.modules.%s' % MODULE,
    ] + [
        'trytond.modules.%s.%s' % (MODULE, p)
        for p in find_packages()
    ],
    package_data={
        'trytond.modules.%s' % MODULE: (
            info.get('xml', [])
            + [
                'tryton.cfg',
            ]
        ),
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Hungarian',
        'Natural Language :: Italian',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Russian',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business',
        ],
    license='GPL-3',
    install_requires=requires,
    extras_require={
        'test': tests_require,
    },
    dependency_links=dependency_links,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    %s = trytond.modules.%s
    """ % (MODULE, MODULE),
)
