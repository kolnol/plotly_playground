import pandas
import numpy as np
from datetime import timedelta, datetime

import pandas as pd

amount_datapoints_to_generate = 100
temp1 = np.random.randint(0, 100, size=amount_datapoints_to_generate)
temp2 = np.random.randint(0, 100, size=amount_datapoints_to_generate)

pressure = np.random.randint(0, 100, size=amount_datapoints_to_generate)

sdate = datetime.fromisoformat('2022-06-04T00:05:23')  # start date
edate = sdate + timedelta(seconds=amount_datapoints_to_generate)  # end date
time = pandas.date_range(sdate, edate-timedelta(seconds=1), freq='s')

d = {
    'Time': time,
    '12343pt343': pressure,
    '2321tt2334': temp1,
    '2144tt2356': temp2,
}

df = pd.DataFrame(data=d)

df.to_csv('test.csv', index=False)
