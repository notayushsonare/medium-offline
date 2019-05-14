# Import required modules
import requests, bs4

# Get the topic to download from user
list = ['comics', 'books', 'art', 'culture', 'film', 'food', 'gaming', 'humor', 'internet-culture', 'lit', 'medium-magazine', 'music', 'photography', 'social-media', 'sports', 'style', 'true-crime', 'tv', 'writing', 'business', 'design', 'economy', 'startups', 'freelancing', 'leadersip', 'marketing', 'productivity', 'work', 'artificial-intelligence', 'blockchain', 'cryptocurrency', 'cybersecurity', 'data-science', 'gadgets', 'javascript', 'macine-learning', 'math', 'neuroscience', 'programming', 'science', 'self-driving-cars', 'software-engineering', 'space', 'technology', 'visual-design', 'addiction', 'creativity', 'disability', 'family', 'health', 'mental-health', 'parenting', 'personal-finance', 'pets', 'psychedelics', 'psychology', 'relationships', 'self', 'sexuality', 'spirituality', 'travel', 'wellness', 'basic-income', 'cities', 'education', 'environment', 'equality', 'future', 'gun-control', 'history', 'justice', 'language', 'lgbtqia', 'media', 'masculinity', 'philosophy', 'politics', 'race', 'religion', 'san-francisco', 'transportation', 'women', 'world']
print('Welcome to Medium aricle downloader by @CoolSonu39!')
choice = 'some-random-topic'
print('Which domain do you want to read today?')
while choice not in list:
    print("Enter 'list' to see the list of topics.")
    choice = input('Enter your choice: ')
    if choice == 'list':
        print()
        for i in list:
            print(i)
        print()
    elif choice not in list:
        print('\nTopic' + choice + 'not found :(')
    
print()
# Parse homepage to gather list of article links
print('Getting latest article links from %s...' % (choice))
tlink = 'https://medium.com/topic/' + choice
medres = requests.get(tlink)
medres.raise_for_status()
medbs = bs4.BeautifulSoup(medres.text, features='lxml')
artelem = medbs.select('h3 > a')
print('Total articles found: ' + str(len(artelem)))

for i in range(len(artelem)):
    heading = artelem[i].getText()
    artlink = 'https://medium.com' + artelem[i].get('href')
    print('Downloading article: ' + str(i+1))
    file = open(heading + '.txt', 'w')
    file.write(heading + '\n\n\n')

    # Go through each article link & write text in files
    artres = requests.get(artlink)
    artbs = bs4.BeautifulSoup(artres.text, features='lxml')
    arttext = artbs.find_all(['p', 'blockquote'])

    for j in range(len(arttext)):
        file.write(arttext[j].getText() + '\n\n')
    file.close()

print('Done.')
