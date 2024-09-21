# step 1
def ask_question():
    ques = "Hey " + name + " what do you want ? - "
    ques = input(ques)
    return ques


def classify_questions(ques):
    goahead_with_web_search = False
    device_lst = ["alarm", "reminder", "message", "call"]
    personal_patterns = ["who are you", "what are you", "who made you", "are you a"]

    device = False
    for i in device_lst:
        if i in ques.lower():
            device = True

    if device:
        print(
            "This question is realted to device things, which is not supported in our utku assistant"
        )

    personal_question = False
    for i in personal_patterns:
        if i in ques.lower():
            personal_question = True
            break

    if personal_question:
        print("Hey, I am a Fairy, created by utku baby")

    if device:
        goahead_with_web_search = False
    elif personal_question:
        goahead_with_web_search = False
    else:
        goahead_with_web_search = True

    return goahead_with_web_search


# start searching with google gemini
import google.generativeai as genai
import os

# configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genration_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
# initialise model
model = genai.GenerativeModel("gemini-pro", generation_config=genration_config)

# text to speech
# from gtts import gTTS

# tts = gTTS("hello")
# tts.save("audio.mp3")
# diap

# from playsound import playsound
# playsound("audio.mp3")


# generate content
def ask_gemini(ques):
    response = model.generate_content(ques)
    text_parts = []
    for part in response.parts:  # Iterate through parts of the response
        if part.text:  # Check if the part has text content
            text_parts.append(part.text)  # Append text content to list

    # Combine text parts into a single string
    combined_text = "".join(text_parts)
    print(combined_text, end="", flush=True)
    return combined_text


have_any_other_ques = "y"
name = ""
while have_any_other_ques == "y":
    if name == "":
        name = input("Hey what is your name ? - ")

    q = ask_question()

    go_ahead = classify_questions(q)
    answer = ""
    if go_ahead == True:
        answer = ask_gemini(q)

    print(answer)

    have_any_other_ques = input("Do you have any other questions? - ")
