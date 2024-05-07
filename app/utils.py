from transformers import AutoTokenizer, AutoModelForCausalLM

# Load pre-trained GPT model and tokenizer
model_name = "gpt2"  # Example: "gpt2", "gpt2-medium", "gpt2-large", "gpt2-xl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_description(input_text):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    
    # Decode generated output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return generated_text
