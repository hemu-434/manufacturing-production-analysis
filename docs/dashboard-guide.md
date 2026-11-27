# Excel and Power BI guide

## Excel
Import production.csv with Data > From Text/CSV. Format as table. Create PivotTables by Plant, Shift, Date and Machine_ID. Sum planned, actual, rejected and downtime. Use ratios of summed quantities for aggregate achievement and rejection rates. Add clustered column charts and slicers.

## Power BI
Import the CSV or connect to MySQL. Set Date to date and quantity columns to numeric types. Create measures:

Planned = SUM(production_data[Planned_Qty])
Actual = SUM(production_data[Actual_Qty])
Achievement % = DIVIDE([Actual],[Planned],0)*100
Rejected = SUM(production_data[Rejected_Qty])
Rejection % = DIVIDE([Rejected],[Actual],0)*100
Variance = [Actual]-[Planned]

Create cards for KPIs, a plant comparison chart, daily trend line, machine downtime bar chart and date/shift slicers. Save your PBIX in this repository after verification.
