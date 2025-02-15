# **TokyoBook Audiobook Downloader**  

This script allows you to **automatically download** audiobook chapters from [TokyoBook](https://tokybook.com/) in one go.  
It extracts `.mp3` chapter links from a given audiobook page and downloads them into a **folder named after the book**.  

---

## **📥 Features**  
✅ Supports **TokyoBook.com** audiobooks  
✅ Creates a folder **named after the book**  
✅ Extracts and downloads **all chapters automatically**  
✅ Displays a **progress bar** while downloading  

---

## **🚀 How to Use**  

### **1️⃣ Install Requirements**  
Make sure you have Python **3.12+** installed. Then, install dependencies:  
```sh
pip install requests beautifulsoup4 tqdm
```

### **2️⃣ Update `book_url`**  
In `main.py`, replace the URL with the **audiobook page URL** from TokyoBook:  
```python
book_url = "https://tokybook.com/providence-the-beginning-after-the-end-book-11"
```

### **3️⃣ Run the Script**  
Simply execute the script:  
```sh
python main.py
```
The chapters will be downloaded into a **folder named after the audiobook**.

---

## **🔍 How It Works**
1. **Scrapes the audiobook page** to get the book title and chapter links.  
2. **Creates a folder** named after the audiobook.  
3. **Downloads each chapter** as an `.mp3` file with a progress bar.  

---

## **📌 Notes**
- The script **only works with** [TokyoBook](https://tokybook.com/) audiobooks.  
- Chapter filenames are saved as **`chapter 1.mp3`, `chapter 2.mp3`, etc.**  
- If the book title contains **invalid characters**, they will be replaced automatically.  
- If you **re-run the script**, it may overwrite existing files if they already exist in the folder.  

---

### **👨‍💻 Author**  
Developed with ❤️ using Python. Contributions and suggestions are welcome!  
