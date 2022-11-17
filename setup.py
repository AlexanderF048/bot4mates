from setuptools import setup, find_namespace_packages

setup(
    name='bot_assistant',
    version='1.0',
    description='To assist your wishes',
    url='https://github.com/kpi-donar/bot4mates.git',
    author='Bot4mates',
    author_email='https://don-ar.github.io/',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown','colorama','python-dateutil','fuzzywuzzy','python-Levenshtein'],
    entry_points={'console_scripts': ['bot-assist = bot4mates.main:main']}
)
