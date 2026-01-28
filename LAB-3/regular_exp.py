# ## 1 In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1?Group2?
import re

pattern=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
paragraph = """
Contact our offices using the following numbers.
Main office: 415-555-2671 is available during working hours.
Support center: 212-333-7890 operates 24/7.
For emergencies, dial your local emergency services.
"""
matches=pattern.finditer(paragraph)
flag=False
for match in matches:
    flag=True
    print("Match found")
    print("Group(0)->Full match:",match.group(0))
    print("Group(1)->area code:",match.group(1))
    print("Group(2)->phone number:",match.group(2))

if not flag:
    print("Nothing found in the paragarph like the given phone number")

# ##2Find website URLs that begin with http:// or https://.
paragraph2= """In today's digital world, people rely heavily on online platforms for learning, shopping,
communication, and entertainment. Many students use educational websites such as
https://www.khanacademy.org for learning mathematics and science, while others prefer
https://www.coursera.org and http://www.edx.org for university-level courses.
Developers often visit https://stackoverflow.com to solve coding problems and explore
documentation on https://docs.python.org and https://developer.mozilla.org.
For cloud services, companies depend on https://aws.amazon.com, https://azure.microsoft.com,
and https://cloud.google.com. Social media platforms like https://www.facebook.com,
https://www.twitter.com, and https://www.linkedin.com are widely used for networking and
communication. For online shopping, people frequently visit https://www.amazon.in,
https://www.flipkart.com, and https://www.ebay.com. News websites such as
https://www.bbc.com and http://www.cnn.com provide real-time updates. Cybersecurity learners
explore resources on https://owasp.org and https://tryhackme.com to improve their skills.
"""
matches=re.findall(r'https?://\S+',paragraph2)
[print(i)  for i in matches]
if not matches:
    print("no url found with the http or https protocols")

# #3Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by replacing them with dates in a single, standard format.
paragraph3="""
The project started on 3/14/2015 and the first milestone was completed on 03-14-2015.
The second phase began on 2015/3/14 and ended on 2015/03/14.
Another important update was released on 03/14/2015, while the final report was published on 2015-3-14.
Future versions may be scheduled for 4/2/2020 and 2020/4/2.
"""
pattern = r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'

def standard_format(match):
    date=match.group()
    if "/" in date:
        parts=date.split("/")
    else:
        parts=date.split("-")
    # yyyy-mm-dd format
    if len(parts[0])==4:
        year=parts[0]
        month=parts[1]
        day=parts[2]
    # mm-dd-yyyy or m/d/yyyy format 
    else:
        month=parts[0]
        day=parts[1]
        year=parts[2]
    # making month and day 2 digits 
    if len(month)==1:
        month="0"+month
    if len(day)==1:
        day="0"+day
    return year+"-"+month+"-"+day

cleaned=re.sub(pattern,standard_format,paragraph3)
print(cleaned)

# #4 How would you write a regex that matches a number with commas for every three digits? Itmust match the following
pattern=re.compile(r'\d{1,3}(,\d{3})*')

number=input("enter a number to match:")
if bool(pattern.fullmatch(number)):
    print("pattern matches")
else:
    print("pattern not matches")

# #5 How would you write a regex that matches the full name of someone whose last name isNakamoto? You can assume that the first name that comes before it will always be one wordthat begins with a capital letter.
pattern=re.compile(r'\b[A-Z][a-zA-Z]*\sNakamoto$\b')

name=input("enter a name including full name:")
if bool(pattern.fullmatch(name)):
    print("name matches")
else:
    print("name not matches")

#6 How would you write a regex that matches a sentence where the first word is either Alice, Bob,or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, orbaseballs; and the sentence ends with a period? This regex should be case-insensitive.
pattern=re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.')

sentence=input("enter a sentence:").strip()
if bool(pattern.fullmatch(sentence)):
    print("sentence matches with the given pattern")
else:
    print("sentence doesn't matches with the given pattern")

#7 Strong Password Detection Write a function that uses regular expressions to make sure thepassword string it is passed is strong. A strong password is defined as one that is at least eightcharacters long, contains both uppercase and lowercase characters, and has at least one digit.You may need to test the string against multiple regex patterns to validate its strength.

def strength_check(password):
    regex=[r'.{8,}',r'[a-zA-Z]',r'\d+',r'[^a-zA-Z0-9]']
    for p in regex:
        if not re.search(p,password):
            return False
    return True


password=input("enter a passoword to check its strongness:")

if strength_check(password):
    print("strong")
else:
    print("weak")