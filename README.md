# samane
## how to deploy

### local

run runserver_local.sh script for local django app

```
chown $user:$user runserver_local.sh 
chmod 755 runserver_local.sh
./runserver_local.sh 
```

run below command for docker compose 
```
docker compose -f docker-compose-local.yaml up -d
```

### server

run below command befor deploy app on server for create image file from django app

```
docker build -t samane:v1.0.0 .
```