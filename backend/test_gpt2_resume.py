from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_dir = "./gpt2_resume_finetuned"
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained(model_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

prompt = """Summary:
Experienced Python developer with expertise in FastAPI and SQL, seeking opportunities to build scalable backend systems.

Skills:
- Python
- FastAPI
- SQL

Experience:
- """

inputs = tokenizer(prompt, return_tensors="pt", padding=True).to(device)

outputs = model.generate(
    inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=60,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=False,
)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

print("\n✅ Generated Resume:\n")
print(generated_text)
