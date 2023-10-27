import openai

openai.organization = ""
openai.api_key = ""
response = openai.Image.create(
  prompt="A fluffy white cat with blue eyes sitting in a basket of flowers, looking up adorably at the camera",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
