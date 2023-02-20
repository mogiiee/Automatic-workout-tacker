import streamlit as st

counter = 0

def increment_counter():
    global counter
    counter += 1

st.set_page_config(page_title="Workout Counter", page_icon=":muscle:", layout="wide")
st.title("Workout Counter")
st.markdown("### Track your progress with this workout counter")

counter = st.number_input("Enter current workout count", value=counter, step=1)

if st.button("Increment workout count"):
    counter += 1

st.write("")
st.write("Current workout count: ", counter)
st.write("")
st.write("Stay motivated and keep up the good work!")
st.write("work well")

st.title("My Beautiful Website")

# Add a button to upload images
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "gif"])

# If an image is uploaded, display it
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

# Add a button to upload GIFs
uploaded_gif = st.file_uploader("Choose a GIF", type=["gif"])

# If a GIF is uploaded, display it
if uploaded_gif is not None:
    st.image(uploaded_gif, caption="Uploaded GIF")

# Add a carousel with some example images
st.carousel(images=["https://via.placeholder.com/300.png/09f/fff",
                    "https://via.placeholder.com/300.png/0cf/fff",
                    "https://via.placeholder.com/300.png/0fc/fff",
                    "https://via.placeholder.com/300.png/ccc/fff",
                    "https://via.placeholder.com/300.png/fff/000"],
            height=300)
