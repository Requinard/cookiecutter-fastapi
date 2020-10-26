"""
This file exports a special handler for AWS Lambda functions
"""
import mangum

from api import api

handler = mangum.Mangum(
    api,
    lifespan="on",
    log_level="warning"
)
