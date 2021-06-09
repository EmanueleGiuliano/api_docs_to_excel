# APIDOCS TO EXCEL

This script reads your api-docs file and produces an excel with the format specified in the first lines, feel free to edit and improve it according to your needs.

## prerequisites
python 2.7+
pip

## before run
i suggest using virtual env, then you have to install this dependency:  xlsxwriter

1. install virtualenv (skip if u already have it) --> pip install virtualenv
2. run -->virtualenv json_to_excel (this creates your virtualenv)
3. run  --> json_to_excel\Scripts\activate (on windows, this activates virtual env)
4. run --> pip install xlsxwriter
5. use the tool
6. when you are done run --> deactivate

#### usage
	python main.py [path-of-apidocs-file.json] [api-environment] [microservice-name] [excel-file-name]

#### example
	python main.py ./api-docs.json DEVELOPMENT core-cruscotto cruscotto-api