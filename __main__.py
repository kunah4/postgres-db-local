import pulumi
from postgres import container as postgres_container
from postgrest import postgrest_container


# --- note: This file will import the PostgreSQL and PostgREST modules and run the stack.

# Exporting outputs
pulumi.export("PostgreSQL Container Name", postgres_container.name)
pulumi.export('PostgREST Container Name', postgrest_container.name)
pulumi.export('PostgREST URL', f"http://localhost:3000")

# pulumi.export('postgrest_url', postgrest_container.ports[0].external.apply(lambda port: f"http://localhost:{port}"))
