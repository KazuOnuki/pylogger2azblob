# Azure Blob Logging

## Overview
This repository provides a Python logging handler, BlobStorageTimedRotatingFileHandler, that extends the functionality of the built-in TimedRotatingFileHandler. This handler automatically rotates log files at specified intervals and uploads the outdated log files to an Azure Storage Blob container. This ensures that your log history is retained in Azure Blob Storage while keeping only the latest log on the local file system.

## Files and Directory Structure
  ```txt
  .
  ├── pylogger2azblob
  │   └── handlers.py          (Main Python module with the Azure Blob Storage logging) implementation.
  ├── tests
  │   └── test_handlers.py     (Unit tests for the Azure Blob Storage logging module.)
  ├── .env                     (Configuration file for environment variables.)
  ├── requirements.txt         (File specifying the Python packages required for this project.)
  └── tutorial.py              (Tutorial script demonstrating how to use the logging functionality.)
  ```

## Installation

1. Install the required packages using the command:
    ```bash
    pip install -r requirements.txt
    ```

1. Set an .env file with the following content:
    ```dotenv
    #######################################
    # pytest settings
    #######################################
    AZURE_BLOB_TESTLOG_FILE=pytest.log
    AZURE_BLOB_TESTLOG_DIR=./tests/testlog
    AZURE_STORAGE_TESTLOG_ACCOUNT_NAME=<your-storage-account-name>

    #######################################
    # Logging settings
    #######################################
    LOGGING_ACCOUNT_NAME=<your-storage-account-name>
    LOGGING_CONTAINER=<your-container-name>
    LOGGING_LEVEL=DEBUG
    LOGGING_FORMATTER=verbose
    LOGGING_FILENAME=./output.log
    LOGGING_WHEN=S
    LOGGING_INTERVAL=1
    ```

1. (optional) If you'd like to test it, Run the tests using the command:
    ```bash
    pytest
    ```

1. (optional) Execute the tutorial script:
    ```bash
    python tutorial.py
    ```