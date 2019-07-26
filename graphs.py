def count_graph(yes,no):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    import csv

    df = pd.read_csv("newdata.csv")
    df1=df.loc[:,[yes,no]]

    sns.set(style="darkgrid")

    g = sns.catplot(x=yes, hue=no,  data=df1, kind="count", height=4,palette="ocean",aspect=7/4)
    g.set_xticklabels(rotation=45)
    

def sum_graph(one,two):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    import csv
    df = pd.read_csv("newdata.csv")
    df3 = pd.DataFrame()
    unique_product=df[two].unique()
    df2=df.loc[:,[one]]

    for i in unique_product:
        df3[i]=df2.loc[df.loc[:,two]==i].sum()

    fig,ax = plt.subplots(1)
    ax.bar(height=df3.iloc[0,:],x=df3.columns)

    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
      
    
def basic_count(x):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    import csv
    df = pd.read_csv("newdata.csv")
    plt.figure(figsize=(6,4))
    sns.set(style="darkgrid")

    ax = sns.countplot(x=df.loc[:,x], palette="inferno")
    for item in ax.get_xticklabels():
        item.set_rotation(45)
    