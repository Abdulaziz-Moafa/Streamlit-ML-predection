import base64
import time
import streamlit as st
import pandas as pd
import pickle


import my_webscraping
import numpy as np

timestr = time.strftime("%Y%m%d-%H%M%S")


def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    dataset = "GHARWAALA_data_{}_.csv".format(timestr)
    st.markdown("### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{dataset}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)


def main():
    global result

    st.title("GHARWAALAA")

    template = """
      <div style = "background-color : red; padding : 10px;font-size=23px;">
      <h1 style = "color:white;text-align:center;> HOUSE PRICE-PREDICTION <h1>
      </div>
      """

    st.markdown(template, unsafe_allow_html=True)
    display = ("jiomart", "winni", "Manakiranam")

    options = list(range(len(display)))

    option = st.selectbox("Choose a Site", options, format_func=lambda x: display[x])
    st.write("you selected", option)

    if option == 0:
        if st.button("SCRAP_JIO"):
            result = my_webscraping.scraping()
            st.success("scraping  process started")
        if st.button("DATA_DOWNLOAD"):
            df = pd.read_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\jiostore_data.csv")

            df = df.drop_duplicates(subset=['name', 'price', 'MRP'], keep="first")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            df.to_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\jiostore_data.csv")

            csv_downloader(df)
            st.balloons()

    elif option == 1:
        if st.button("SCRAP_WINNI"):
            result = my_webscraping.winniscrap()
            st.success("scraping process started ")

        if st.button("DOWNLOAD"):
            df = pd.read_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\winnistore_data.csv")
            df = df.drop_duplicates(subset=['name', 'price', 'MRP'], keep="first")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            df.to_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\winnistore_data.csv")
            csv_downloader(df)
            st.balloons()

    elif option == 2:
        if st.button("SCRAP_MANAKIRANAM"):
            result = my_webscraping.manakr()
            st.success("scraping process started ")

        if st.button("DOWNLOAD_FILE"):
            df = pd.read_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\manakiranam_data.csv")
            df = df.drop_duplicates(subset=['name', 'price', 'MRP'], keep="first")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            df.to_csv(r"C:\Users\zezo0\Downloads\Gharwaalaa1\Gharwaalaa\manakiranam_data.csv'")
            csv_downloader(df)
            st.balloons()

if __name__=="__main__":
    main()
