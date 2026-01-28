import re

def clean_corpus(chat_export_file):
    date=r"\d{1,2}/\d{1,2}/\d{2,4}"
    time=r"\d{1,2}:\d{2}(?:\s*[aApP][mM])?"
    pattern=r"^"+date+r",\s*"+time+r"\s*-\s*.+?:\s*"

    with open(chat_export_file,"r",encoding="utf-8") as f:
        lines=f.readlines()

    cleaned=[]
    for line in lines:
        msg=re.sub(pattern,"",line).strip()
        msg=re.sub(time,"",msg).strip()
        if msg and "<media omitted>" not in msg.lower():
            cleaned.append(msg)
    return cleaned

if __name__=="__main__":
    path="/home/brahmajikavya/Downloads/chat.txt"
    for m in clean_corpus(path)[:10]:
        print(m)
