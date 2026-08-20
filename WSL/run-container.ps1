# Run a command in a throwaway container
wslc run --rm -it ubuntu:latest bash -c "echo Hello world from WSL container!"

# Run a web server in the background and publish port 8080 to the container's port 80
wslc run -d --rm -p 8080:80 --name web nginx

# Request content from the running web server
curl http://localhost:8080

# List the running container
wslc container list

# Run an additional command inside the running container
wslc exec web cat /etc/os-release

# Stop the container
wslc container stop web