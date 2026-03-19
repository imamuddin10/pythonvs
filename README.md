📊 Data Jobs Market Analysis — India

An end-to-end Python data analysis project exploring job postings, skill demand, and salary trends for data roles in India using the lukebarousse/data_jobs dataset from Hugging Face.


🎯 Project Goals

Investigate top-paying roles and skills in the data science industry
Explore a real-world dataset of job postings using Python
Generate actionable insights for job seekers looking for data roles in India


❓ Questions Answered
#Question1What are the most demanded skills for the top 3 most popular data roles?2How are in-demand skills trending for Data Analysts?3How well do jobs and skills pay for Data Analysts in India?4What is the most optimal skill to learn? (High Demand AND High Paying)

📁 Project Structure
├── 1_EDA.ipynb              # Exploratory Data Analysis — global and India-level overview
├── 2_skill_demand.ipynb     # Skill demand analysis for top 3 data roles in India
├── 3_salary_analysis.ipynb  # Salary distribution and skill-salary mapping for Data Analysts
└── README.md

📓 Notebook Breakdown
1. 1_EDA.ipynb — Exploratory Data Analysis
Objective: Understand the overall structure of the dataset and narrow the focus to India.
Steps performed:

Loaded the lukebarousse/data_jobs dataset (~785,741 job postings) using the Hugging Face datasets library
Visualised distribution of job postings by job title, country, and company
Analysed binary job attributes using pie charts:

Work From Home availability
Degree requirement mention
Health insurance offering


Filtered dataset to India-only postings
Plotted top job titles, companies, and locations within India

Key Insight: Data Engineer is the most posted role in India, followed by Data Scientist and Data Analyst.

2. 2_skill_demand.ipynb — Skill Demand Analysis
Objective: Identify the most requested skills for the top 3 data roles in India.
Methodology:

Cleaned the job_skills column — converted string-represented lists using ast.literal_eval
Exploded the skills column so each skill occupies its own row
Grouped by job_skills and job_title_short to count skill frequency
Focused on: Data Analyst, Data Engineer, Data Scientist
Merged skill counts with total job counts per title to compute skill percentages
Visualised skill percentages in a multi-panel bar chart

Key Insights:

Data Engineer: SQL (~68%), Python (~61%), Spark (~38%), AWS (~37%)
Data Scientist: Python (~70%), SQL, and ML-specific tools
Data Analyst: Excel, SQL, Python, Power BI, Tableau are top demanded skills


3. 3_salary_analysis.ipynb — Salary Analysis
Objective: Understand how salary varies across job titles and skills for Data Analysts in India.
Methodology:

Filtered for India job postings with non-null salary_year_avg
Selected top 6 job titles by posting volume
Ordered job titles by median salary and plotted salary distributions using box plots
Drilled into Data Analyst roles specifically:

Exploded skill column
Grouped by skill to get count and median salary
Identified top 10 highest-paying skills (by median)
Identified top 10 most in-demand skills (by count, then sorted by median)


Plotted both as side-by-side horizontal bar charts

Key Insights:
CategoryTop SkillsHighest PaidPostgreSQL, PySpark, GitLab, Linux, MySQL (~$165K median)Most In-DemandSQL (46 listings), Excel (39), Python (36)Best BalancePower BI (~$111K, high demand), Tableau (~$108K)

🛠️ Tech Stack
ToolPurposePython 3Core programming languagepandasData manipulation and aggregationmatplotlibBase plotting libraryseabornStatistical visualisationdatasets (Hugging Face)Loading the lukebarousse/data_jobs datasetastParsing string-represented Python lists in skill columns

🚀 Getting Started
Prerequisites
bashpip install pandas matplotlib seaborn datasets
Run
Clone the repo and open the notebooks in order:
bashgit clone https://github.com/your-username/data-jobs-india-analysis.git
cd data-jobs-india-analysis
jupyter notebook
Run notebooks in sequence:

1_EDA.ipynb
2_skill_demand.ipynb
3_salary_analysis.ipynb


📊 Dataset

Source: lukebarousse/data_jobs on Hugging Face
Size: ~785,741 job postings globally
India subset: ~51,000+ postings
Key columns used: job_title_short, job_country, job_skills, salary_year_avg, company_name, job_location


💡 Key Takeaways for Job Seekers in India

SQL and Python are non-negotiable — demanded across all top data roles
Power BI and Tableau offer the best balance of demand and salary for Data Analysts
PySpark, PostgreSQL, and cloud tools (AWS, Azure) push salaries significantly higher
Data Engineer is the most posted and among the highest-paid roles in India
Degree requirements are often not mentioned — skills matter more than credentials


👤 Author

Analysis focused on the Indian job market using real-world data from 2023–2024 job postings.


📄 License
This project is for educational and portfolio purposes. Dataset credit: Luke Barousse.
