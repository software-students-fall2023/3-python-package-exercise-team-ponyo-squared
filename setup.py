from setuptools import setup, find_packages

setup(
    name="runtimeponyo",
    version="0.0.3",
    description="A package that allows the user to record and print out neatly the runtime of functions and also the entire program.",
    author="Aaron Stein, Alex Hmitti, Rafael Nadal-Scala, Jhon Kim",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.4" # standard ones like functool and time are already included in python
    ],
    entry_points={
        "console_scripts": [
            "runtimeponyo = runtimeponyo.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
