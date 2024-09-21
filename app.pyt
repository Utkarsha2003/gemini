import google.generativeai as genai
import os

# configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genration_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
# initialise model
model = genai.GenerativeModel("gemini-pro", generation_config=genration_config)
# generate content
response = model.generate_content(["Create a meal plan today"])


for chunk in response:
    print(chunk.text, end="", flush=True)
# Iteration over Response:

# Imagine the response as a big chunk of text coming from the AI model.
# Sometimes, the text might be too large to handle all at once. So, it's split into smaller parts called "chunks."
# The line for chunk in response: helps us go through each of these smaller parts, or chunks, one by one.
# Accessing Chunk Text:

# Now, think of each chunk like a slice of the big text pie.
# chunk.text is like taking a bite from that slice. It gives us the actual text content of each chunk.
# Printing Content:

# Printing chunk.text is like showing what's written on each slice of the pie.
# The end="" part tells Python not to start a new line after printing each slice. We want to keep showing the text on the same line.
# The flush=True part ensures that everything we print shows up immediately, without waiting. It's like saying, "Hey, show this right now!"


import google.generativeai as genai
from pathlib import Path
import os

# configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genration_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
# initialise model
model = genai.GenerativeModel("gemini-pro-vision", generation_config=genration_config)
# generate content
image_path = Path("hamster.png")
image_part = {"mime_type": "image/png", "data": image_path.read_bytes()}
prompt_parts = ["Describe what the people are doing in this image:\n", image_part]
response = model.generate_content(prompt_parts)

print(response.text)
