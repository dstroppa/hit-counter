FROM python:3.5-onbuild
EXPOSE 5000
CMD [ "gunicorn", "app:app", "-b", "0.0.0.0:5000" ]
