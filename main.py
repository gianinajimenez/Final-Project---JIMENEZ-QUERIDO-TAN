def main():
    
    import pandas as pd
    import ipywidgets as widgets
    from ipywidgets import interact, interact_manual
    import graphs
    
    df = pd.read_csv("newdata.csv")
    
    categories = ['Branch', 'Customer Type', 'Gender','Product Line','Date','Time','Payment','Basic Stats']
    options_branch = ['Net Profit per Branch','Number of Members per Branch','Number of Sales per Branch']
    options_ct = ['Net Profit per Customer Type','Number of Members per Gender']
    options_gender = ['Number of Sales per Gender','Product Line Popularity per Gender', 'Type of Payment per Gender', 'Number of Members per Gender','Total Amount Spent per Gender']
    options_pl = ['Net Profit per Product Line','Payment Type per Product Line', 'Number of Sales per Product Line','Number of Sales per Product Line per Month']
    options_date = ['Number of Sales per Month','Number of Sales per Product Line per Month','Net Profit per Month']
    options_time = ['Number of Sales per Hour']
    options_payment = ['Payment Type per Product Line', 'Number of Sales per Payment Type', 'Type of Payment per Gender', 'Net Profit per Payment Type']
    options_bs = ['Overall Net Profit','Average Amount per Sale']

    def second_option(Option):
        if Option=="Net Profit per Branch":
            display(df.loc[:,["Branch","Net Profit"]].groupby("Branch").sum())
            graphs.sum_graph("Net Profit","Branch")
        if Option=="Number of Members per Branch":
            display(df.loc[df.loc[:,"Customer Type"]=="Member",["Customer Type","Branch"]].groupby("Branch").count())
            graphs.count_graph("Customer Type","Branch")
        if Option=="Number of Sales per Branch":
            display(df.loc[:,["Invoice ID","Branch"]].groupby("Branch").count())
            graphs.basic_count("Branch")
        if Option=="Net Profit per Customer Type":
            display(df.loc[:,["Net Profit","Customer Type"]].groupby("Customer Type").sum())
            graphs.sum_graph("Net Profit","Customer Type")
        if Option=="Number of Members per Gender":
            display(df.loc[df.loc[:,"Customer Type"]=="Member",["Customer Type","Gender"]].groupby("Gender").count())
            graphs.count_graph("Customer Type","Gender")
        if Option=="Number of Sales per Gender":
            display(df.loc[:,["Gender","Invoice ID"]].groupby("Gender").count())
            graphs.basic_count("Gender")
        if Option=="Product Line Popularity per Gender":
            display(df.loc[:,["Invoice ID","Gender","Product Line"]].groupby(["Gender","Product Line"]).count())
            graphs.count_graph("Product Line","Gender")
        if Option=="Type of Payment per Gender":
            display(df.loc[:,["Gender","Payment","Invoice ID"]].groupby(["Gender","Payment"]).count())
            graphs.count_graph("Payment","Gender")
        if Option=="Net Profit per Product Line":
            display(df.loc[:,["Net Profit","Product Line"]].groupby("Product Line").sum())
            graphs.sum_graph("Net Profit","Product Line")
        if Option=="Payment Type per Product Line":
            display(df.loc[:,["Payment","Product Line","Invoice ID"]].groupby(["Payment","Product Line"]).count())
            graphs.count_graph("Payment","Product Line")
        if Option=="Number of Sales per Product Line":
            display(df.loc[:,["Product Line","Invoice ID"]].groupby("Product Line").count())
            graphs.basic_count("Product Line")
        if Option=="Number of Sales per Payment Type":
            display(df.loc[:,["Invoice ID","Payment"]].groupby("Payment").count())
            graphs.basic_count("Payment")
        if Option=="Net Profit per Payment Type":
            display(df.loc[:,["Payment","Net Profit"]].groupby("Payment").sum())
            graphs.sum_graph("Net Profit","Payment")
        if Option=="Overall Net Profit":
            display(df["Net Profit"].sum())
        if Option=="Number of Sales per Hour":
            ten = df.loc[df["Time"].str.match("10"),"Invoice ID"].count()
            eleven = df.loc[df["Time"].str.match("11"),"Invoice ID"].count()
            twelve = df.loc[df["Time"].str.match("12"),"Invoice ID"].count()
            thirteen = df.loc[df["Time"].str.match("13"),"Invoice ID"].count()
            fourteen = df.loc[df["Time"].str.match("14"),"Invoice ID"].count()
            fifteen = df.loc[df["Time"].str.match("15"),"Invoice ID"].count()
            sixteen = df.loc[df["Time"].str.match("16"),"Invoice ID"].count()
            seventeen = df.loc[df["Time"].str.match("17"),"Invoice ID"].count()
            eighteen = df.loc[df["Time"].str.match("18"),"Invoice ID"].count()
            nineteen = df.loc[df["Time"].str.match("19"),"Invoice ID"].count()
            twenty = df.loc[df["Time"].str.match("20"),"Invoice ID"].count()
            display(pd.DataFrame({"Hour":["10 am - 11 am","11 am - 12 pm","12 pm - 1 pm", "1 pm - 2 pm", "2 pm - 3 pm", "3 pm - 4 pm", "4 pm - 5 pm", "5 pm - 6 pm", "6 pm - 7 pm","7 pm - 8 pm", "8 pm - 9 pm"],"Count":[ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]}))
        if Option=="Number of Sales per Month":
            display(df.loc[:,["Month","Invoice ID"]].groupby("Month").count())
        if Option=="Number of Sales per Product Line per Month":
            display(df.loc[:,["Invoice ID","Product Line","Month"]].groupby(["Month","Product Line"]).count())
        if Option=="Total Amount Spent per Gender":
            display(df.loc[:,["Gender","Total"]].groupby("Gender").sum())
        if Option=="Average Amount per Sale":
            display(df["Total"].mean())
        if Option=="Net Profit per Month":
            display(df.loc[:,["Month","Net Profit"]].groupby("Month").sum())
        

    def first_option(Category):
        if Category == 'Branch':
            interact(second_option, Option=options_branch)
        if Category == 'Customer Type':
            interact(second_option, Option=options_ct)
        if Category == 'Gender':
            interact(second_option, Option=options_gender)
        if Category == 'Product Line':
            interact(second_option, Option=options_pl)
        if Category == 'Date':
            interact(second_option, Option=options_date)
        if Category == 'Time':
            interact(second_option, Option=options_time)
        if Category == 'Payment':
            interact(second_option, Option=options_payment)
        if Category == 'Basic Stats':
            interact(second_option, Option=options_bs)
    interact(first_option, Category=categories)