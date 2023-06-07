import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity",
                                                         "Social support", "Life expectancy",
                                                         "Freedom to make life choices",
                                                         "Corruption"))

y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity",
                                                         "Social support", "Life expectancy",
                                                         "Freedom to make life choices",
                                                         "Corruption"))

st.subheader(f"{x_axis} and {y_axis}")


def get_data(x, y):
    x = x.replace(" ", "_")
    y = y.replace(" ", "_")
    x_data = list(df[f"{x.lower()}"])
    y_data = list(df[f"{y.lower()}"])
    return x_data, y_data


x_axis_data, y_axis_data = get_data(x_axis, y_axis)

fig = px.scatter(x=x_axis_data, y=y_axis_data, labels={"x": x_axis, "y": y_axis}, hover_name=df['country'])

st.plotly_chart(fig)
