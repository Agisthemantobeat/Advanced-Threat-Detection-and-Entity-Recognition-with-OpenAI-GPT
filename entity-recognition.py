import openai

# Set OpenAI API configurations

# openai.api_type =
# openai.api_base =
# openai.api_version =
# openai.api_key = 

def recognize_entities(text):
    # Prepare the input text for entity recognition
    prompt = f"Identify entities in the given text: '{text}'"

    # Make the API call to GPT-3.5
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    # Extract the recognized entities from the response
    recognized_entities = response.choices[0].message.content.strip()

    return recognized_entities

# Sample text for entity recognition
sample_text = "The IP address 192.168.1.1 accessed the system."

# Perform entity recognition
recognized_entities = recognize_entities(sample_text)

# Display the recognized entities
print("Recognized Entities:", recognized_entities)
