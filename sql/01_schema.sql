CREATE DATABASE IF NOT EXISTS Manufacturing_Production_DB;
USE Manufacturing_Production_DB;
CREATE TABLE IF NOT EXISTS production_data (
 Production_ID INT AUTO_INCREMENT PRIMARY KEY,
 `Date` DATE, Plant VARCHAR(50), Shift VARCHAR(30), Machine_ID VARCHAR(30),
 Product VARCHAR(50), Planned_Qty INT, Production_Hours DECIMAL(5,2),
 Downtime_Minutes INT, Actual_Qty INT, Rejected_Qty INT,
 Production_Variance INT, Achievement_Pct DECIMAL(8,2),
 Good_Production INT, Rejection_Rate_Pct DECIMAL(8,2)
);
