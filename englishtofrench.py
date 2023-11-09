from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

def translate_english_to_french(text):
    # Explicitly specify the T5 model and tokenizer
    model_name = "t5-base"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    # Set legacy=False and install protobuf for the new behavior
    tokenizer = T5Tokenizer.from_pretrained(model_name, model_max_length=1024, legacy=False)

    # Tokenize and translate the text
    inputs = tokenizer("translate English to French: " + text, return_tensors="pt")
    # Set max_new_tokens to control the maximum length of the generation
    translation_ids = model.generate(**inputs, max_new_tokens=1024)
    translated_text = tokenizer.batch_decode(translation_ids, skip_special_tokens=True)[0]

    return translated_text

# Get input from the user
english_text = input("Enter English text to translate to French: ")

# Translate the input
french_translation = translate_english_to_french(english_text)

# Display the results
print(f"\nEnglish Text: {english_text}")
print(f"French Translation: {french_translation}")
