 # app_translation.py
import gradio as gr
from transformers import pipeline

# 지정된 모델: 영어 -> 한국어 번역 파이프라인 로드
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ko-en")

def translate_text(text_to_translate):
    if not text_to_translate.strip():
        return ""
    translated_text= translator(text_to_translate)
    return translated_text[0]['translation_text']

iface= gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter Korean text to translate..."),
    outputs=gr.Textbox(lines=5, label="번역 결과 (English)"),
    title="한-영 번역기 (opus-mt-ko-en)",
    description="Hugging Face Transformers 모델(Helsinki-NLP/opus-mt-ko-en)을 사용한 번역 앱입니다."
)
iface.launch() # 로컬 테스트용. Hugging Face Spaces는 app.py 파일을 직접 실행.