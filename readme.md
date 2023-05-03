# NinerStudy

This is a simple image board website designed for UNCC Students to help study.

## Getting Started

### Dependencies

* Python 3.11 or higher
* MySQL 8.0 or higher

### Installing

1. Clone the repo
   ```sh
   git clone https://github.com/chris-pitre/ITSC-3155-Design-Group-19.git
   ```
2. Set up Python Virtual Environment 
   ```sh
   python -m venv venv
   ```
3. Activate Python Virtual Environment
   ```sh
   Depends on your system and shell of choice.
   Refer to python official documentation: https://docs.python.org/3/library/venv.html#how-venvs-work
   ```
4. Install Requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Run ninerstudy-schema.sql in MySQL
6. Put URI for schema in app.py at line 21
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = \
     'mysql://user:pass@host:port/ninerstudy' #IMPORTANT!!! FILL IN YOUR OWN DATABASE HERE AND RUN ninerstudy-schema.sql TO CREATE TABLE 
   ```
### Executing program

* Run Flask in terminal of your choice
   ```sh
   flask --app app run
   ```
