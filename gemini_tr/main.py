import os
import textwrap
import google.generativeai as genai
from PyPDF2 import PdfReader
from google.cloud import storage

import pathlib
import textwrap
 
import google.generativeai as genai
 
from IPython.display import display
from IPython.display import Markdown
from config import Config
 
# 서식이 지정된 Markdown 텍스트를 표시하는 함수
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
 
# 제미나이 API 키 설정
genai.configure(api_key=Config.GOOGLE_API_KEY)

# 모델 설정
model = genai.GenerativeModel('gemini-1.5-flash')  # 텍스트 전용 모델 

# '파일' 폴더에 있는 PDF 파일 경로
file_path = "C:/Users/kimin/cv-project/my-cv-project/gemini_tr/paper/시계열 데이터 분석을 위한 SAR영상 비교기법 연구.pdf"

sample_file = genai.upload_file(path=file_path, display_name="Attention paper summary")

# 업로드 확인
print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

# PDF 파일에서 텍스트 추출
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# 제미나이 API를 이용하여 텍스트 번역
def find_title(text):
    prompt = f"find the title of this paper: {text}"
    response = model.generate_content(prompt)
    return response.text

def summarize_paper(text):
    prompt = f"Summarize the following text into Korean: {text}"
    response = model.generate_content(prompt)
    return response.text

def translate_abstract(text):
    prompt = f"Translate the abstract in the following text in Korean: {text}"
    response = model.generate_content(prompt)
    return response.text

def translate_contribution(text):
    prompt = f"Translate the main contribution of the following text in Korean: {text}"
    response = model.generate_content(prompt)
    return response.text

def save_to_markdown_file(title,summarized_text, abstract, main_contribution, file_name="translated_result.txt"):
    # text형식으로 만들기
    text_content = f"{title}\n\n{summarized_text}\n\n{abstract}\n\n{main_contribution}"
    
    # Write to a text file
    with open(file_name, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text_content)
    
    print(f"Markdown content saved to {file_name}")

# PDF 파일에서 텍스트를 추출하고 번역
pdf_text = extract_text_from_pdf(file_path)
Title = find_title(pdf_text)
Summarized_text = summarize_paper(pdf_text)
Abstract = translate_abstract(pdf_text)
Main_contribution = translate_contribution(pdf_text)

# 번역된 결과를 Markdown 형식으로 출력
display(to_markdown(Title))
display(to_markdown(Summarized_text))
display(to_markdown(Abstract))
display(to_markdown(Main_contribution))

# 결과물을 .txt 파일에 저장
save_to_markdown_file(Title,Summarized_text, Abstract, Main_contribution)