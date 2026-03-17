# 🔒 **AgroCryptGuard**

> **Secure, local, and offline application for encrypted agricultural data management.**

**AgroCryptGuard** is an open-source application focused on agricultural data management with a core emphasis on **security, privacy, and simplicity**. It utilizes **256-bit AES-GCM encryption** to protect sensitive data, featuring master password authentication powered by **Argon2id**.

---

## 🌟 **Features**

* ✅ **AES-GCM (256-bit)** Encryption
* ✅ Secure storage with **Argon2id** (PHC winner)
* ✅ Intuitive interface via **Streamlit**
* ✅ **100% Offline** – your data never leaves your computer
* ✅ Robust input validation and clear visual feedback
* ✅ Management for Costs, Production, Inputs, Harvest, and Finances

---

## 🛡️ **Security Layers**

### 🔐 Encryption (AEAD)
The application uses the **Authenticated Encryption with Associated Data (AEAD)** protocol to ensure that data is not only unreadable but also protected against unauthorized modifications.

| Parameter | Value |
| :--- | :--- |
| **Algorithm** | AES-GCM |
| **Key** | 256 bits |
| **Nonce** | 96 bits (unique per operation) |
| **Tag** | 128 bits (integrity verification) |

### 🔑 Password Protection
* **Argon2id Hashing:** Resistant to brute-force and GPU-accelerated attacks.
* **Random 128-bit Salt:** Unique salt generated upon the first execution.
* **Zero Knowledge:** The master password is **never** stored in plain text.

---

## 📦 **Installation & Setup**

### Prerequisites
* **Python 3.10+** - [Download](https://www.python.org/downloads/)
* **Git** (Optional) - [Download](https://git-scm.com/)

---

### 🎓 Step-by-Step Guide

#### **1. Get the Project**
**Option A (Git):**

git clone [https://github.com/your-username/AgroCryptGuard.git](https://github.com/your-username/AgroCryptGuard.git)
cd AgroCryptGuard
Option B (Manual): Download the ZIP, extract it, and open your terminal inside the folder.

2. Create a Virtual Environment

# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
3. Activate the Environment

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
4. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt
🚀 How to Use
Running the App
With the environment activated, run:


streamlit run app.py
The browser will automatically open at http://localhost:8501.

🔄 Workflow
First Access: Set your master password. Warning: There is no password recovery.

New Entry: Input your crop or financial data.

Encryption: When saving, the system encrypts the data into a .enc file.

Viewing: Data is decrypted in-memory only while the app is active.

📁 Project Structure

AgroCryptGuard/
├── app.py             # Streamlit UI
├── auth.py            # Argon2id Authentication
├── crypto.py          # AES-GCM Logic
├── storage.py         # File Handling
├── data/
│   └── data.enc       # Encrypted Database
├── auth.json          # Password Verifier
└── requirements.txt   # Dependencies
⚠️ Important Notices
[!IMPORTANT]
BACKUP: You are responsible for your data. Always keep a backup of auth.json and the data/ folder.

Lost Password: If you forget your master password, all data is permanently lost.

Privacy: 100% offline. No one but you has access to your records.

📝 License
Distributed under the MIT License.

Developed for the agricultural community.