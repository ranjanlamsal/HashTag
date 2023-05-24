from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("Ranjan22/TextToTagGenerator")
tokenizer = AutoTokenizer.from_pretrained("Ranjan22/TextToTagGenerator")

def Generatetag(text: str):
    """ Generates tags from given text """
    text = text.strip().replace('\n', '')
    text = 'tag: ' + text
    tokenized_text = tokenizer.encode(text, return_tensors="pt")

    tags_ids = model.generate(tokenized_text,
                                        num_beams=4,
                                        no_repeat_ngram_size=2,
                                        max_length=20,
                                        early_stopping=True)

    output = tokenizer.decode(tags_ids[0], skip_special_tokens=True)
    return output.split(', ')

Generatetag("This is a sample text to generate tags from it")