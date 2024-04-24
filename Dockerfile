# 파이썬 3.9 이미지를 기반으로 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY app.py .

# 컨테이너 실행 시 실행할 명령어
CMD ["python", "app.py"]