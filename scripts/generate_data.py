import pandas as pd
import numpy as np
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(42)
n=1200
df=pd.DataFrame({'Date':rng.choice(pd.date_range('2026-01-01','2026-04-30'),n),'Plant':rng.choice(['A','B','C'],n),'Shift':rng.choice(['Morning','Evening','Night'],n),'Machine_ID':rng.choice([f'M{i:02}' for i in range(1,13)],n),'Product':rng.choice(list('XYZW'),n),'Planned_Qty':rng.integers(500,1501,n),'Production_Hours':rng.uniform(6,8,n).round(2),'Downtime_Minutes':rng.integers(0,91,n)})
df['Actual_Qty']=(df.Planned_Qty*rng.uniform(.75,1.08,n)).round().astype(int)
df['Rejected_Qty']=(df.Actual_Qty*rng.uniform(.005,.06,n)).round().astype(int)
df['Production_Variance']=df.Actual_Qty-df.Planned_Qty
df['Achievement_Pct']=(df.Actual_Qty/df.Planned_Qty*100).round(2)
df['Good_Production']=df.Actual_Qty-df.Rejected_Qty
df['Rejection_Rate_Pct']=(df.Rejected_Qty/df.Actual_Qty*100).round(2)
(root/'data').mkdir(exist_ok=True)
df.to_csv(root/'data/production.csv',index=False,date_format='%Y-%m-%d')
print('Generated',len(df),'rows')
