from google import genai
client = genai.Client(api_key="AIzaSyAVXewDhBkwh9kNkGp-YPrn-VbaNYKmZDc")
for model in client.models.list():
    print(model.name)