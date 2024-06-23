import pulumi
import pulumi_docker as docker
from pulumi import ResourceOptions
from dotenv import load_dotenv
import os
from postgres import container as postgres_container
from common import network

# Load environment variables from a .env file
load_dotenv()

# Reading values from environment variables
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB')
postgres_host = os.getenv('POSTGRES_HOST')
postgrest_version = os.getenv('POSTGREST_VERSION')
container_name = os.getenv('POSTGREST_CONTAINER_NAME')
postgres_api_schemas = os.getenv('POSTGRES_API_SCHEMA_NAME')
postgres_api_anon_role = os.getenv('POSTGRES_API_ANON_ROLE')


# Create the PostgREST configuration file
postgrest_conf_content = f"""
db-uri = "postgres://{postgres_user}:{postgres_password}@{postgres_host}:5432/{postgres_db}"
db-schemas = "{postgres_api_schemas}"
db-anon-role = "{postgres_api_anon_role}"
"""

with open("postgrest.conf", "w") as f:
    f.write(postgrest_conf_content)


# Create the PostgREST Docker container
postgrest_container = docker.Container("postgrest",
    image=f"postgrest/postgrest",
    name=container_name,
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(
         name=network.name
     )],
    mounts=[docker.ContainerMountArgs(
        type="bind",
        source=os.path.abspath("postgrest.conf"),
        target="/etc/postgrest.conf",
    )],
    ports=[docker.ContainerPortArgs(
        internal=3000,
        external=3000
    )],
    command=["postgrest", "/etc/postgrest.conf"],
    opts=ResourceOptions(depends_on=[postgres_container])  # Ensure Postgres is up first
)

# # Export the PostgREST container name and URL
# pulumi.export("postgrest_container_name", postgrest_container.name)
# pulumi.export("postgrest_url", f"http://localhost:3000")
