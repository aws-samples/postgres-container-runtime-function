FROM public.ecr.aws/lambda/python:latest

# Copy reqs file into dockerfile
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install requirements
RUN pip install -r requirements.txt

COPY rds_query.py ${LAMBDA_TASK_ROOT}

CMD ["rds_query.handler"]