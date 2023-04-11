import subprocess

#  Retrieve Git commit SHA
commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()

# Retrieve Git branch name
branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()

# Build Docker image
subprocess.run(['docker', 'build', '-t', f'test_app:{branch_name}-{commit_sha}', '.'], check=True)

# Tag Docker image
subprocess.run(['docker', 'tag', f'test_app:{branch_name}-{commit_sha}', f'noktos/test_app:{branch_name}-{commit_sha}'], check=True)

# Push Docker image
subprocess.run(['docker', 'push', f'noktos/test_app:{branch_name}-{commit_sha}'], check=True)
