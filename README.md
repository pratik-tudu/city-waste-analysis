# city-waste-analysis
This project is an interactive City Waste Collection Dashboard built using Python, Pandas, Matplotlib, and Gradio/Streamlit (depending on version). The application allows users to upload their own CSV datasets and visualize waste collection data in a simple and intuitive way.

# 📊 City Waste Collection Dashboard

🔗 Live Project: https://huggingface.co/spaces/pratik-tudu/city-waste-analysis

An interactive data visualization dashboard built using **Python**, **Pandas**, **Matplotlib**, and **Gradio/Streamlit** that analyzes city waste collection data.  
The application allows users to upload CSV files and instantly visualize waste patterns across different zones, areas, dates, and waste types.

---

## 🚀 Project Overview

Urban waste management plays a crucial role in maintaining clean and sustainable cities.  
This project helps analyze waste collection data by presenting it visually, making it easier to understand trends, compare zones, and identify waste distribution patterns.

The dashboard supports **user-uploaded datasets** and also includes **sample data** for quick testing.

---

## ✨ Features

- 📁 **CSV File Upload**
  - Upload your own waste collection dataset
  - Automatic data validation

- 🗓️ **Date-based Records**
  - Uses actual dates instead of weekday names

- 🌍 **Area-wise Analysis**
  - Green Part  
  - Lake View  
  - River Side  
  - Hill Town  

- ♻️ **Waste Type Classification**
  - Organic Waste  
  - Plastic Waste  

- 📊 **Visualizations**
  - Zone-wise waste collection
  - Waste type distribution
  - Interactive bar charts

- 🧩 **Fallback Sample Data**
  - Sample dataset loads if no CSV is uploaded

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Matplotlib**
- **Gradio / Streamlit**
- **CSV File Handling**

---

## 📂 Dataset Format

The uploaded CSV file should include the following columns:

| Column Name | Description |
|------------|------------|
| `Date` | Date of waste collection |
| `Zone` | City zone (North, South, East, West) |
| `Area` | Area type (Green Part, Lake View, etc.) |
| `Waste_Type` | Type of waste (Organic / Plastic) |
| `Waste_Collected_Tons` | Waste collected in tons |

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/city-waste-dashboard.git
cd city-waste-dashboard

