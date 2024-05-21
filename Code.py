import pandas
from pydub import AudioSegment
from gtts import gTTS                          #gtts means 'google text-to-speech'

def textToSpeech(text,filename):               #Converts the string "str" into an audio and stores the audio into the file "filename"
    s = str(text)                              #Converts the text into string because the text can contain integers, float numbers, etc...
    audio=gTTS(text=s,lang="hi",slow=False)
    audio.save(filename)

def merge_audios(audios):                      #Takes a list of names of component audios as an input and merges them into a single audio
    final=AudioSegment.empty()                 #Initialize the combined audio with an emtpty audio
    for audio in audios:
        final+=AudioSegment.from_mp3(audio)    #"AudioSegment.from_mp3(MP3 File)" is the audio content of the mp3 file in argument
    return final

def break_audio():                             #Breaks the audio "Announcement.mp3" into component audios (or skeleton audios)
    audio = AudioSegment.from_mp3("Announcement.mp3")

    #Generate "Kripya dhyan dijiye"
    audio[0:1500].export("1.mp3",format="mp3") #"AudioSegment" allows slicing of audios 
    #Generate "Se chalkar"
    audio[2750:4300].export("3.mp3",format="mp3")
    #Generate "Ke raaste"
    audio[5500:6500].export("5.mp3",format="mp3")
    #Generate "Ko jaane vaali gaadi sankhya"
    audio[7500:10500].export("7.mp3",format="mp3")
    #Generate "Kuch hi samay me platform sankhya"
    audio[15500:18000].export("9.mp3",format="mp3")
    #Generate "Par aa rahi hai dhanyavaad"
    audio[18500:21500].export("11.mp3",format="mp3")

def generate_announcement(filename):           #Takes an excel file as an input and uses the data in it to create mp3 announcement files for each row of the excel sheet
    train_list = pandas.read_excel(filename)   #The excel file is stored in the variable "df"
    print(train_list)

    for index,item in train_list.iterrows():   #"Index" iterates over rows
        textToSpeech(item["From"],"2.mp3")     #"item["Column"]" gives the data stored in the column named "Column" for the row number "index"
        textToSpeech(item["Via"],"4.mp3")
        textToSpeech(item["To"],"6.mp3")
        textToSpeech(item["Train No."] + " " + item["Train Name"],"8.mp3")
        textToSpeech(item["Platform"],"10.mp3")

        audios = [f"{i}.mp3" for i in range(1,12)] #A list containing the names of all componnet audios from "1.mp3" to "11.mp3".
        announcement = merge_audios(audios)
        announcement.export(f"Announcement_{index+1}.mp3",format="mp3") #Separate announcements are generated for each row of the input excel sheet

if __name__=="__main__":

    print("Generate skeleton.....")
    break_audio()

    print("Generating announcement.....")
    generate_announcement("Announcement.xlsx")

"""
 This Railway Announcement System allows you to make the following announcements about the train feeded in the excel sheet:
 1. The train Number
 2. The train Name
 3. The place the train is coming from (Source)
 4. The place where the train is going (Destination)
 5. The place the train will pass through (Via)
 6. The platform number on which the train is arriving
 """