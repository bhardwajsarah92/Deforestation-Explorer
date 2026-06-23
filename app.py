import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Deforestation: Our Planet in Numbers")
st.image(
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?q=80&w=1200&auto=format&fit=crop",
    caption="Industrial logging impacts on forest ecosystems.",
    use_container_width=True
)
st.write("Welcome to the interactive data explorer. This website examines deforestation patterns across the world, how they have changed over time, and what causes them.")
st.write("Feel free to check out the **Take Action!** section to see how you can do your part in helping the climate!")



col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="**Total Loss (2025)**", value="4.3 Mha", delta="-36% vs 2024", delta_color="inverse")

with col2:
    st.metric(label="**Primary Driver**", value="Agriculture")

with col3:
    st.metric(label="**Worst Recent Year**", value="2024", delta="+540% vs 2023", delta_color="inverse")


with st.expander("🔎 Click Here for An In-Depth Analysis of the Causes of Deforestation"):
    st.subheader("Key Climate Insights:")
    st.markdown("""
                * **The Core Threat:** According to the World Resource Institute, the tropics has lost 4.3 million hectares of primary forest in 2025; an area larger than Switzerland.
                * **The Impact:** Deforestation is a detrimental problem, destroying ecosystems, accelerating global warming and threatening humans.
                * **The Power of Policy:** The 36% decrease in 2025 was primarily driven by stronger anti-deforestation policies and reduced fire activity.
                """)

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

st.write(" **Explore Specific Regions**:")
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
    ### Indonesia & Biodiversity Loss
   Indonesia is home to approximately 93 million hectares of forest, covering about 50.3% of the total land area. This makes Indonesia one of the largest rainforest nations in the world.
    * Clearing land fragment habitats severely threatens endangered species such as the Bornean orangutan and Sumatran Tiger.
    * According to the World Resource Institute, Indonesia has lost approximately 74 million hectares of primary forest since 1990. 
    * As of 2020, Indonesia's forest cover has been reduced by approximately 50.3% from what it used to be.
    """,

    "DR Congo": """
    ### DR Congo & The Congo Basin Rainforest
    The Congo Basin is the largest remaining net carbon sink, removing on average of 160 million tons of carbon dioxide. 
    * As seen from the graph alongside the research done by Global Forest Watch, the Congo Basin has seen a 14.2% increase in primary forest loss in 2024.
    * In recent years, cocoa farming has emerged as the primary agriculture driver. In DRC, cocoa production has quadrupled between 2015 and 2023. Scientists predict these practices may lead to forest loss in highly forested landscapes such as Tsopo, Equateur and Orential provinces in DRC.
    * Charcoal Production is another major driver of forest loss. Although it does not directly lead to permanent loss of the forest, it causes widespread degradation. In DRC, around 95% of the population relies on biomass, including charcoal for energy.
    """,

    "Bolivia": """
    ### Alarming Rates of Deforestation in Bolivia
    Bolivia's deforestation trends are tied to soy expansion, and fire.
    * Deforestation Rates in Bolivia have increased by 259% over the last eight years driven primarily by agriculture expansion.
    * Almost three quarters of recent deforestation has taken place in the eastern departement of Santa Cruz, where most of Bolivia's soy production is located.
    * Findings from New Trase Data published in August show that the soy production in 2020 was linked to 77,090 ha of deforestation and conversion, increasing to 105,600 ha in 2021. 
    """
}

fig.update_layout(barmode='stack', xaxis_tickmode='linear')

st.write("---")
st.header("Regional Forest Loss Charts")
st.write("Select a region above and review the chart below.")
st.plotly_chart(fig)
st.write("---")

st.markdown(analysis_content.get(active_region, "### Region analysis is not available."))
st.write("### Carbon Emissions Released Based on Forest Lost")
st.write("Adjust the slider below to see how much carbon is released into the atmosphere based on the number of hectares of forest lost.")

reduction_percent = st.slider(
    "Select a Target Deforestation Reduction (%):",
    min_value=0, max_value=100, value=25, step=1)

projected_yearly_loss_ha = 4000000
co2_per_hectare_tons = 600

hectares_saved_yearly = projected_yearly_loss_ha* (reduction_percent/100)
co2_prevented_yearly_tons = hectares_saved_yearly * co2_per_hectare_tons

hectares_saved_10yr = hectares_saved_yearly * 10 
co2_prevented_10year_tons = co2_prevented_yearly_tons * 10

st.write(f"### Projected Impact over 10 years with {reduction_percent}% Reduction")

card_col1, card_col2 = st.columns(2)

with card_col1: 
    st.metric(
        label="Rainforest Area Saved",
        value=f"{hectares_saved_10yr:,.0f} Hectares",
        delta=f"+{hectares_saved_yearly:,.0f} Hectares/Year"
    )

with card_col2:
    st.metric(
        label="CO₂ Emissions Prevented", 
        value=f"{co2_prevented_10year_tons:,.0f} Metric Tons",
        delta=f"-{co2_prevented_yearly_tons:,.0f} tons / year"
    )

st.info(
    f"**Did you know?** Saving {co2_prevented_10year_tons:,.0f} metric tons of $CO_2$ is equivalent to "
    f"taking roughly { (co2_prevented_10year_tons / 4.6):,.0f} gasoline-powered passenger vehicles off the road for an entire year!"
)