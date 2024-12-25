from podcastfy.client import generate_podcast
import os 
import getpass

os.environ["OPENAI_API_KEY"] = getpass.getpass


audio_file = generate_podcast(urls=["https://es.wikipedia.org/wiki/American_Life"],
                            llm_model_name="gpt-4-turbo",
                            api_key_label="OPENAI_API_KEY",
                            conversation_config={
                                "output_language" : "es"
                            })