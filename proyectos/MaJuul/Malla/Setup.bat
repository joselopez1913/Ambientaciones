@echo off
env_malla\Scripts\activate && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt && python gen_password.py
pause


