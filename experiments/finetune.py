from transformers import MixtralForQuestionAnswering, MixtralTokenizer, TrainingArguments, Trainer
from datasets import load_dataset
import torch

dataset = load_dataset("your_curated_dataset_name")

model = MixtralForQuestionAnswering.from_pretrained("google/mixtral-base")
tokenizer = MixtralTokenizer.from_pretrained("google/mixtral-base")

def tokenize_function(examples):
    return tokenizer(examples["question"], examples["context"], truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

training_args = TrainingArguments(
    per_device_train_batch_size=8,
    num_train_epochs=3,
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

trainer.train()
model.save_pretrained("fine_tuned_mixtral_model")
