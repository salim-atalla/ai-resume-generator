from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_dir = "./gpt2_resume_finetuned"
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained(model_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Improved prompt for structured generation
prompt = "Summary:\nExperienced Python developer with expertise in FastAPI and SQL, seeking opportunities to build scalable backend systems.\n\nSkills:\n"

inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
attention_mask = torch.ones_like(inputs)

outputs = model.generate(
    inputs,
    attention_mask=attention_mask,
    max_length=300,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.7
)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\nGenerated Resume:\n")
print(generated_text)
