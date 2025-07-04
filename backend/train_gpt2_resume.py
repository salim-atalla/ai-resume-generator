from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import os

# Load tokenizer and GPT-2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")

def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size
    )

# Ensure dataset exists
dataset_path = "resume_dataset.txt"
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"{dataset_path} not found. Please create and fill it with resume samples before training.")

train_dataset = load_dataset(dataset_path, tokenizer)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

training_args = TrainingArguments(
    output_dir="./gpt2_resume_finetuned",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2,
    logging_steps=50,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

trainer.train()

trainer.save_model("./gpt2_resume_finetuned")
tokenizer.save_pretrained("./gpt2_resume_finetuned")

print("Fine-tuning complete! Your GPT-2 model is saved in './gpt2_resume_finetuned' and ready for FastAPI generation.")
