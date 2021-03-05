# GCP-PUBSUB
POSTGRESQL DB CREATION
----------------------
1.Creating a PostgreSQL instance

gcloud sql instances create INSTANCE_NAME --database-version=POSTGRES_12
 --cpu=NUMBER_CPUS --memory=MEMORY_SIZE
 --region=REGION --gce-zone=GCE_ZONE --zone=ZONE
 
2.Creating a database
gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]
[--charset=CHARSET] [--collation=COLLATION]

3. Need to Enable Cloud ADMIN API 

PUBSUB TOPIC  AND CLOUD FUNCTION CREATION
=========================================

1. Creating a topic

gcloud pubsub topics create MY_TOPIC # Create a Pub/Sub topic
2. Creating a functions and publish the message
gcloud functions deploy MY_FUNCTION  --trigger-topic MY_TOPIC  --runtime python37 # Deploy a Function with a Pub/Sub trigger
gcloud pubsub topics publish MY_TOPIC --message '{ "greeting": "Hello" }'
