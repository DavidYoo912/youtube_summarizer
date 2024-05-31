import streamlit as st
from scrape_youtube import extract_video_id, get_transcript, extract_metadata, download_thumbnail
from summarize_text import summarize_text
import os

def main():
    #st.title("YouTube Transcript Summarizer")
       
    # Define the title text and image URL
    title_text = "YouTube AI Summarizer"
    image_url = "https://i.pinimg.com/originals/3a/36/20/3a36206f35352b4230d5fc9f17fcea92.png"  # Replace this URL with your image URL

    # Use HTML and CSS to style the title and image
    html_code = f"""
    <div style="display: flex; align-items: center; margin-bottom: 30px;">
        <img src="{image_url}" alt="Tiny Image" style="width: 50px; height: 50px; margin-right: 15px;">
        <h3 style="font-size: 45px;">{title_text}</h3>
    </div>
    """

    # Display the HTML code using markdown
    st.markdown(html_code, unsafe_allow_html=True)
    
    def get_thumbnail_from_url(url):
        video_id = extract_video_id(url)
        download_thumbnail(video_id)
    
    # Function to get transcript from URL
    def get_transcript_from_url(url):
        video_id = extract_video_id(url)
        transcript = get_transcript(video_id)
        return transcript

    # Function to summarize text
    def summarize_transcript(transcript):
        summary = summarize_text(transcript)
        return summary

    # Interface components
    st.subheader("Enter YouTube URL:")
    st.write("Paste a YouTube link to summarize its content (must have a transcript available)")
    url = st.text_input("URL")

    if st.button("Summarize"):
        if url:
            # After Button is Clicked
            # Display Title and Channel Names
            title, channel = extract_metadata(url)
            st.subheader("Title:")
            st.write(title)
            st.subheader("Channel:")
            st.write(channel)
            
            # Display Thumbnail
            get_thumbnail_from_url(url)
            st.image(os.path.join(os.getcwd(), "thumbnail.jpg"), caption='Thumbnail', use_column_width=True) 
            
            # Display Summary
            transcript = get_transcript_from_url(url)
            summary = summarize_transcript(transcript)
            st.subheader("Video Summary:")
            st.write(summary)
        else:
            st.warning("Please enter a YouTube URL.")

if __name__ == "__main__":
    main()
