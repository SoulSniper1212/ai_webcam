import cv2
import base64
import io
from PIL import Image
from google import generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

def send_to_gemini(image_base64, prompt, history):
    """Send image and prompt to Gemini API and receive the response."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        full_prompt = ""
        for item in history:
            full_prompt += f"{item['role'].capitalize()}: {item['content']}\n"
        full_prompt += f"User: {prompt}"
        response = model.generate_content([full_prompt, image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

def capture_image(cap):
    """Capture a single frame from the webcam and return its base64 encoding."""
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Could not capture image from webcam.")
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer).decode('utf-8')

def main():
    cap = cv2.VideoCapture(0)
    conversation_history = []
    image_base64 = None
    print("Non-GUI AI Assistant CLI")
    print("Commands: \n 1: Capture Photo and Analyze\n 2: Ask Question\n 3: Exit")

    while True:
        cmd = input("Select command (1/2/3): ").strip()
        if cmd == '1':
            try:
                image_base64 = capture_image(cap)
                prompt = "Describe what you see in this image in a couple sentences."
                conversation_history.clear()
                conversation_history.append({"role": "user", "content": prompt})
                response = send_to_gemini(image_base64, prompt, conversation_history)
                conversation_history.append({"role": "assistant", "content": response})
                print("AI:")
                print(response)
            except Exception as e:
                print(f"Error: {e}")

        elif cmd == '2':
            if not image_base64:
                print("No photo captured yet. Please use command 1 first.")
                continue

            use_prev = input("Use previous photo? (y/n): ").strip().lower()
            if use_prev not in ('y', 'n'):
                print("Invalid choice, assuming 'y'.")
                use_prev = 'y'

            if use_prev == 'n':
                try:
                    image_base64 = capture_image(cap)
                except Exception as e:
                    print(f"Error: {e}")
                    continue

            prompt = input("Enter your question: ").strip()
            if not prompt:
                print("Empty prompt. Please enter a valid question.")
                continue

            conversation_history.append({"role": "user", "content": prompt})
            response = send_to_gemini(image_base64, prompt, conversation_history)
            conversation_history.append({"role": "assistant", "content": response})
            print("AI:")
            print(response)

        elif cmd == '3':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please select 1, 2, or 3.")

    cap.release()

if __name__ == '__main__':
    main()
