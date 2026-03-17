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

## 📦 **Installation & Setup (Windows)**

### Prerequisites
* **Python 3.10 or higher** - [Download for Windows](https://www.python.org/downloads/windows/)
* **Git** (Optional) - [Download for Windows](https://git-scm.com/download/win)

---

### 🎓 Step-by-Step Guide

#### **1. Get the Project**
**Option A (Git):**

git clone [https://github.com/your-username/AgroCryptGuard.git](https://github.com/your-username/AgroCryptGuard.git)
cd AgroCryptGuard

Option B (Manual): Download the project as a ZIP file, extract it to a folder, and open the Command Prompt (CMD) or PowerShell inside that folder.

2. Create a Virtual Environment

python -m venv venv

3. Activate the Environment
Using PowerShell (Recommended):

.\venv\Scripts\Activate.ps1

4. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

🚀 How to Use
Running the App
With the environment activated, simply run:

streamlit run app.py

Your web browser will automatically open at http://localhost:8501.

🔄 Workflow
First Access: Set your master password (minimum 8 characters). Warning: There is no password recovery.

New Entry: Input your crop, input, or financial data.

Encryption: When saving, the system encrypts the data into a secure .enc file.

Viewing: Data is decrypted in-memory only while the app is active and disappears when closed.

📁 Project Structure

AgroCryptGuard/
├── app.py             # Streamlit UI (User Interface)
├── auth.py            # Argon2id Authentication Management
├── crypto.py          # AES-GCM Encryption Logic
├── storage.py         # Encrypted File Handling
├── config.py          # Security Parameters
├── data/
│   └── data.enc       # Encrypted Database
├── auth.json          # Password Verifier (Generated on 1st access)
└── requirements.txt   # Required Libraries


⚠️ Important Notices
[!IMPORTANT]
BACKUP: You are the sole responsible for your data. Always keep a backup of the auth.json file and the data/ folder on a secure USB drive or external HDD.

Lost Password: If you forget your master password, all data is permanently lost. There is no "Reset Password" button in local end-to-end encryption.

Privacy: 100% offline. No agency, company, or developer can access your records.

📝 License
Distributed under the MIT License.

Developed for the agricultural community.