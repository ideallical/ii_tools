from setuptools import setup

setup(
    name='ii_tools',
    version='0.2',
    description='ideallical tools',
    url='https://github.com/ideallical/ii_tools',
    download_url='https://github.com/ideallical/ii_tools/archive/0.2.tar.gz',
    author='ideallical',
    author_email='info@ideallical.com',
    keywords=['string-utils', ],
    license='BSD',
    install_requires=[
        'six>=1.10.0',
    ],
    packages=['ii_tools'],
    zip_safe=False
)
