import os
from openai import OpenAI

def summarize_text(text):
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    
    client = OpenAI(
        api_key =OpenAI.api_key,
    )
    
    prompt = f"""                
            understand the language of the input text, generate an output in the same language in the following format

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
    )
    
    summary_text = response.to_dict()['choices'][0]['message']['content']
    return summary_text

if __name__ == "__main__":
    text_to_summarize = input("Enter the text to summarize: ")
    summary = summarize_text(text_to_summarize)
    print("Summary:")
    print(summary)