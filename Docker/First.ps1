# Docker With redis

docker search redis

docker run -d redis

# Step:2 --- Finding Running Containers

docker ps

#The command docker inspect <friendly-name|container-id> provides more details about a running container, such as IP address.

#The command docker logs <friendly-name|container-id> will display messages the container has written to standard error or standard out.

# Step: 3 ---- Accessing Redis

# By default Redis runs on port 6379
# Jane discovers that ports are bound when containers are started using -p <host-port>:<container-port> option.

docker run -d --name redisHostPort -p 6379:6379 redis:latest

# Step:4 ---- Accessing Redis
# Jane discovers that just using the option -p 6379 enables her to expose Redis but on a randomly available port. She decides to test her theory using

docker run -d --name redisDynamic -p 6379 redis:latest

# While this works, she now doesn't know which port has been assigned. Thankfully, this is discovered via
docker port redisDynamic6379

#List all containers 
docker ps

#  Jane realises that the data stored keeps being removed when she deletes and re-creates a container. Jane needs the data to be persisted and reused when she recreates a container.

# Containers are designed to be stateless. Binding directories (also known as volumes) is done using the option -v <host-dir>:<container-dir>. When a directory is mounted, the files 
# which exist in that directory on the host can be accessed by the container and any data changed/written to the directory inside the container will be stored on the host. This allows you to upgrade or change containers without losing your data.

# Using the Docker Hub documentation for Redis, Jane has investigated that the official Redis image stores logs and data into a /data directory.

# Any data which needs to be saved on the Docker Host, and not inside containers, should be stored in /opt/docker/data/redis.

docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis

# Running A container in the foreground
# Jane has been working with Redis as a background process. Jane wonders how containers work with foreground processes, such as ps or bash.

#Previously, Jane used the -d to execute the container in a detached, background, state. Without specifying this, the container would run in the foreground. If Jane wanted to interact with the container (for example, to access a bash shell) she could include the options -it.

#As well as defining whether the container runs in the background or foreground, certain images allow you to override the command used to launch the image. Being able to replace the default command makes it possible to have a single image that can be re-purposed in multiple ways. For example, the Ubuntu image can either run OS commands or run an interactive bash prompt using /bin/bash

docker run ubuntu ps 

docker run -it ubuntu bash
