# Lambda PostgreSQL Container Solution

This project provides a solution for connecting AWS Lambda functions to PostgreSQL databases using custom container runtimes. It overcomes the default runtime limitations, enabling seamless integration between Lambda and PostgreSQL RDS instances.

## Overview

AWS Lambda functions, by default, face challenges when connecting to PostgreSQL RDS instances. This solution leverages custom container runtimes to include all necessary dependencies, allowing Lambda functions to establish PostgreSQL connections efficiently.

## Features

- Custom Docker container for AWS Lambda
- PostgreSQL connectivity using pg8000
- Easy deployment to AWS Lambda
- Scalable and maintainable serverless database operations

## Prerequisites

- AWS Account
- Docker installed on your local machine
- AWS CLI configured with appropriate permissions
- Basic knowledge of AWS Lambda and PostgreSQL

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/lambda-postgres-container.git
   cd lambda-postgres-container
   ```

2. Build the Docker image:
   ```bash
   docker build --platform linux/amd64 -t lambda-postgres-image .
   ```

3. Authenticate with Amazon ECR:
   ```bash
   aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
   ```

4. Tag and push the image to ECR:
   ```bash
   docker tag lambda-postgres-image:latest your-account-id.dkr.ecr.your-region.amazonaws.com/lambda-postgres-image:latest
   docker push your-account-id.dkr.ecr.your-region.amazonaws.com/lambda-postgres-image:latest
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

- `DB_HOST`: Your PostgreSQL RDS endpoint
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password

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

