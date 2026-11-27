# Manufacturing Production Performance Analysis

Portfolio project demonstrating production KPI analysis using Python, Excel, MySQL and Power BI. All records are synthetic; no employer or confidential production data is included.

## Repository structure
- `data/production.csv`: 1,200 synthetic records, 14 fields
- `scripts/generate_data.py`: reproducible dataset generator
- `scripts/analyze.py`: validation, plant KPI aggregation and chart
- `sql/01_schema.sql`: MySQL database and table
- `sql/02_analysis.sql`: quality checks and KPI queries
- `docs/` Excel and Power BI implementation guide
- `outputs/`: generated analysis results (created when script runs)

## Run the project
1. Install Python 3.10+ and run `pip install -r requirements.txt`.
2. Run `python scripts/generate_data.py` then `python scripts/analyze.py`.
3. In MySQL Workbench execute `sql/01_schema.sql`. Import `data/production.csv` into the existing production_data table using Table Data Import Wizard. Map all CSV fields to matching columns, omit Production_ID, and skip the header row.
4. Execute `sql/02_analysis.sql` and verify the row count and KPIs.
5. Build Excel and Power BI reports using the guide.

## KPIs
- Variance = Actual - Planned
- Achievement % = SUM(Actual) / SUM(Planned) × 100
- Good production = Actual - Rejected
- Rejection % = SUM(Rejected) / SUM(Actual) × 100

## Suggested dashboard
Plant performance, shift comparison, machine downtime, production trend, rejection rate and date filters.

## Project status
The dataset, Python analysis and SQL scripts are provided. Excel workbook and Power BI PBIX are not included; follow the guide to create them. Do not claim these deliverables as completed until you build and verify them.
