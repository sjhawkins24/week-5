import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''The cliche with the Titanic is the saying 'Women and children' first.  \
This would make you think that women and children would have a significantly higher survival \
rate than men. But this was also a time with stark socioeconomic divides, so the question is: \
Do women and children have higher survival rates across all passenger classes?"

'''
)
# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
'''
I would like to know if there is a relationship between class and family size. On one hand, I \
         could see first class passangers having more family members on board because they inherently come \
         from families with more weatlth. On the other hand, I could see third class passangers having \
         more family memebers on board because if you are taking a big family, you probably want the least \
         expensive ticket. 
'''
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
#fig3 = visualize_family_size()
#st.plotly_chart(fig3, use_container_width=True)