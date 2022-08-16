# :information_desk_person: Mongo server in a :whale: Docker container

## :point_right:Introduction

- This is a simple project to help my classmates out using a lighter server-like instead of a VM that is way heavier.
- So, this came because some of us don't have a fast ethernet connection and downloading heavy stuff it takes many hours or days indeed!

## :exclamation: Make sure that

1. You have [docker](https://docs.docker.com/get-docker/) previously installed 
2. You have docker with [rootless permission](https://docs.docker.com/engine/security/rootless/) or at least with access
3. You have *python 3* already configured in your PATH (Just run a `` python3 --version `` to test it)
4. You better execute the **run.py** in a linux-like O.S. (From now only tested in Linux)


## :bulb: How use it

1. Clone this repository in a local directory
2. Set your working directory in the root of the project where **run.py** is at 
  - ``cd docker4mongodb-dam2-m6-uf3/``
3. Execute the script
  - `` python3 run.py``
4. Wait until it says ``All data is imported!``
5. Now the mongo server is up and all data loaded within!

- If you restart the computer, or it happens anything like the container is not running ( `docker ps`) you should **start** it again
> $ docker start mongodb_dam2
- Another option if you don't have any container yet created (only this one). It just starts all the containers you have built.
> $ docker start \`docker ps -a\`

Finally, you just need to use your client to connect to ``localhost`` and the default port for mongo ``27017``

I do recommend using a simple one like [nosqlbooster](https://nosqlbooster.com/downloads) because it quite simple and powerful.



## :point_right: Directories explanation

- **root**
    - The ``*s_*`` files you can find there are scripts from mongodb to [load or import data](https://docs.mongodb.com/manual/reference/program/mongoimport/).
    - example from file _s_cityInspect_:            
          ``mongoimport -d  cityInspec -c cityInspec db/cityInspec/city_inspections.json --drop --stopOnError --maintainInsertionOrder``


- **db**
    - All the databases files with **json** files, and some **bson** to back them up with the mongo import scripts in _root_.
 
