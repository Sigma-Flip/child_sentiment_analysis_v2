import torch
import whisperx
import json
from pathlib import Path
import gc
from tqdm import tqdm
'''
mp3파일 넣으면 json 파일로 output_dir 경로에 transcription.json으로 저장합니다. 
모델은 tiny, base, large,,,etc 있음. 
'''

def process_audio_with_whisperx(input_file, output_dir):
    # GPU 장치 설정
    device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if torch.cuda.is_available() else "int8"
    
    # 모델 로드 (작은 모델로 변경: base 모델)
    model = whisperx.load_model("tiny", device, compute_type=compute_type, language="ko")
    
    # 오디오 파일 로드 및 변환
    audio = whisperx.load_audio(input_file)
    result = model.transcribe(audio, batch_size=16)

    # 정렬 모델 로드 및 적용
    model_a, metadata = whisperx.load_align_model(language_code="ko", device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    # JSON으로 변환할 데이터 생성
    json_result = {
        "audio_file": str(input_file),
        "segments": result["segments"]
    }
    
    # GPU 메모리 정리
    if device == "cuda":
        torch.cuda.empty_cache()
        gc.collect()

    # JSON 파일로 저장
    output_file = Path(output_dir) / f"{Path(input_file).stem}_transcription.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_result, f, ensure_ascii=False, indent=2)

    return str(output_file)


process_audio_with_whisperx("/Users/dongwoo/Desktop/yaj_renewal/user_audio/광화문자생한방병원_1.mp3", "/Users/dongwoo/Desktop/yaj_renewal/user_audio")
