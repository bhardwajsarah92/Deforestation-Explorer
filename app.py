import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Deforestation Over Time: Our Planet in Numbers")
st.write("Welcome to the interactive data explorer. This website examines deforestation patterns across the world, how they have changed over time, and what causes them.")
st.write("Feel free to check out the **Take Action!** section to see how you can do your part in helping the climate!")


col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="**Total Loss (2025)**", value="4.3 Mha", delta="-36% vs 2024", delta_color="inverse")

with col2:
    st.metric(label="**Primary Driver**", value="Agriculture")

with col3:
    st.metric(label="**Worst Recent Year**", value="2024", delta="+540% vs 2023", delta_color="inverse")

# Data Taken from University of Maryland Global Land Analysis and Discovery (GLAD)
if "current_country" not in st.session_state:
    st.session_state.current_country = "Global"

all_country_data = {
    "Global": { "Year":[2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 , 2020, 2021, 2022, 2023, 2024, 2025],
    "Human Clearing (Agri/Logging)": [3.2, 3.1, 3.4, 3.6, 3.0, 3.2, 3.2, 3.1, 3.2, 3.3, 3.4, 3.3, 3.4, 3.3, 3.6, 3.5, 3.2, 3.4, 3.6, 3.25, 3.3, 3.2, 3.5, 2.7],
    "Wildfire Loss": [0.2, 0.2, 0.2, 0.3, 0.4, 0.3, 0.2, 0.4, 0.4, 0.3, 0.4, 0.3, 0.5, 0.4, 1.1, 0.8, 0.4, 0.4, 0.6, 0.5, 0.8, 0.5, 3.2, 1.6]
    
    }, 
    "Brazil": { "Year": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 , 2020, 2021, 2022, 2023, 2024, 2025],
    "Primary Forest Loss": [60, 74, 69, 120, 110, 67, 71, 80, 110, 65, 120, 87, 100, 120, 450, 190, 160, 180, 200, 270, 350, 250, 400, 210]

    },
    "Indonesia": { "Year": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 , 2020, 2021, 2022, 2023, 2024, 2025],
    "Primary Forest Loss": [270, 250, 480, 480, 470, 530, 470, 680, 540, 610, 860, 470, 740, 670, 930, 370, 340, 320, 270, 200, 230, 290, 260, 300]
   
    }, 
    "DR Congo": { "Year": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 , 2020, 2021, 2022, 2023, 2024, 2025],
    "Primary Forest Loss": [170, 78, 120, 150, 150, 150, 120, 220, 270, 150, 210, 350, 440, 320, 500, 470, 480, 480, 490, 500, 510, 530, 590, 560]

    },
    "Bolivia": { "Year": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 , 2020, 2021, 2022, 2023, 2024, 2025],
    "Primary Forest Loss": [70, 77, 97, 140, 120, 110, 180, 110, 270, 160, 150, 82, 130, 83, 250, 270, 150, 290, 280, 290, 380, 490, 1500, 620]
    }
}

st.write("Explore Specific Regions:")
btn_col1, btn_col2, btn_col3, btn_col4, btn_col5 = st.columns(5)

with btn_col1:
    if st.button("Global View", use_container_width=True):
        st.session_state.current_country = "Global"

with btn_col2:
    if st.button("Brazil", use_container_width=True):
        st.session_state.current_country = "Brazil"
    
with btn_col3:
    if st.button("Indonesia", use_container_width=True):
        st.session_state.current_country = "Indonesia"

with btn_col4:
    if st.button("DR Congo", use_container_width=True):
        st.session_state.current_country = "DR Congo"

with btn_col5:
    if st.button("Bolivia", use_container_width=True):
        st.session_state.current_country = "Bolivia"

active_region = st.session_state.current_country
if active_region not in all_country_data:
    active_region = "Global"

df = pd.DataFrame(all_country_data[active_region])

if active_region == "Global":
    y_columns = ["Human Clearing (Agri/Logging)", "Wildfire Loss"]
    color_map = {
        "Human Clearing (Agri/Logging)": "#65ba79",
        "Wildfire Loss": "#eb5e34",
    }
    fig = px.line(
        df,
        x="Year",
        y=y_columns,
        title=f"Tropical Primary Forest Loss in {active_region} (2002-2025)",
        labels={"value": "Forest Loss (kha)", "variable": "Metric Tracking"},
        color_discrete_map=color_map,
    )
else:
    y_columns = ["Primary Forest Loss"]
    color_map = {
        "Primary Forest Loss": "#2ca02c"
    }
    fig = px.bar(
        df,
        x="Year",
        y=y_columns,
        title=f"Tropical Primary Forest Loss in {active_region} (2002-2025)",
        labels={"value": "Forest Loss (kha)", "variable": "Metric Tracking"},
        color_discrete_map=color_map,
    )

analysis_content = {
    "Global": """
    ### Global Carbon & Climate Implications
    The global forest loss signal shows both human clearing and wildfire impact.
    * Agriculture, logging, and wildfire can all drive large swings in tropical forest loss.
    * Tracking these metrics together helps show how policies and climate extremes interact over time.
    """,

    "Brazil": """
    ### Brazil & The Amazon Tipping Point
    The Amazon Rainforest is approaching a critical ecological tipping point.
    * The Moisture Cycle: The Amazon creates its own rain by recycling moisture through its canopy.
    * Why this Matters: Scientists warn that if deforestation crosses a 20-25% threshold, the forest will lose the ability to generate rain.
    * A collapse would transition the forest into a dry savanna and disrupt global weather systems.
    """,

    "Indonesia": """
    ### Indonesia, Peatlands & Biodiversity Loss
    Indonesia's forest loss is strongly linked to peatland drainage, fires, and plantation expansion.
    * Peatland fires emit large volumes of carbon and destroy critical biodiversity.
    * Conserving peatland forests is essential for climate stability in Southeast Asia.
    """,

    "DR Congo": """
    ### DR Congo & The Congo Basin Rainforest
    The Congo Basin is the world's second-largest rainforest and a key carbon sink.
    * Logging, agriculture, and mining threaten the region's ability to store carbon.
    * Protecting the Congo Basin is vital for regional climate resilience and biodiversity.
    """,

    "Bolivia": """
    ### Bolivia & The Amazon Rainforest
    Bolivia's deforestation trends are tied to cattle ranching, soy expansion, and fire.
    * The Bolivian Amazon is a critical corridor linking major rainforest regions.
    * Strong land-use policies are needed to preserve biodiversity and local climate.
    """
}

fig.update_layout(barmode='stack', xaxis_tickmode='linear')

st.write("---")
st.header("Regional Forest Loss Charts")
st.write("Select a region above and review the chart below.")
st.plotly_chart(fig)
st.write("---")

# Show chart outside the tabs

tab1, tab2 = st.tabs(["Analysis", "Take Action"])

with tab1:
    st.markdown(analysis_content.get(active_region, "### Region analysis is not available."))

    with st.expander("🔎 Click Here for An In-Depth Analysis of the Causes of Deforestation"):
        st.subheader("Key Climate Insights:")
        st.markdown("""
                     * **The Core Threat:** According to the World Resource Institute, the tropics has lost 4.3 million hectares of primary forest in 2025; an area larger than Switzerland.
                     * **The Impact:** Deforestation is a detrimental problem, destroying ecosystems, accelerating global warming and threatening humans.
                     * **The Power of Policy:** The 36% decrease in 2025 was primarily driven by stronger anti-deforestation policies and reduced fire activity.
                     """)

with tab2:
    st.subheader("How You Can Make an Impact")
    st.write("* **Eat less beef**: Cattle ranching is responsible for about 41% of global deforestation, especially in the Amazon Rainforest.")
    st.write("* **Reduce soy consumption**: Large forest tracts are cleared for soy fields, primarily used as livestock feed.")
    st.write("* **Adopt Meatless Mondays**: Cutting meat consumption by 20% can help dramatically scale back the demand for new agricultural land.")
    st.write("* **Buy FSC-certified items**: Check wood, paper, and tissue products for the \"check tree\" label from the Forest Stewardship Council.")
    st.write("* **Print on Both Sides**: Use \"good on one side\" paper scraps for notes before throwing them away.")
    st.write("* **Avoid Unsustainable Palm Oil**: Look at ingredient labels on snack and cosmetics to avoid products driving tropical deforestation.")