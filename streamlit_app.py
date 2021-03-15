import os
import signal
import pandas as pd
import streamlit as st
from vaccinetracker import *

if __name__ == "__main__":
    # The coordinates for the Texas Capitol.
    st.markdown("# To run the vaccine alert system: \n- Enter in the Lat and Lon coordinates (you can find these using google maps the longitude is negative if it is a W coordiante)\n- Enter in the search radius if you would like to search larger then 20km \n- Once the data is correctly input the program will display a map of all the relevant HEBs\n- Click start to begin the alert system links will appear at the bottom of the page as vaccines become availble\n- Once started to do another search with a differnet location or search radius you will need to refresh the page")
    dist = float(st.slider("Search Radius:",1,100,20))
    home_lat = float(st.text_input("Latitude","0")) 
    home_lon = float(st.text_input("Longitude","0"))

    if home_lat != 0.0 and home_lon != 0.0: 
        home_coords = [home_lat,home_lon]
        app = Application(
            origin=home_coords,
            notifiers=[],
            min_qty=1,  # Don't show notifications less than 1
            max_dist=dist,  # Search within 20 miles
            rate=1  # update the results every 10 seconds
        )
        coords = app.make_location_map() 
        coords = pd.DataFrame(coords, columns = ['lat','lon']) 
        st.map(coords)
        start = st.button("Start") #not sure if this is gonna break hosting will objects get destroyed if page refreshes?
        if start: 
            app.run()
    else:
        st.text(f"Please input correct information")

