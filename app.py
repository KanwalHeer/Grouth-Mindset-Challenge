import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge By Kanwal Heer", page_icon="🌱")

# Homepage
st.title("🌱 Growth Mindset Challenge")
st.write("""
Welcome to the Growth Mindset Challenge! This app is designed to help you develop a growth mindset, 
embrace challenges, and achieve your full potential. Created by **Kanwal Heer**.
""")

# Inspirational Quote
st.header("Daily Inspiration")
st.write("Here’s a quote to motivate you:")
st.success("“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt")

# Interactive Quiz
st.header("What’s Your Mindset?")
st.write("Take this short quiz to find out if you have a fixed or growth mindset.")

question1 = st.radio("1. When faced with a challenge, I tend to:", 
                     ["Avoid it", "Give up easily", "Embrace it and learn from it"])
question2 = st.radio("2. I believe my intelligence and abilities are:", 
                     ["Fixed and unchangeable", "Can improve with effort", "Not sure"])
question3 = st.radio("3. When I make a mistake, I:", 
                     ["Feel ashamed", "Ignore it", "Learn from it and try again"])

if st.button("Submit Quiz"):
    score = 0
    if question1 == "Embrace it and learn from it":
        score += 1
    if question2 == "Can improve with effort":
        score += 1
    if question3 == "Learn from it and try again":
        score += 1
    
    if score >= 2:
        st.success("You have a Growth Mindset! Keep up the great work!")
    else:
        st.warning("You may have a Fixed Mindset. Don’t worry—adopting a growth mindset is a journey!")

# Resources Section
st.header("Resources to Learn More")
st.write("Here are some resources to help you develop a growth mindset:")
st.markdown("- [Carol Dweck’s TED Talk](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")
st.markdown("- [Mindset: The New Psychology of Success (Book)](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)")
st.markdown("- [Growth Mindset Activities](https://www.mindsetworks.com/)")

# Daily Challenge
st.header("Daily Challenge")
st.write("Here’s your challenge for today:")
st.info("Try something new that you’ve been afraid to attempt. Reflect on what you learned from the experience.")

# User Feedback
st.header("Share Your Experience")
feedback = st.text_area("How has the Growth Mindset Challenge helped you? Share your thoughts:")
if st.button("Submit Feedback"):
    st.success("Thank you for sharing! Your feedback helps us improve.")

# Signature at the Bottom
st.write("\n")
st.write("Created with ❤️ by **Kanwal Heer**.")
