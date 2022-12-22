import openai, os

openai.api_key = ''

running_prompt = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
Human: """

def generate_prompt(prompt):

    global running_prompt
    
    running_prompt += prompt + "\nAI: "
    
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=running_prompt,
            temperature=0.8,
            max_tokens= 2049,
        )

    running_prompt += response.choices[0].text + '\nHuman: '
    return response.choices[0].text.replace('\n\n','',1).replace('\n\n','\n')


    
    
