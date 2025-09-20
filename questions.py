from google import genai
from google.genai import types


def generate(topic):
    client = genai.Client(
        api_key=("[API_KEY]"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=topic),
            ],
        ),
    ]
    tools = [
        types.Tool(google_search=types.GoogleSearch())
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""you give every user a quiz with 2 questions in the chapter as a python list in the form [(Question,[options],answer key as index)], use only ascii characters"""),
        ],
    )

    s=''
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        s+=chunk.text
    
    ind=s.index('=')
    endInd=s.index('```',ind)
    l=(eval((s[ind+1:endInd-1])))
    return l

#print(generate('thermodynamics for chemistry'))
