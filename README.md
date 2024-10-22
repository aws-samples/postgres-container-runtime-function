# PostgreSQL Container Runtime Solution

This project provides a solution for connecting AWS Lambda functions to PostgreSQL databases using custom container runtimes. It overcomes the default runtime limitations, enabling seamless integration between Lambda and PostgreSQL RDS instances.

## Overview

AWS Python Lambda functions, by default, face challenges when connecting to PostgreSQL RDS instances. While Lambda layers can extend the Python runtime with libraries to enable connections to PostgreSQL databases, the in-console code editor's runtime lacks the dependencies needed to utilize the libraries. This solution leverages custom container runtimes to include all necessary dependencies, allowing Lambda functions to establish PostgreSQL connections efficiently.

## Features

- Docker file that creates container image for AWS Lambda container runtime support
- PostgreSQL connectivity using pg8000
- Instructions to create container and deploy to AWS ECR

## Prerequisites

- AWS Account
- Docker installed on your local machine
- AWS CLI configured with appropriate permissions
- Basic knowledge of AWS Lambda and PostgreSQL

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aws-samples/postgres-container-runtime-function.git
   cd postgres-container-runtime-function
   ```

2. Build the Docker image:
   ```bash
   docker build --platform linux/amd64 -t postgres-container-runtime-function .
   ```

3. Authenticate with Amazon ECR:
   ```bash
   aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
   ```

4. Tag and push the image to ECR:
   ```bash
   docker tag postgres-container-runtime-functione:latest your-account-id.dkr.ecr.your-region.amazonaws.com/postgres-container-runtime-function:latest
   docker push your-account-id.dkr.ecr.your-region.amazonaws.com/postgres-container-runtime-function:latest
   ```

## Usage

1. Create a new Lambda function in the AWS Console.
2. Choose "Container image" as the deployment package type.
3. Select the image you pushed to ECR.
4. Configure the function's environment variables with your PostgreSQL connection details.
5. Update the function's execution role to allow access to your RDS instance.
6. Deploy and test your function.

## Configuration

Ensure you set the following environment variables in your Lambda function:

- `RDS_HOST`: Your PostgreSQL RDS endpoint
- `RDS_NAME`: RDS name
- `RDS_USER`: RDS username
- `RDS_PASSWORD`: RDS password
- `RDS_PORT`: RDS port

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- AWS Documentation on Lambda Container Images
- pg8000 project

## Support

If you encounter any problems or have any questions, please open an issue in this repository.

---

Happy coding!

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

