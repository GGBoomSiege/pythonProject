import pyttsx3,PyPDF2
total_text = ''
pdfreader = PyPDF2.PdfReader(open('story.pdf','rb'))
speaker = pyttsx3.init()
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()  ## extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')  ## Removes unnecessary spaces and break lines
    print(cleaned_text)                ## Print the text from PDF
    total_text += cleaned_text
    #speaker.say(cleaned_text)        ## Let The Speaker Speak The Text
speaker.save_to_file(total_text,'story.mp3')  ## Saving Text In a audio file 'story.mp3'
speaker.runAndWait()
speaker.stop()