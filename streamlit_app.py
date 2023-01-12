import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Favourites")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocker Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocaso Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.multiselect('Pick some fruits', list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
