import plotly.express as px
import pandas as pd

# Exercise 1 Functions
def survivial_demographics():
    """Function that returns survival data by age and gender for the titanic data set
    """
    #Start by reading in the data 
    data = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

    #Now create our age categories 
    max_age = data["Age"].max()
    bins = [0,12, 19, 59, max_age]
    labels = ["Child", "Teen", "Adult", "Senior"]
    data["age_cat"] = pd.cut(data["Age"],\
                              bins = bins,\
                                  labels = labels, \
                                    right = True,\
                                          include_lowest = True)
    #Grouping the data 
    data_grouped = data.groupby(["Pclass", "Sex", "age_cat"]) \
        [["PassengerId", "Survived"]].agg({"PassengerId": "count", "Survived": "sum"})\
              .rename(columns ={"PassengerId": "n_passengers", "Survived": "n_survived"}).\
                reset_index()
    #Calculate the survival rate 
    #One question here: in R I can use dplyr's mutate to create new variables 
    #so it can stay all piped in togther, is there something similar for python? 
    #Or does it have to be a separate line of code? 
    data_grouped["survival_rate"] = data_grouped["n_survived"]/data_grouped["n_passengers"]
    #Arrange by survival rate
    data_grouped.sort_values(by = "survival_rate")
    return(data_grouped)

def visualize_demographic():
    """Function to generate visualization comparing the survivial rate of 
    women and children by class """
    #Start by getting the data from the first half of the exercise 
    data_grouped = survivial_demographics()
    #Then clean the data a little bit. I want all female passengers and child passengers 
    #to be in one category and all male, non child passengers to be another category 
    #Create the new variable 
    data_grouped["woman_child"] = (data_grouped["Sex"] == "female") | (data_grouped["age_cat"] == "Child")
    #Re-group the data 
    data_regrouped = data_grouped.groupby(["Pclass", "woman_child"])\
        [["n_passengers", "n_survived"]].agg({"n_passengers": "sum", "n_survived": "sum"})\
            .reset_index()
    #Then recalculate the survival rate 
    data_regrouped["survival_rate"] = data_regrouped["n_survived"]/data_regrouped["n_passengers"]

    #Now we can actual generate the figure 
    fig = px.bar(data_regrouped, 
             x = "Pclass", 
             y = "survival_rate",
             hover_data=["n_passengers"],
             color = "woman_child",
             color_discrete_sequence = ["#88AED0", "#E4A0B7"],
             template = "plotly_white",
             barmode = "group"
            )
    fig.update_layout(
        xaxis_title="Class",
        yaxis_title="Survival Rate",
        title_text = "Survivial rate of Women and Children by Class",
        yaxis = dict(
        tickformat = ".0%"  
        )
        )
    return(fig)

#Exercise 2 Functions 

def family_groups():
    """function to generate the data on family size"""
     #Start by reading in the data 
    data = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
    #Creating a new column for family size 
    data["family_size"] = data["SibSp"]  + data["Parch"] + 1
    #Grouping 
    grouped_data = data.groupby(["family_size", "Pclass"])\
        [["PassengerId", "Fare"]].agg({"PassengerId": "count", "Fare": ["mean", "min", "max"] })\
        .reset_index()
    grouped_data.columns = ['_'.join(col).strip() for col in grouped_data.columns.values]

    grouped_data = grouped_data.rename(columns ={"family_size_": "family_size",\
                               "Pclass_": "class", \
                                "PassengerId_count": "n_passengers",\
                                "Fare_mean": "avg_fare", \
                                "Fare_min": "min_fare", \
                                "Fare_max": "max_fare" }).\
                                        sort_values(by = ["class", "family_size"])
    return(grouped_data)
def last_names():
     #Start by reading in the data 
    data = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
    #Now we are getting the last name and counting the frequency 
    data[["last_name", "first_name"]] = data["Name"].str.split(",", expand = True)
    data.groupby(["last_name"])["last_name"].\
    count().\
            rename(columns = {"last_name": "family_count"}).\
                sort_values("family_count")




