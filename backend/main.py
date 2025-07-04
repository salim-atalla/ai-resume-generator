from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class ResumeRequest(BaseModel):
    prompt: str

# Load the fine-tuned GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2_resume_finetuned")
model = GPT2LMHeadModel.from_pretrained("./gpt2_resume_finetuned")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.post("/generate-resume")
async def generate_resume(data: ResumeRequest):
    prompt = data.prompt
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = model.generate(
                inputs,
                max_length=200,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                pad_token_id=tokenizer.eos_token_id,
                do_sample=True,
                top_k=30,
                top_p=0.9,
                temperature=0.8
            )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"resume": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
