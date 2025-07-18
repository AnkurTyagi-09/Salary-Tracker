
# 💰 Salary Tracker

A simple terminal-based Python application to track and manage salary-related entries, such as expenses and revenue, with secure access.

---

## 🔐 Authentication

The app uses a password-based authentication system:
- **Default Password**: `1234`
- Change this in the `PASSWORD` variable in the code if needed.

---

## 📦 Features

- ✅ Add new salary entries (date, name, amount, category, designation)
- 📃 View all entries
- ❌ Delete an entry by date and name
- 📊 Generate a trial balance summary
- 🔐 Password-protected access
- 🗂 CSV-based persistent storage

---

## 🛠 How to Run

```bash
python Salary\ Tracker-3.py
```

Make sure to have `salary.csv` in the same directory. If not, the script will create it.

---

## 📁 Data Format

Entries are stored in `salary.csv` with the following columns:

```csv
Date, Name, Amount, Category, Designation
```

---

## 📈 Trial Balance

Generates:
- Total Expenses
- Total Revenue
- Net Total (Revenue - Expenses)

---

## ⚠️ Notes

- Only `Expense` and `Revenue` are valid categories.
- Make sure the date is entered in `YYYY-MM-DD` format.

---

## 📄 License

Free to use for personal or educational purposes.
