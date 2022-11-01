docker build -t vehicle-ml-build .
docker run -d -p 80:80 --name vehicle-api vehicle-ml-build
