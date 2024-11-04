import subprocess

# Read subdirectories from 'dirs.txt'
with open('dirs.txt', 'r') as file:
    directories = file.readlines()

# Strip newlines and spaces from each directory name
directories = [dir_name.strip() for dir_name in directories]

# Define the base command
base_command = 'aws --endpoint-url http://challenge.ctf.games:30714 s3 ls s3://bucket/{} --no-sign-request'

# Iterate over each directory and execute the command
for dir_name in directories:
    command = base_command.format(dir_name)
    print(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error running command for {dir_name}: {e.stderr.decode('utf-8')}")
