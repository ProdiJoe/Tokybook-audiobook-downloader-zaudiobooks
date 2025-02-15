import os , requests , re
from bs4 import BeautifulSoup
from tqdm import tqdm

# Replace with the actual audiobook page URL
book_url = "https://tokybook.com/divergence"

# Fetch the audiobook page
response = requests.get(book_url)
soup = BeautifulSoup(response.text, "lxml")

# Extract audiobook title
book_title = soup.find("div",{"class":"inside-page-hero grid-container grid-parent"}).find("h1").text.strip()
book_title = re.sub(r'[<>:"/\\|?*]', "_", book_title)
print(f"downloading {book_title}")
# make a folder with book title
os.makedirs(f"{book_title}", exist_ok=True)

# Find chapter MP3 links 
chapter_links = []
for script in soup.find_all("script"):
    if "chapter_link_dropbox" in script.text:
        for line in script.text.split("\n"):
            if "chapter_link_dropbox" in line and ".mp3" in line:
                url = line.split('"')[3]
                welcom_url = "https://file.tokybook.com/upload/welcome-you-to-tokybook.mp3"
                if not url.startswith("https://files02.tokybook.com/audio/") and url !=welcom_url:
                    url = "https://files02.tokybook.com/audio/"+url.replace(" ","%20").replace('\\',"/")
                if url!=welcom_url:
                    chapter_links.append(url)
                    
# enumerate returns the value and its index (index start at 1 in this case)                    
for i,link in enumerate(chapter_links,start=1): 
    file_name = os.path.join(book_title,f"chapter {i:02}.mp3")
    chap_response = requests.get(link,stream=True)
    chap_size = int(chap_response.headers.get("content-length",0))
    
    if chap_response.status_code == 200:
        # creates file with chapter name and opens it in write binary mode (to be able to write none-text files)
        # and creates a progress bar with correct units
        with open(file_name,"wb") as f , tqdm(total=chap_size,unit="B"
                                              ,unit_scale=True,unit_divisor=1024
                                              ,desc=f"downloading chapter {i:02}.mp3:") as progress:
            # reads the mp3 file from the link in a 1 MB chunks
            for chunk in chap_response.iter_content(chunk_size=2**20):
                f.write(chunk)
                progress.update(len(chunk)) 
    else : print(f"failed to download {link} : {chap_response}")

print("All chapters downloaded!")
