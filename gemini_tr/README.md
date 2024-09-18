# My Own Paper Translator with Gemini
Use Gemini API

## 프로젝트 소개
Gemini를 활용한 나만의 논문 번역기

업로드된 논문에서 필요한 내용을 요약 및 번역
- 논문 요약
- 논문 Abstract 번역
- Main Contribution

### 개발환경
- `Python 3.9`
- `gemini-1.5-flash`

### Repository 구성
- `config.py` : `GOOGLE_API_KEY` 등록
- `main.py` : 논문 번역 및 요약
- `requirements.txt` : 모든 패키지 .txt 파일에 포함
- `translated_result.txt` : 예시 논문 번역 및 요약 결과


다음 명령을 실행하면 모든 패키지를 한 번에 설치
    
    pip install -r requirements.txt