import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

'''
# Venn-Gogh
## 2 Group Venn Diagram

This project came about while I was trying to look for a venn diagram generator online.
The ones that I came across either does not scale according to the group size, or I 
have to draw them out manually.

"Venn-Gogh" aims to help you produce a scaled venn diagram with minimal effort & coding, 
which you can then save the chart to your presentation or document. 

If you like this awesome web app, you can consider "[buying me a coffee](https://www.buymeacoffee.com/bernard)".
'''

# Group1 vs Group2 (input here)
st.sidebar.subheader(body="Input Parameters")

chart_title = st.sidebar.text_input(label='Chart Title', value="Input Chart Title (50chars)", max_chars=50)

group1_label = st.sidebar.text_input(label='Group 1 Label', value="Group 1 Name (30chars)", max_chars=30)
group1 = st.sidebar.number_input(label='Group 1 Size', value=100, format='%g')
group2_label = st.sidebar.text_input(label='Group 2 Label', value="Group 2 Name (30chars)", max_chars=30)
group2 = st.sidebar.number_input(label='Group 2 Size', value=100)
overlap = st.sidebar.number_input(label='Overlap Size', value=25)

# plot venn diagram
plt.figure(figsize=(10,8)) #set chart area and background colour, use facecolor='None' for transparent background
venn_chart = venn2(subsets=[group1, group2, overlap],  
                set_labels=([group1_label, group2_label]),  
                set_colors=['#2b71a8', '#fe5f55'], #change circle's colour, comment out to use default colour 
                subset_label_formatter=lambda x: f"{x:,}") #change to 1.2% for 2 decimal place, comment out when using integer
for text in venn_chart.set_labels:
    text.set_fontsize(14) #set label's fontsize 
    text.set_color('#16697a') #set label's font colour
for text in venn_chart.subset_labels:
    text.set_fontsize(18) #set circle's value fontsize 
    text.set_color('#495057') #set circle's value font colour
    text.set_alpha(1) #set circle's value font transparency, 0 as full transparent
plt.title(chart_title, fontsize=22, color='#16697a') #set title

# show it!
st.pyplot()