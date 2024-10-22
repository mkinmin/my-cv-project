# "Gemini"를 활용한 나만의 논문 번역기
Use Gemini API

## 프로젝트 소개
논문의 핵심 내용을 파악하고 요약을 효과적으로 제공하기 위해 'Gemini API'를 활용하여 구현하였습니다.

업로드된 논문에서 필요한 내용을 요약 및 번역
- 논문 요약
- 논문 Abstract 번역
- Main Contribution

### 프로젝트 기간
- 2024.09.11 ~ 2024.09.22

### 개발환경
- `Python 3.9`
- `gemini-1.5-flash`

### Repository 구성
- `config.py` : `GOOGLE_API_KEY` 등록
- `main.py` : 논문 번역 및 요약
- `requirements.txt` : 모든 패키지 .txt 파일에 포함
- `translated_result.txt` : 예시 논문 번역 및 요약 결과

### 필요 패키지 설치
다음 명령을 실행하면 모든 패키지를 한 번에 설치
    
    pip install -r requirements.txt

## 참고 및 출처
1. Gemini API 설명 : <https://ai.google.dev/gemini-api/docs/text-generation?hl=ko&lang=python>
2. pdf 파일 업로드 code : <https://medium.com/@woyera/how-i-use-gemini-on-my-pdf-files-using-python-50f4eaba4f0b>
3. 구글 AI Gemini API 사용하기 : <https://luvris2.tistory.com/880>
