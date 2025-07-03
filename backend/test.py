from google.generativeai import configure, GenerativeModel

# Authenticate with your API key
configure(api_key="AIzaSyCypmLLEcanWRm9AXUQK6WQPi3M31R_fgI")

# Choose the model
model = GenerativeModel('gemini-1.5-flash')

# Generate content
response = model.generate_content("Explain how AI works in a few words")

# Print the response
print(response.text)
