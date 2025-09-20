from google import genai
from google.genai import types

def generate(history):
    client = genai.Client(
        api_key="[API_KEY]"
    )

    model = "gemini-2.0-flash"
    contents=history
    tools = [
        types.Tool(google_search=types.GoogleSearch())
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""you are a personalized learning assistant that focuses on asking good and new questions and explaining topics with ease of understanding. you need to focus on clarity and accuracy of information. generate using only ascii characters"""),
        ],
    )
    s=''
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        s+=chunk.text
    return s


if __name__ == "__main__":
    user=input('User: ')
    history=[types.Content(role="user",parts=[types.Part.from_text(text=user),],)]
    while user!='Quit':
        out=generate(history)
        history+=[types.Content(role="model",parts=[types.Part.from_text(text=out)])]
        print()
        print('AthenAI:',out)
        user=input('User: ')
        if user!='Quit':
            history+=[types.Content(role="user",parts=[types.Part.from_text(text=user)])]
