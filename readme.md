# Gunicorn cmd to python files 
    1. file where is server file is written 
    gunicorn -w 1 -b 0.0.0.0:8000 wsgi:server
