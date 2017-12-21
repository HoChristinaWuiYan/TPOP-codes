sampleText = ("As Python's creator, I'd like to say a few words about its "+
              "origins, adding a bit of personal philosophy.\n"+
              "Over six years ago, in December 1989, I was looking for a "+
              "'hobby' programming project that would keep me occupied "+
              "during the week around Christmas. My office "+
              "(a government-run research lab in Amsterdam) would be closed, "+
              "but I had a home computer, and not much else on my hands. "+
              "I decided to write an interpreter for the new scripting "+
              "language I had been thinking about lately: a descendant of ABC "+
              "that would appeal to Unix/C hackers. I chose Python as a "+
              "working title for the project, being in a slightly irreverent "+
              "mood (and a big fan of Monty Python's Flying Circus).")

question = int(input("Choose 1 for Word frequency. Choose 2 for counting number of words in the text. Choose 3 for find out average length of word. Choose 4 for how many words of length n appear in the text."))


def wordfrequency(a):
    from collections import Counter
    sampleText = a.split()
    counts = Counter(sampleText)
    print (counts)

def countnumberofwords(a):
    sampleText = a.split()
    print (len(sampleText))

def averagelengthofwords(a):
    b = list(a)
    sampleText = a.split()
    print (len(b)/len(sampleText))

def lengthnappearingintext(a):
    sampleText = a.split()
    q = int (input("Enter the word length that you want to search for."))
    for i in range (0,120):
        length = len(sampleText[i])
        if length == q:
            print (sampleText[i])

if question==1:
    wordfrequency(sampleText)
if question==2:
    countnumberofwords(sampleText)
if question==3:
    averagelengthofwords(sampleText)
if question==4:
    lengthnappearingintext(sampleText)


