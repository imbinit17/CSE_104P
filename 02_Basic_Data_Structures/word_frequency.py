# Create a program that counts frequency of each word in a given text

def count_words(text : str):
    p1,p2 = 0,0
    freq = {}

    word = ''
    while(p2<len(text)):
        ch = text[p2]

        if ch==' ' and p2==p1+1 :
            p1=p2
            p2+=1 
            continue
        
        elif ch==' ' and p2!=p1+1:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
            word = ''
            p1 = p2
            p2+=1

        elif ord(ch)<97 or ord(ch)>122:
            p2+=1
            continue

        elif ord(ch)>=97 and ord(ch)<=122:
            word+=ch
            p2+=1

        
    print('Frequency of words in the given text :')
    for word in freq:
        print(f'{word} : {freq[word]}')

print('Enter a sentence')
text = str(input())
text = text.lower()
text = text.strip()

count_words(text)

