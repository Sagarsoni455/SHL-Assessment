import google.generativeai as genai
import os

# --- PASTE YOUR API KEY BELOW ---
os.environ["GOOGLE_API_KEY"] = "AIzaSyC3EgmknWvv_wgcmHMFlbE2EFZqmqZSdAo"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Checking available models for your key...\n")

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")