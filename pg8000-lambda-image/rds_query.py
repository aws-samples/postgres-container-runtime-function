import os
import json
import pg8000.native

def handler(event, context):
    
    # Connect to RDS instance
    try:
        conn = pg8000.native.Connection(
            host=os.environ['RDS_HOST'],
            port=os.environ['RDS_PORT'],
            database=os.environ['RDS_DB_NAME'],
            user=os.environ['RDS_USER'],
            password=os.environ['RDS_PASSWORD']
        )

        # Execute a query
        data = conn.run(
            """
            SELECT version();
            """
        ) 

        # Clean up
        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps({
                "message": "RDS connection established successfully!", 
                "response": data
            }, default=str),  
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
