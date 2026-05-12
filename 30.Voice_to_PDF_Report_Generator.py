# pip install SpeechRecognition
# pip install pyaudio
# pip install word2number

import speech_recognition as sr
from reportlab.pdfgen import canvas
from word2number import w2n

# Create Recognizer and Item storage
r = sr.Recognizer()
items = []

# Listen Function
def listen():
    with sr.Microphone as source:
        print("🎙️ Speak (say 'exit' to finish)")
        audio = r.listen(source)   # Records the audio

    # Passing it to Google's speech recognizer which converts it into text
    try:
        return r.recognize_google(audio).strip()
    except:
        return ""

# Keep Listening until user says 'Exit'
while True:
    text = listen()
    if not text:   # If text is empty, keep listening (don't give Error)
        continue
    if text.lower() == "exit":
        break

    # Extract Item Name and Price
    words = text.split()
    price = ""

    for w in words:
        if w.replace(".", "").isdigit():
            price = w
            break

        if not price:   # If spoken in words
            try:
                price = str(w2n.word_to_num(text))
            except:
                price = ""

    # Clean Item Name
    item_name = " ".join(w for w in words if not w.repace(".", "").isdigit() and w.lower() != "rs".capitalize())

    # Store Item in a List
    if price:
        items.append(item_name, price)
        print(f"Added: {item_name}           Rs.{price}")
    else:
        print("Please repeat and say item with price")


# Generate PDF Report
c = canvas.Canvas("Items_Report.pdf")
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "Item-Report")
c.setFont("Helvetica-Bold", 12)
y = 770

for i, (name, price) in enumerate(items, 1):
    c.drawString(50, y, f"{i}. {name} -------------------         Rs.{price}")

    y -= 20


c.save()
print("Report PDF Saved: Items_Report.pdf")

