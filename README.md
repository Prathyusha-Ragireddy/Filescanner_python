Script is written in python3

# Running as script:

python3 filescanner.py <filepath>

Note: default filepath will be current directory

# Build as docker container:
# (.) Takes the Dockerfile in the current directory and builds the image with the tag name fielscanner

docker build -t filescanner .

# logs the changed to filescan.log in the tmp folder

docker run -dit -v $(pwd)/tmp:/tmp/filescanner/tmp -v $(pwd)/filescan.log:/var/log/filescan.log --name filescanner filescanner

# To check the logs

docker logs -f filescanner
