import time

def transcribe_audio_with_retry(audio_file_path, max_retries=3, delay_seconds=2):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempting transcription (Attempt {attempt} of {max_retries})...")
            transcribed_text = transcribe_audio(audio_file_path)
            return transcribed_text
        except Exception as ex:
            print(f"Error: {str(ex)}")
            print(f"Retrying in {delay_seconds} seconds...")
            time.sleep(delay_seconds)

    raise Exception("Max retries reached. Unable to transcribe audio.")

def main():
    if audio_file and upload_button:
        try:
            temp_audio_path = "temp_audio.wav"
            with open(temp_audio_path, "wb") as f:
                f.write(audio_file.read())

            transcribed_text = transcribe_audio_with_retry(temp_audio_path)
            sentiment_label, sentiment_score = perform_sentiment_analysis(transcribed_text)

            st.header("Transcribed Text")
            st.text_area("Transcribed Text", transcribed_text, height=200)
            st.header("Sentiment Analysis")
            # ... (rest of your code)

        except Exception as ex:
            st.error("Error occurred during audio transcription and sentiment analysis.")
            st.error(str(ex))
            traceback.print_exc()

        finally:
            os.remove(temp_audio_path)

if __name__ == "__main__":
    main()
