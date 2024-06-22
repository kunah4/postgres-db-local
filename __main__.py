import pulumi
import pulumi_docker as docker
from dotenv import load_dotenv
import os


# Load environment variables from a .env file
load_dotenv()

# Reading values from environment variables
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB')
postgres_version = os.getenv('POSTGRES_VERSION')
data_path = os.getenv('DATA_PATH')
container_name = os.getenv('CONTAINER_NAME')

# Create a Docker Volume for data persistence
volume = docker.Volume("pgdata")

# Create the Postgres Docker container
container = docker.Container("postgres",
    image=f"postgres:{postgres_version}",
    name=container_name,
    envs=[
        f"POSTGRES_USER={postgres_user}",
        f"POSTGRES_PASSWORD={postgres_password}",
        f"POSTGRES_DB={postgres_db}",
    ],
    mounts=[docker.ContainerMountArgs(
        type="bind",
        source=data_path,
        target="/var/lib/postgresql/data",
    )],
    ports=[docker.ContainerPortArgs(
        internal=5432,
        external=5432
    )],
)

# Export the container name
pulumi.export("container_name", container.name)