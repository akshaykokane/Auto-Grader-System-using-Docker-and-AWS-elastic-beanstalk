# Instructions copied from - https://hub.docker.com/_/python/
FROM python:3-onbuild

# tell the port number the container should expose
EXPOSE 5000

#Give exe permission
RUN chmod 777 test.sh

# run the command
CMD ["python", "./app.py"]
