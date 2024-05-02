import re

def custom_tokenizer(query_string):
    
    pattern = r"'([^']+)'"
    
    # Use re.findall() to find all matches
    matches = re.findall(pattern, query_string)
    
    # Return the list of matched words
    return matches

def dename_tokenizer(text):
    # Pass 1: Remove the word "name" from the input text
    text_without_name = re.sub(r"name", "", text)
    text_without_name = re.sub(r"''","",text_without_name)
    text_without_name = re.sub(r"this.","this'",text_without_name)
    text_without_name = re.sub(r"length","'length'",text_without_name)
    # Pass 2: Tokenize using regular expressions
    pattern_quotes = r"'(?:[^']|'')*'"
    tokens = re.findall(pattern_quotes, text_without_name)
    

    # Pass 3: Handle curly braces and colons
    processed_tokens = []
    for token in tokens:
        if token.startswith("'"):
            processed_tokens.append(token)
        else:
            processed_tokens.extend(re.split(r"([{}:])", token))

    # Remove empty strings from the list
    processed_tokens = [t for t in processed_tokens if t != ""]

    return processed_tokens