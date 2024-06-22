# Pulumi PostgreSQL Local Deployment

This repository contains a Pulumi setup for deploying a PostgreSQL database locally using Docker. Follow the steps below to set up and verify your local PostgreSQL instance.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Pulumi: [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository, and

```bash
cd pulumi-postgres-local
```

### Step 2: Additional Setup

Initialize the Pulumi project and create a new stack:

```bash
pulumi new docker-python
pulumi stack init prod
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Copy `.env_example` to `.env` and add your own values.

### Step 3: Create the Data Directory

Create a directory on your host machine to store PostgreSQL data files:

```bash
sudo mkdir -p /path/to/your/data
sudo chown 1000:1000 /path/to/your/data  # Replace 1000:1000 with the appropriate UID:GID if necessary
```

### Step 4: Deploy the Stack

Deploy the Pulumi stack to start the PostgreSQL container:

```bash
pulumi up
```

### Step 5: Verify the Deployment

Verify that the PostgreSQL container is running:

```bash
docker ps
```

You should see a container name matching what you have in your `.env` file. If your project scope goes beyond local
deployment, you might want to consider where to put secrets and where to put other variables.

### Step 6: Connect to PostgreSQL

You can connect to the PostgreSQL instance using `psql` or any database management tool like DBeaver or pgAdmin.

#### Using psql

```bash
psql -h localhost -U your_username -d your_database
```

#### Using DBeaver

1. Open DBeaver.
2. Click on the **New Database Connection** button.
3. Select **PostgreSQL** from the list of database types.
4. Enter the connection details:
   - **Host**: `localhost`
   - **Port**: `5432`
   - **Database**: `your_database`
   - **Username**: `your_username`
   - **Password**: `your_password`
5. Click **Finish** to establish the connection.


## Conclusion

You have successfully set up a local PostgreSQL database using Pulumi and Docker. Feel free to customize the setup as needed for your projects.

---

### Notes:

- Replace `your_username`, `your_password`, `your_database`, and `/path/to/your/data` with your actual values.
- Ensure you have the correct permissions for the data directory on your host machine.



## Additional Commands

### Preview Changes

To see the changes Pulumi will apply without actually making them:

```bash
pulumi preview
```

### Destroy the Stack

To remove all resources created by Pulumi:

```bash
pulumi destroy
```