# TacticalBoardPlanner
Tactical board for games like rainbow six siege. 
Inspired by:
1. Lack of planning within tactical games
2. Lack of support for current solutions.

Starting database with docker-compose:
1. ```docker-compose up -d``` (runs dockers detached)
2. ```python```
3. ```from app.database.db import init_db()```
4. ```init_db()``` (create the database tables)
5. ```exit()```
6. ```docker volume ls``` (check that database is created after running python init command)
7. ```docker ps``` (list containers to get id)
8. ```docker exec -ti <containerID> bash``` (go into container with bash)

Postgres Commands:
1. ```psql -U postgres```
2. `````\dt````` (list tables to confirm creation)

To run local server uvicorn with command from src/app/ directory (same command used to start within docker):
> uvicorn run:app --reload --host 0.0.0.0 --post 8080

Build image with docker file:
> docker build -t **image-name** **path/to/dir**

Run docker image and go into it:
> docker run -it -p 8080:8080 **image-name** /bin/sh
>
*Network must be specified when database and flask app ran in container to
allow them to communicate and be given hostname*

To find network (usually ends in default when created by docker-compose):
> docker network ls

Specify network when running image: 
> --net tacticalboardapi_default

Images stored on linode buckets:
1. Follow s3cmd guide: https://www.linode.com/docs/platform/object-storage/how-to-use-object-storage/#s3cmd
2. Make images public
