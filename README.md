# TacticalBoardPlanner
Tactical board for games like rainbow six siege. 
Inspired by:
1. Lack of planning within tactical games
2. Lack of support for current solutions.

Commands when starting docker:
1. docker-compose up -d -> runs docker file detached
2. python
3. from database.data import *
4. init_db() -> create the database tables
5. exit()
6. docker volume ls -> check that database is created after running python init command
7. docker ps -> list containers to get id
8. docker exec -ti containerID bash -> go into container with bash

Postgres Commands:
1. psql -U postgres
2. \dt -> list tables to confirm creation

Images stored on linode buckets:
1. Follow s3cmd guide: https://www.linode.com/docs/platform/object-storage/how-to-use-object-storage/#s3cmd
2. Make images public