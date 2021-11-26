import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

st.set_page_config(layout='wide',
                  menu_items={
                      'Get Help': 'https://www.extremelycoolapp.com/help',
                      'Report a bug': "https://www.extremelycoolapp.com/bug",
                      'About': "# This is a header. This is an *extremely* cool app!"})
st.title('3D mapping in Streamiit')
st.write('')
st.write('Give a longitude and latitude to vieuw a randomized data visualization of the location chosen.')
a, b,c,d = st.columns(4)
longitude = a.number_input(label='longitude',value=37.76)
latitude = b.number_input(label='latitude',value=-122.4) 

df = pd.DataFrame(
    np.random.randn(3000, 2) / [50, 50] + [longitude, latitude],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
#     map_style='dark',
    initial_view_state=pdk.ViewState(
        latitude=longitude,
        longitude=latitude,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
     ],
 ))
st.write("How fast does this change my data app?") 