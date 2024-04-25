import sys
def handler(event, context):
    return 'Goodbye from AWS Lambda using Python' + sys.version + '!'