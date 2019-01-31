# Docker - Deploy Static HTML Website as container

# Step 1 - Create Dockerfile
# Docker Images start from a base image. The base image should include the platform dependencies required by your application, for example, having the JVM or CLR installed.

# This base image is defined as an instruction in the Dockerfile. Docker Images are built based on the contents of a Dockerfile. The Dockerfile is a list of instructions describing how to deploy your application.

# In this example, our base image is the Alpine version of Nginx. This provides the configured web server on the Linux Alpine distribution.

FROM nginx:alpine
COPY . /usr/share/nginx/html
# The first line defines our base image. The second line copies the content of the current directory into a particular location inside the container.


# Step 2 -- Build Docker Images
# The Dockerfile is used by the Docker CLI build command. The build command executes each instruction within the Dockerfile. The result is a built Docker Image that can be launched and run your configured app.
# The build command takes in some different parameters. The format is docker build -t <build-directory>. The -t parameter allows you to specify a friendly name for the image and a tag, commonly used as a version number. This allows you to track built images and be confident about which version is being started.

docker build -t webserver-image:v1 . 

# The built image will have the name webserver-image with a tag of v1.

# to check all images which are currently 
docker images

# Step 3 - Run
# The built Image can be launched in a consistent way to other Docker Images. When a container launches, it's sandboxed from other processes and networks on the host. When starting a container you need to give it permission and access to what it requires.

# For example, to open and bind to a network port on the host you need to provide the parameter -p <host-port>:<container-port>.

# Launch our newly built image providing the friendly name and tag. As it's a web server, bind port 80 to our host using the -p parameter.

docker run -d -p 80:80 webserver-image:v1

# Once started, you'll be able to access the results of port 80

# You now have a static HTML website being served by Nginx.