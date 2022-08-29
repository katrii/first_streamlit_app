import streamlit

streamlit.title("My Parents' New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Instagrammable Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Very Trendy Avocado Toast')
streamlit.text('🐔 Free-Range Eggs with Fancy Toppings')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
