# Download last mongo version image
FROM mongo:latest

LABEL mantainer="hikager"
# "cd" to our new container directory
WORKDIR /dam2/mongodb
# copy all the directory to docker current dir
COPY /mongo_databases ./
# Allowing to exec the script in the container
RUN ["chmod", "+x", "./script.sh"]

