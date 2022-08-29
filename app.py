from itertools import count
from operator import le
from click import option
from matplotlib import container
from pyparsing import col
import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from textblob import TextBlob


Leads_basic_details = pd.read_csv("D:\ED_Tech_Analysis\Data\leads_basic_details.csv")  
Leads_demo_watched_details = pd.read_csv("D:\ED_Tech_Analysis\Data\leads_demo_watched_details.csv")
Leads_interaction_details = pd.read_csv("D:\ED_Tech_Analysis\Data\leads_interaction_details.csv")
Leads_reasons_for_no_interest = pd.read_csv("D:\ED_Tech_Analysis\Data\leads_reasons_for_no_interest.csv")

# Merged Awarness Dataset 
Awarness_data = pd.merge(Leads_basic_details,Leads_demo_watched_details,how='inner')

# Merged Interaction Dataset
interaction_data = pd.merge(Awarness_data,Leads_interaction_details,how="inner")

#-------------------------Introduction-------------------------------------

with st.container():
    st.title("Hello, Myself Rishikesh Chakraborty")
    st.text("Here i'm presenting you a dasboard based on Customer Acquisition - Call")
    st.text("interaction flow")
#-----------------------Horizontal Menu-----------------------------------

selected = option_menu (
    menu_title="Customer Acquisition Analysis",
    options = ["Demography Analysis","Awarness Analysis","Interaction Analysis","Sentiment Analysis"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    
)
    
###======================================================= Demography Analysis================================================================
if selected == "Demography Analysis":
   with st.container():
       st.subheader("Demography Analysis")
 
   with st.container():
    left_cont1,right_cont1 = st.columns(2)
    with left_cont1:
      st.subheader("Leads Age analysis")
      Leads_basic_details.drop(Leads_basic_details[Leads_basic_details.age > 50].index,inplace=True)
      bins = [15,19,22,25]
      labels = ["16-19","20-22","23-25"]
      Leads_basic_details["age_group"] = pd.cut(Leads_basic_details["age"],bins=bins,labels=labels)
      fig1 = px.histogram(Leads_basic_details,x = "age_group")
      st.plotly_chart(fig1, use_container_width=True)
    with right_cont1:
      st.subheader("Leads Gender analysis")
      fig2 = px.histogram(Leads_basic_details,x = "gender")
      st.plotly_chart(fig2, use_container_width=True)
      
   with st.container():
    left_cont2,right_cont2 = st.columns(2)
    with left_cont2:
        st.subheader("Leads City analysis")
        fig3 = px.histogram(Leads_basic_details,x = "current_city")
        st.plotly_chart(fig3, use_container_width=True)
    with right_cont2:
        st.subheader("Leads Education analysis")
        fig4 = px.histogram(Leads_basic_details,x = "current_education")
        st.plotly_chart(fig4, use_container_width=True)

   with st.container():
    left_cont3,right_cont3 = st.columns(2)
    with left_cont3:
        st.subheader("Leads Parents Occupation analysis")
        fig5 = px.histogram(Leads_basic_details,x = "parent_occupation")
        st.plotly_chart(fig5, use_container_width=True)
    with right_cont3:
        st.subheader("Lead Generation analysis")
        fig6 = px.histogram(Leads_basic_details,x = "lead_gen_source")
        st.plotly_chart(fig6, use_container_width=True)

######################################################################################################################################################

###==========================================================Awarness Analysis=========================================================================

if selected == "Awarness Analysis":
   with st.container():
       st.subheader("Awarness Analysis")
 
   with st.container():
    left_cont4,right_cont4 = st.columns(2)
    with left_cont4:
      st.subheader("Leads Retention analysis")
      Awarness_data.drop(Awarness_data[Awarness_data.watched_percentage > 150].index,inplace=True)
      bins = [1,10,20,30,40,50,60,70,80,90,100]
      labels = ["1-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]
      Awarness_data["watched_percentage_group"] = pd.cut(Awarness_data["watched_percentage"],bins=bins,labels=labels)
      fig7 = px.histogram(Awarness_data,x = "watched_percentage_group",color="language")
      st.plotly_chart(fig7, use_container_width=True)
    with right_cont4:
      st.subheader("Leads Language analysis")
      fig8 = px.histogram(Awarness_data,x = "language")
      st.plotly_chart(fig8, use_container_width=True)
      
   with st.container():
    #Leads City analysis by language & Watch Time
     st.subheader("Leads City analysis by language & watch time")
     fig91 = px.sunburst(Awarness_data,path = ["current_city","language","watched_percentage_group"])
     fig91.update_traces(textinfo="label+percent parent")
     st.plotly_chart(fig91, use_container_width=True)
    
    #Leads Education Analysis by Language & Watch Time
     st.subheader("Leads Education analysis by language & watch time")
     fig92 = px.sunburst(Awarness_data,path = ["current_education","language","watched_percentage_group"])
     fig92.update_traces(textinfo="label+percent parent")
     st.plotly_chart(fig92, use_container_width=True)
     
     #Leads Parents Ocupation Analysis by Language & Watch Time
     #st.subheader("Leads Parents Ocupation analysis by language & watch time")
     #fig93 = px.sunburst(Awarness_data,path = ["parent_occupation","language","watched_percentage_group"])
     #fig93.update_traces(textinfo="label+percent parent")
     #st.plotly_chart(fig93, use_container_width=True)
     
     #Leads Lead Generation Analysis by Language & Watch Time
     st.subheader("Lead Generation analysis by language & watch time")
     fig94 = px.sunburst(Awarness_data,path = ["lead_gen_source","language","watched_percentage_group"])
     fig94.update_traces(textinfo="label+percent parent")
     st.plotly_chart(fig94, use_container_width=True)
     
     #Leads Gender Analysis by Language & Watch Time
     st.subheader("Lead Gender analysis by language & watch time")
     fig95 = px.sunburst(Awarness_data,path = ["gender","language","watched_percentage_group"])
     fig95.update_traces(textinfo="label+percent parent")
     st.plotly_chart(fig95, use_container_width=True)

######################################################################################################################################################

###==========================================================Interaction Analysis=========================================================================
     
if selected == "Interaction Analysis":
   
  with st.container():
    st.subheader("Interaction Analysis on Basis of Lead Stage")
  
  with st.container():
    left_cont5,right_cont5 = st.columns(2)
    with left_cont5:
      st.subheader("Leads Age analysis")
      interaction_data.drop(interaction_data[interaction_data.age > 50].index,inplace=True)
      bins = [15,19,22,25]
      labels = ["16-19","20-22","23-25"]
      interaction_data["age_group"] = pd.cut(interaction_data["age"],bins=bins,labels=labels)
      fig96 = px.histogram(interaction_data,x = "age_group",color="lead_stage")
      st.plotly_chart(fig96, use_container_width=True)
    with right_cont5:
      st.subheader("Leads Gender analysis")
      fig97 = px.histogram(interaction_data,x = "gender",color="lead_stage")
      st.plotly_chart(fig97, use_container_width=True)
      
  with st.container():
    left_cont6,right_cont6 = st.columns(2)
    with left_cont6:
        st.subheader("Leads City analysis")
        fig98 = px.histogram(interaction_data,x = "current_city",color="lead_stage")
        st.plotly_chart(fig98, use_container_width=True)
    with right_cont6:
        st.subheader("Leads Education analysis")
        fig99 = px.histogram(interaction_data,x = "current_education",color="lead_stage")
        st.plotly_chart(fig99, use_container_width=True)

  with st.container():
    left_cont7,right_cont7 = st.columns(2)
    with left_cont7:
        st.subheader("Leads Parents Occupation analysis")
        fig100 = px.histogram(interaction_data,x = "parent_occupation",color="lead_stage")
        st.plotly_chart(fig100, use_container_width=True)
    with right_cont7:
        st.subheader("Lead Generation analysis")
        fig101 = px.histogram(interaction_data,x = "lead_gen_source",color="lead_stage")
        st.plotly_chart(fig101, use_container_width=True)
    
  with st.container():
    st.subheader("Interaction Analysis on Basis of Lead Stage")
  
  with st.container():
    left_cont8,right_cont8 = st.columns(2)
    with left_cont8:
      st.subheader("Leads Age analysis")
      interaction_data.drop(interaction_data[interaction_data.age > 50].index,inplace=True)
      bins = [15,19,22,25]
      labels = ["16-19","20-22","23-25"]
      interaction_data["age_group"] = pd.cut(interaction_data["age"],bins=bins,labels=labels)
      fig96 = px.sunburst(interaction_data,path = ["age_group","call_reason"])
      fig96.update_traces(textinfo="label+percent parent")
      st.plotly_chart(fig96, use_container_width=True)
    with right_cont8:
      st.subheader("Leads Gender analysis")
      fig97 = px.sunburst(interaction_data,path = ["gender","call_reason"])
      fig97.update_traces(textinfo="label+percent parent")
      st.plotly_chart(fig97, use_container_width=True)
      
  with st.container():
    left_cont9,right_cont9 = st.columns(2)
    with left_cont9:
        st.subheader("Leads City analysis")
        fig98 = px.sunburst(interaction_data,path = ["current_city","call_reason"])
        fig98.update_traces(textinfo="label+percent parent")
        st.plotly_chart(fig98, use_container_width=True)
    with right_cont9:
        st.subheader("Leads Education analysis")
        fig99 = px.sunburst(interaction_data,path = ["current_education","call_reason"])
        fig99.update_traces(textinfo="label+percent parent")
        st.plotly_chart(fig99, use_container_width=True)

  with st.container():
    left_cont10,right_cont10 = st.columns(2)
    with left_cont10:
        st.subheader("Leads Parents Occupation analysis")
        fig100 = px.sunburst(interaction_data,path = ["parent_occupation","call_reason"])
        fig100.update_traces(textinfo="label+percent parent")
        st.plotly_chart(fig100, use_container_width=True)
    with right_cont10:
        st.subheader("Lead Generation analysis")
        fig101 = px.sunburst(interaction_data,path = ["lead_gen_source","call_reason"])
        fig101.update_traces(textinfo="label+percent parent")
        st.plotly_chart(fig101, use_container_width=True)

######################################################################################################################################################

###==========================================================Sentiment Analysis=========================================================================

if selected == "Sentiment Analysis":
   
  with st.container():
    st.subheader("Sentiment Analysis")
  
  with st.container():
    st.subheader("Reason for Not interested in demo")
    reasons_for_not_interested_in_demo = pd.DataFrame(Leads_reasons_for_no_interest.iloc[:,0:2])
    reasons_for_not_interested_in_demo = reasons_for_not_interested_in_demo.dropna()
    reasons_for_not_interested_in_demo["sentiment"] = reasons_for_not_interested_in_demo['reasons_for_not_interested_in_demo'].apply(lambda x: 'NaN' if pd.isnull(x) else TextBlob(x).sentiment.polarity)
    fig102 = px.line(reasons_for_not_interested_in_demo, y="sentiment", x="lead_id", hover_name = "reasons_for_not_interested_in_demo" ,markers=True)
    st.plotly_chart(fig102, use_container_width=True)
  
  with st.container():
    st.subheader("Reason for Not interested to Consider")
    reasons_for_not_interested_to_consider = pd.DataFrame(Leads_reasons_for_no_interest[["lead_id","reasons_for_not_interested_to_consider"]])
    reasons_for_not_interested_to_consider = reasons_for_not_interested_to_consider.dropna()
    reasons_for_not_interested_to_consider["sentiment"] = reasons_for_not_interested_to_consider['reasons_for_not_interested_to_consider'].apply(lambda x: 'NaN' if pd.isnull(x) else TextBlob(x).sentiment.polarity)
    fig103 = px.line(reasons_for_not_interested_to_consider, y="sentiment", x="lead_id",hover_name = "reasons_for_not_interested_to_consider", markers=True)
    st.plotly_chart(fig103, use_container_width=True)
  
  with st.container():
    st.subheader("Reason for Not interested to Convert")
    reasons_for_not_interested_to_convert = pd.DataFrame(Leads_reasons_for_no_interest[["lead_id","reasons_for_not_interested_to_convert"]])
    reasons_for_not_interested_to_convert = reasons_for_not_interested_to_convert.dropna()
    reasons_for_not_interested_to_convert["sentiment"] = reasons_for_not_interested_to_convert['reasons_for_not_interested_to_convert'].apply(lambda x: 'NaN' if pd.isnull(x) else TextBlob(x).sentiment.polarity)
    fig104 = px.line(reasons_for_not_interested_to_convert, y="sentiment", x="lead_id",hover_name="reasons_for_not_interested_to_convert", markers=True)
    st.plotly_chart(fig104, use_container_width=True)