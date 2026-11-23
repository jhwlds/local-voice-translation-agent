import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "facebook/nllb-200-distilled-600M"
DEVICE = "mps"

print("Loading NLLB...")
tokenizer = AutoTokenizer.from_pretrained(MODEL, src_lang="eng_Latn")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL).to(DEVICE)
model.eval()

text = "Hello, my name is Howon. This is a test for my machine translation project."

inputs = tokenizer(text, return_tensors="pt").to(DEVICE)

with torch.inference_mode():
    output = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("kor_Hang"),
        max_new_tokens=128,
    )

translation = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

print("English:", text)
print("Korean:", translation)