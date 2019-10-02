
from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/zachattack_0111/titanic_datascience',
    author='Zach nguyen',
    author_email='nguyenngochaiizz@gmail.com', 
    license='MIT',
    packages=['titanic'],
)

setup(
	...
    install_requires=[
		...
        'pytest>=4.3.1',
        'pytest-runner>=4.4',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

setup(
    ...
    install_requires=[
        ...
        'click>=7.0'
    ],
	...
    entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
)