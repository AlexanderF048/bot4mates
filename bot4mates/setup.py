from setuptools import setup

setup(
    name='bot_assistant',
    version='1.0',
    description='To assist your wishes',
    url='https://github.com/kpi-donar/Bot_Assistant.git',
    author='Bot4mates',
    author_email='https://don-ar.github.io/',
    license='MIT',
    packages=['bot4mates'],
    entry_points={'console_scripts': ['bot_assist = bot4mates.main:main']}
)