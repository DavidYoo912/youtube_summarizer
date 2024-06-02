import os
from openai import OpenAI

def summarize_text(text, lang='en'):
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    
    client = OpenAI(
        api_key =OpenAI.api_key,
    )
    
    prompt = f"""
            The following text is in its original language. Provide the output in this lanuage: {lang}. 
            Format the output as follows:

            Summary:
            short summary of the video

            Key Takeaways:
            succinct bullet point list of key takeaways

            input text: {text}
            """
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        #model="gpt-4-turbo", # better performance, slower inference
        )
    
    summary_text = response.to_dict()['choices'][0]['message']['content']
    return summary_text

if __name__ == "__main__":
    text_to_summarize = input("Enter the text to summarize: ")
    lang = input("Enter the language for the summary: ")
    summary = summarize_text(text_to_summarize, lang)
    print("Summary:")
    print(summary)