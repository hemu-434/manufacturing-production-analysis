import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
df=pd.read_csv(root/'data/production.csv',parse_dates=['Date'])
assert df.isna().sum().sum()==0
assert (df.Rejected_Qty<=df.Actual_Qty).all()
def kpis(g):
 return pd.Series({'Planned':g.Planned_Qty.sum(),'Actual':g.Actual_Qty.sum(),'Achievement_Pct':100*g.Actual_Qty.sum()/g.Planned_Qty.sum(),'Rejection_Pct':100*g.Rejected_Qty.sum()/g.Actual_Qty.sum(),'Downtime':g.Downtime_Minutes.sum()})
summary=df.groupby('Plant').apply(kpis,include_groups=False) if int(pd.__version__.split('.')[0])>=2 else df.groupby('Plant').apply(kpis)
(root/'outputs').mkdir(exist_ok=True)
summary.to_csv(root/'outputs/plant_kpis.csv')
ax=summary[['Planned','Actual']].plot.bar(title='Production by plant',rot=0)
ax.figure.tight_layout(); ax.figure.savefig(root/'outputs/plant_performance.png')
print(summary)
