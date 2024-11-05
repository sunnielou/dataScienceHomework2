from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:mathQuiz',
        ],
    },
    author="Alisson Licona Beltrán",
    author_email="ali.licona@fau.de",
    description="Math quiz game based on Data Science Survival Skills Homework 2",
    license="Apache License 2.0",
    url="https://github.com/sunnielou/dataScienceHomework2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)