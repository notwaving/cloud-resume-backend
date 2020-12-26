import boto3
import os
import pytest
from moto import mock_dynamodb2
from lambda_function.visitor_count import lambda_handler
