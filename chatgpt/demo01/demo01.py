import openai

openai.organization = "org-q4K1V5Usbd1b8v7aqmHlNBaM"
openai.api_key = "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"
response = openai.Image.create(
  prompt="A fluffy white cat with blue eyes sitting in a basket of flowers, looking up adorably at the camera",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)