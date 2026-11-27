USE Manufacturing_Production_DB;
SELECT COUNT(*) AS total_rows FROM production_data;
SELECT * FROM production_data WHERE Planned_Qty<=0 OR Actual_Qty<0 OR Rejected_Qty<0 OR Rejected_Qty>Actual_Qty;
SELECT Plant, SUM(Planned_Qty) planned, SUM(Actual_Qty) actual,
 SUM(Actual_Qty)-SUM(Planned_Qty) variance,
 ROUND(100*SUM(Actual_Qty)/NULLIF(SUM(Planned_Qty),0),2) achievement_pct,
 ROUND(100*SUM(Rejected_Qty)/NULLIF(SUM(Actual_Qty),0),2) rejection_pct,
 SUM(Downtime_Minutes) downtime
FROM production_data GROUP BY Plant;
SELECT Shift, SUM(Actual_Qty) actual, SUM(Downtime_Minutes) downtime FROM production_data GROUP BY Shift;
SELECT Machine_ID, SUM(Actual_Qty-Planned_Qty) variance FROM production_data GROUP BY Machine_ID ORDER BY variance;
