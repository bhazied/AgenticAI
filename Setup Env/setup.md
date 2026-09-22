# Setup a local environment

Make sur you have python installed on your machine, the version will be 3.10 or newer.
if not, try to install it : The version recomanded in this date is the 3.14 as shown bellow

![Python release cycle](https://devguide.python.org/_static/release-cycle.svg)

## Install python

#### on windows

https://www.python.org/downloads/latest/pymanager/

#### on linux

#### on mac

https://www.python.org/ftp/python/3.14.7/python-3.14.7-macos11.pkg

## create and activate a virtual environement

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

Next, create a new file named requirements.txt and copy the code provided below, or get it from [requirements.txt](requirements.txt)

```plaintext
# === Agent + LLM Tools ===
aisuite==0.1.11
anthropic
docstring-parser
markdown
mistralai
openai
qrcode
tavily-python>=0.7.12
textstat
vertexai

# === Web Framework + API ===
fastapi
pydantic
pydantic[email]
python-dotenv
python-multipart
requests
sqlalchemy
uvicorn

# === Notebook Experience ===
ipywidgets
jupyter_server
nbclassic
notebook

# === Data Analysis / Display (Optional Enhancements) ===
duckdb
matplotlib
pandas
seaborn
tabulate
tinydb

# === Machine Learning / NLP (Optional Enhancements) ===
jinja2
psycopg2-binary
scikit-learn
Wikipedia
```

finally, install all required libraries

```bash
pip install -r requirements.txt
```
and optionnaly, link this environement to your IDE or your Jupyter notebook

```bash
python -m ipykernel install --user --name=venv
```