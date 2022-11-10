from setuptools import setup

setup(
    name='bot_assistant',
    version='1.0',
    description='To assist your wishes',
    url='https://github.com/kpi-donar/Bot_Assistant.git',
    author='Dream_Team',
    author_email='https://don-ar.github.io/',
    license='MIT',
    packages=['bot_ass'],
    entry_points={'console_scripts': ['bot-assist = bot_ass.main:main']}
)