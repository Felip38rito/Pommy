''' Setup do Pommy '''

from setuptools import setup

setup(
    name = "Pommy",
    version = "0.1.0",
    author = "Felipe Brito",
    author_email = "felip38rito@yahoo.com",
    packages = ["pommy"],
    url = "https://github.com/Felip38rito/Pommy",
    license = "MIT LICENSE",
    description = "Simple pomodoro solution implemented in python",
    long_description = open('README.md').read(),
    keywords = ["pomodoro", "productivity"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)