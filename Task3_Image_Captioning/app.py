import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


# Load model
@st.cache_resource
def load_model():

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model

processor, model = load_model()

# Page
st.title("AI Image Caption Generator")

st.write(
    "Upload an image and AI will generate a caption"
)


uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg","png","jpeg"]
)


if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


    if st.button("Generate Caption"):

        inputs = processor(
            images=image,
            return_tensors="pt"
        )


        output = model.generate(
            **inputs,
            max_new_tokens=50
        )


        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )


        st.success(
            caption
        )