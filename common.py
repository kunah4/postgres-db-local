import pulumi_docker as docker

# Ensure both containers are on the same network
network = docker.Network("postgres-db-network")