from setuptools import setup, find_packages

setup(
    name="python_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Flask-RESTful",
        "Flask-Cors",
        "peewee"
    ],
    entry_points={
        "console_scripts": [
            "run-app=app:app"
        ]
    }
)
