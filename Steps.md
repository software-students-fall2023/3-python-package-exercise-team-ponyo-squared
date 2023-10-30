1. Make sure you've done this

    **pip install pipenv**

2. Install development dependencies

    **pipenv install --dev**

3. Create virtual environment

    __python -m venv env__

4. import **package_main.main** + the function you want to test into **_tests.py** (package/tests/_test.py) 

5. Run tests on code

    **pipenv run pytest**

I don't know if we need to include a **setup.py** file but some packages do

**main.py** is just an example function I put to get a sense of things 
