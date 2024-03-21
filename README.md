## Prerequisites
- Python 3.11
- virtualenv package
```
$ python3.11 -m pip install virtualenv
```

## Setup
- Create a virtual environment in your project
```
$ python3.11 -m venv .venv
```
- Activate the virtual environment
```
$ source .venv/bin/activate
```
- Install packages
```
$ pip install -r requirements.txt
```
- Run the streamlit application using
```
$ streamlit run main.py
```