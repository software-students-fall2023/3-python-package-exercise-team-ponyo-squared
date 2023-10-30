1. Make sure you've done this

    __pip install pipenv__

2. Install development dependencies

    __pipenv install --dev__

3. Create virtual environment

    __python -m venv env__

4. import __package_main.main__ + the function you want to test into ___tests.py__ (package/tests/_test.py) 

5. Run tests on code

    __pipenv run pytest__


I don't know if we need to include a __setup.py__ file but some packages do

__main.py__ is just an example function I put to get a sense of things 
