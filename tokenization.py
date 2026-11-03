import tiktoken

# Load a tokenizer
encoding = tiktoken.get_encoding("o200k_base")

text = "Prominent figures such as Marcus Aurelius, Seneca, and Epictetus expanded these teachings into a practical framework for living, emphasizing that lasting tranquility (eudaimonia) arises from aligning one’s will with nature and reason. Far from emotional suppression, Stoicism encourages the transformation of destructive passions into clear-headed judgment, using techniques like negative visualization and daily reflection to prepare for adversity and appreciate the present moment."

# Convert text into token IDs
token_ids = encoding.encode(text)

# Convert token IDs back into token strings
tokens = [
    encoding.decode_single_token_bytes(token_id).decode(
        "utf-8", errors="replace"
    )
    for token_id in token_ids
]

print("Original text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
print("Token count:", len(token_ids))

# Decode the token IDs back into text
decoded_text = encoding.decode(token_ids)
print("Decoded text:", decoded_text)
