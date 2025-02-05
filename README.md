# 🔄 Backup Sync Utility v1.0  

📌 **A Python GUI tool for syncing new files from a primary drive to a backup drive.**  

---

## 🚀 **Features**  
✅ **User-Friendly GUI** – Select drives easily using a graphical interface  
✅ **Automatic File Sync** – Copies **new** files from the primary drive to the backup  
✅ **Non-Blocking UI** – Uses **threading** to prevent the UI from freezing  
✅ **Real-Time Status Updates** – Displays `Syncing...` and `Success ✅` messages  
✅ **Error Handling** – Alerts users if an error occurs during sync  

---

## 🖥️ **How It Works**  

1️⃣ **Run the application**  
2️⃣ **Select Primary Drive (Left)** 📂 – This is the source drive containing new files  
3️⃣ **Select Backup Drive (Right)** 📂 – This is the destination drive where files will be copied  
4️⃣ Click **"Sync Now"**  
5️⃣ **Status updates in real time**:  
   - `"Syncing..."` (Orange)  
   - `"Sync Completed Successfully ✅"` (Green)  
   - `"Sync Failed ❌"` (Red)  

---

## 📸 **Screenshot** *(TBA)*  
![Backup Sync Utility Screenshot](screenshot.png)  

---

## 🔧 **Installation & Setup**  
### **1️⃣ Prerequisites**  
- **Python 3.8+**  
- Required libraries (install if missing):  
  ```sh
  pip install tk

2️⃣ Running the Program
1. Clone the repository
   ```sh
   git clone https://github.com/your-username/BackupSyncTool.git
   cd BackupSyncTool

3. Run the script
   ```sh
   python BackupSyncTool.py

## 🛠️ **Planned Future Features**  
✅ **Progress Bar for File Copying**  
✅ **Logging System (`sync_log.txt`)**  
✅ **Auto-Sync on Drive Plug-In**  
✅ **Timestamped Versions for Modified Files**  

---

## 💻 **Contributing**  
🔹 Feel free to **fork** this project and submit **pull requests** with improvements!  

---

## 📜 **License**  
📝 This project is open-source under the **MIT License**.  

---

## 🌎 **Author**  
👤 **MedusaDrift**  
🔗 GitHub: [MedusaDrift](https://github.com/MedusaDrift)  

---

🚀 **Happy Syncing!** 💾💻  
