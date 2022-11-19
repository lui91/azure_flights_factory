import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from secrets import get_connection_string

try:
    connection_string = get_connection_string()
    blobServiceClient = BlobServiceClient(connection_string)
    containerClient = blobServiceClient.GetBlobContainerClient("file_sharing")
    print("Azure Blob Storage Python quickstart sample")

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)


