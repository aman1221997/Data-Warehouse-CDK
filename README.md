# Automated Data Collection and Transformation Pipeline

- [Project Description](#project-description)
    - [Data Collection](#data-collection)
    - [Data Transformation](#data-transformation)
    - [CSV File Generation](#csv-file-generation)
    - [Data Storage](#data-storage)
    - [Automation and Scheduling](#automation-and-scheduling)
    - [Deployment](#deployment)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Key Benefits](#key-benefits)

## Project Description
This project involves the creation of a sophisticated Python script designed to automate the collection, transformation, and storage of data from multiple sources. The primary objectives and functionalities of the script are outlined as follows:

### Data Collection
The script retrieves data from two main sources:

- An on-premises SQL Server
- AWS Athena

### Data Transformation
After collecting the data, the script performs necessary transformations to ensure the data is in a suitable format for analysis and reporting.

### CSV File Generation
Post transformation, the data is exported and saved as a CSV file.

### Data Storage
The generated CSV file is then uploaded to an AWS S3 bucket, ensuring secure and scalable storage.

### Automation and Scheduling
This entire process is automated to run on a daily basis, ensuring up-to-date data is always available.

### Deployment
The Python script is deployed on AWS Lambda, providing a serverless environment for efficient execution. The deployment is managed using AWS Cloud Development Kit (CDK) for Python, ensuring infrastructure as code and seamless management.

## Technologies and Tools Used
- **Programming Language:** Python
- **Data Sources:** SQL Server (On-premises), AWS Athena
- **Data Storage:** AWS S3
- **Automation and Scheduling:** AWS Lambda
- **Infrastructure Management:** AWS CDK (Python)

## Key Benefits
- **Efficiency:** Automates the daily collection, transformation, and storage of data, reducing manual effort and minimizing errors.

- **Scalability:** Utilizes AWS services to ensure the solution can handle growing data volumes and complexity.

- **Reliability:** Ensures data is consistently and accurately processed and stored, providing a reliable source of truth for analysis and decision-making.


