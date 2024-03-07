def main():
    audio_file = st.sidebar.file_uploader("Browse", type=["wav", "mp3"])
    upload_button = st.sidebar.button("Upload")

    if upload_button:
        if audio_file is not None:
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
        else:
            st.warning("Please upload an audio file.")
    else:
        st.warning("Click the 'Upload' button to upload an audio file.")

if __name__ == "__main__":
    main()
