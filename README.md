# 🎵 Day 21 - Custom Playlist with Dunder Methods

Hey there! 👋  
Welcome to **Day 21** of my **#30DaysOfPythonChallenge**. Today I explored the magic of Python’s **dunder (double underscore) methods** to make my custom class behave like native Python objects.

---

## 📌 What’s This About?
Today’s focus:
- Using **dunder methods** like `__str__`, `__add__`, and `__len__`
- Making classes feel intuitive and Pythonic

---

## 💭 Why Is This Useful?
Dunder methods allow your classes to integrate seamlessly with Python’s built-in syntax. With them, you can:
- Customize print behavior (`__str__`)
- Combine objects with `+` (`__add__`)
- Support built-in functions like `len()` (`__len__`)

---

## ✨ Features

Here’s what the `Playlist` class supports:
- 🎶 `print(playlist)` – Displays playlist name and song count
- 🔢 `len(playlist)` – Returns number of songs in the playlist
- ➕ `playlist1 + playlist2` – Combines two playlists into one

---

## 🛠️ Tech Stuff

Built with:
- 🐍 **Python 3**
- 🎧 Custom class `Playlist`
- ✨ Dunder methods: `__str__`, `__add__`, `__len__`

---

## 🚀 Getting It Running

### ✅ What You’ll Need
Just Python 3!  
Run the program with:
```bash
python Day-21Code.py
