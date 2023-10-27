

1. Make sure you've done this
pip install pipenv

2. Install development dependencies
pipenv install --dev 

3. Create virtual environment
python -m venv env

4. After importing <i> package_main.main <i> to <i> _tests.py <i> (in the tests directory), run tests on code
pipenv run pytest


I don't know if we need to include a <span>setup.py</span> file but some packages do

<span>main.py</span> is just an example function I put to get a sense of things 