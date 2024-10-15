from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import Dataset

def tokenize_function(tokenizer, prepared_dict):
    """Tokenizes the input text for the LLM."""
    return tokenizer(prepared_dict['text'], padding='max_length', truncation=True)

def fine_tune_model(corpus, model_name='distilgpt2', output_dir='./results'):
    """Fine-tunes a pre-trained GPT-2 model using the given corpus."""
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Prepare dataset
    train_texts = {'text': corpus}
    train_dataset = Dataset.from_dict(train_texts)
    tokenized_dataset = train_dataset.map(lambda x: tokenize_function(tokenizer, x), batched=True)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=10_000,
        save_total_limit=2,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Fine-tune the model
    trainer.train()
