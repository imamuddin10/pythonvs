# 🏦 Customer Behavior & Cross-Sell Analytics

## 📌 Problem Statement
Banks often run broad marketing campaigns, but conversion rates remain low due to uniform targeting.  
This project analyzes customer behavior to identify high-probability users for cross-sell and improve campaign efficiency.

---

## 📊 Dataset
- Banking marketing dataset (~11K customers)
- Features include:
  - Demographics (age, job, education)
  - Financial (balance)
  - Campaign data (contact type, campaign count)
  - Previous interactions (poutcome)

---

## ⚙️ Approach

### 1. Data Cleaning
- Handled missing values and "unknown" categories  
- Converted target variable (`deposit`) into binary format  

### 2. Exploratory Data Analysis
- Identified key drivers of conversion  
- Analyzed customer behavior and campaign performance  

---

## 🔍 Key Insights

- Previous campaign success → **91% conversion (strongest predictor)**  
- High-balance customers → **higher likelihood to convert (~58%)**  
- Cellular contact → **better performance**  
- More campaigns → **lower conversion (customer fatigue)**  

---

## 💡 Business Recommendations

- Target customers with previous successful interactions  
- Focus on high-balance users  
- Use cellular channels for outreach  
- Reduce excessive campaign contacts  

---

## 📈 Business Impact

Targeted campaigns can improve conversion efficiency while reducing unnecessary outreach, leading to better customer engagement and higher ROI.

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy)

---

## 📂 Project Structure
