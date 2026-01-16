# 📱 Data-Driven Product Management: Market Analysis for App Development
**Technical Research Case Study | Python Business Intelligence**

## 📌 Project Overview
This research analyzed the mobile app market using a dataset of over 9,000 apps to identify profitable niches for new product development. The project focuses on uncovering the relationship between **Category**, **Rating**, **Pricing**, and **Installs** to provide data-driven recommendations that minimize risk and maximize user acquisition for a product management team.

---

## 🛠️ Technical Toolkit
* **Language:** Python
* **Libraries:** Pandas (Data Cleaning & Wrangling), Seaborn & Matplotlib (Market Visualization)
* **Techniques:** Data Sanitization, Type Conversion, Category Aggregation, Outlier Analysis.

---

## 🧮 Research Methodology
A multi-stage data pipeline was implemented to transform raw, "dirty" market data into actionable insights:

1.  **Data Sanitization & Cleaning:** I addressed data integrity issues in the `Installs` and `Price` columns by stripping non-numeric characters (e.g., `+`, `,`, `$`).
2.  **Type Conversion:** Converted cleaned strings into numeric types (float/int) to enable mathematical modeling and statistical calculations.
3.  **Market Segmentation:** Grouped over 30 categories to visualize market distribution and saturation levels.
4.  **Sentiment Mapping:** Evaluated average user ratings across categories to identify sectors where users are consistently underserved or dissatisfied.

---

## 📊 Key Insights & Market Outcomes
* **Niche Opportunity:** Specific categories like **HEALTH_AND_FITNESS** showed a strong balance of high user installs and high sentiment (ratings), representing a prime "Market-Product Fit."
* **Monetization Strategy:** The analysis confirmed that the vast majority of successful market leaders follow a **Freemium model**, suggesting that a "Free-to-Install" entry point is essential for rapid scaling.
* **Rating Benchmarks:** Established that a new product must target a minimum rating of **4.3** to be competitive, as the majority of high-performing apps cluster between 4.0 and 4.5.

### Market Distribution Visualization
![App Market Distribution](./Images/category_distribution.png)
*Figure 1: Distribution of apps across various market categories, highlighting the volume of competition in each sector.*

### Rating vs. Pricing Insights
![Rating vs Price](./Images/rating_price_scatter.png)
*Figure 2: Scatter plot analysis showing the relationship between app pricing and user sentiment.*

---

## 💻 Technical Implementation
The core of this project involved programmatic data cleaning using Python's `apply` and `lambda` functions to prepare the dataset for statistical analysis.

```python
# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
apps = pd.read_csv('apps.csv')

# List of characters to remove for numeric analysis
chars_to_remove = ['+', ',', '$']
cols_to_clean = ['Installs', 'Price']

# Cleaning and Type Conversion Pipeline
for col in cols_to_clean:
    for char in chars_to_remove:
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))
    apps[col] = apps[col].astype(float)

# 1. Visualizing Category Distribution
plt.figure(figsize=(10, 8))
sns.countplot(y='Category', data=apps, order=apps['Category'].value_counts().index)
plt.title('Market Concentration by Category')
plt.show()

# 2. Analyzing Ratings Distribution
plt.figure(figsize=(8, 6))
sns.histplot(apps['Rating'], bins=20, kde=True)
plt.title('Distribution of User Ratings')
plt.show()
```
***Note:*** *This project demonstrates the application of Industrial Mathematics logic—precision and algorithmic structure—to solve modern business problems.*
## 📁 Repository Structure
```text
├── notebook.ipynb    
├── data/
│   └── three_keywords_geo.csv              
│   └── three_keywords.csv  
│   └── workout_geo.csv  
│   └── workout.csv  
└── README.md
```

## 📫 Connect with me:
* **LinkedIn:** [linkedin.com/in/emycodes](https://linkedin.com/in/emycodes)