import json

def lambda_handler(event, context):
    # 요청 본문 파싱
    body = json.loads(event['body'])
    
    # 요청 처리 로직 작성
    response_body = {
        'message': 'Hello, Lambda!',
        'input': body
    }
    
    # 응답 반환
    response = {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
    
    return response