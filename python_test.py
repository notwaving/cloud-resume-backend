import boto3
import os
import pytest
from moto import mock_dynamodb2
from lambda_function.visitor_count import lambda_handler


def test_Env():
    DEFAULT_REGION = "eu-west-2"
    os.environ['AWS_ACCESS_KEY_ID'] = 'foobar'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'foobar'
    os.environ["AWS_DEFAULT_REGION"] = DEFAULT_REGION


# @mock_dynamodb2
# def test_negative():
#     # os.environ["databaseName"] = 'ddbTableName'

#     response = lambda_handler(0, 0)
#     print("Response: ", response)

#     message = "Status code is not 200"
#     assert 200 == response['statusCode'], message


if __name__ == '__main__':
    test_Env()
    # test_negative()
return ("Everything passes")
