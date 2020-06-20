import pytest
from lambda_function import lambda_handler
import json

def test_lambda ():
    res_api = lambda_handler("event", "context")
    assert res_api["statusCode"] == 200

