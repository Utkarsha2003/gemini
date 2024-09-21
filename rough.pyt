import os
# from googleapiclient.discovery import build

# gemini_api_key = os.environ.get('GEMINI_API_KEY')
api_key = os.getenv("google_gemini_apikey")
print(api_key)
# def classify_questions(ques):
#     goahead_with_web_search = True  # Default to True unless overridden
    
#     device_lst = ["alarm", "reminder", "message", "call"]
#     personal_patterns = ["who are you", "what are you", "who made you"]

#     device = any(keyword in ques.lower() for keyword in device_lst)

#     if device:
#         print("api_key = "AIzaSyAtGW7OqflqGc6BivFsV4eU-_Y0LW7Y7l4" question is related to device things, which is not supported in our utku assistant")
#         goahead_with_web_search = False

#     personal_question = any(pattern in ques.lower() for pattern in personal_patterns)

#     if personal_question:
#         print("Hey, I am a Fairy, created by utku baby")
#         goahead_with_web_search = False

#     return goahead_with_web_search

# classify_questions("who are you....a fairyyy?")

# # Assuming you want to use the API key somewhere else, you can do it like this:
# if gemini_api_key:
#     service = build('geminiservice', 'v1', developerKey=gemini_api_key)
#     # Now you can use the 'service' object to make requests to the Gemini API
# else:
#     print("Gemini API key not found. Unable to authenticate requests.")
