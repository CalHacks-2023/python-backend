import openai

# Your DALL-E API key
openai.api_key = "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"

# The text prompt you want to use to generate an image
prompt = "Brave fighting cartoon character in desert"

# Generate an image
response = openai.Image.create(
    prompt=prompt,
    model="image-alpha-001",
    size="1024x1024",
    response_format="url"
)

# Print the URL of the generated image
print(response["data"][0]["url"])