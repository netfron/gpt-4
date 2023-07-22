import os
import openai
openai.organization = "org-kcokGpa7Tp6j3f1BwVlZXCo6"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
