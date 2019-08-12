Script is written in python3

Add all the files on to your /(root) folder before running the below commands.

# Running as script:

python3 filescanner.py <filepath>

Note: default filepath will be current directory

# Build as docker container:

docker build -t filescanner .

Note : (.) Takes the Dockerfile in the current directory and builds the image with the tag name filescanner

# Run teh container in detached mode and logs the changes to filescan.log in the tmp folder

docker run -dit -v $(pwd)/tmp:/tmp/filescanner/tmp -v $(pwd)/filescan.log:/var/log/filescan.log --name filescanner filescanner

# To check the logs

docker logs -f filescanner

--------------------------------------------------------------------------------
# Logs & output png
 
The left terminal shows the output of before and after modififations in the folder.
Right teminal shows how the changes are logged in when modifications are made. 
