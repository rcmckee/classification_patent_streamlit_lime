import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import pickle
import numpy as np
import pandas as pd

from lime import lime_text
from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidfsmall.pkl','rb'))
# def predict(patent_text):

#     id_to_category = {0:'Not 705 or 706',1:'705',2:"706"}

#     final_features = tfidf.transform([patent_text])
#     prediction = model.predict(final_features)
#     predicted_class = id_to_category[prediction[0]]

#     return predicted_class


st.title('Patent Classification') 
st.title('Streamlit Share And LIME Visualization')

txt = st.text_area('Text to analyze', '''1. A computer-implemented method comprising:
          acquiring, by a computing system, real-time image data depicting at least a portion of a face of a user of the computing system;
          analyzing, by the computing system, the real-time image data to determine a state associated with at least the portion of the face;
          providing, by the computing system, an emoji based on the state associated with at least the portion of the face; and
          inputting, by the computing system, the emoji in a communication to be made by the user.
          2. The computer-implemented method of claim 1, further comprising:
          analyzing the real-time image data to determine one or more positions of one or more specified facial features within at least the portion of the face of the user;
          identifying one or more emoji features within the emoji that are associated with the one or more specified facial features; and
          modifying the one or more emoji features based on the one or more positions of the one or more specified facial features.
          3. The computer-implemented method of claim 2, wherein the one or more specified facial features include at least one of an eye of the user, an eyebrow of the user, a nose of the user, a lip of the user, a tooth of the user, a tongue of the user, or a mouth of the user.
          4. The computer-implemented method of claim 1, further comprising:
          analyzing the real-time image data to determine that the real-time image data further depicts at least one of an object or a gesture;
          selecting a graphical representation for the at least one of the object or the gesture; and
          providing the graphical representation in conjunction with the emoji.
          5. The computer-implemented method of claim 1, wherein analyzing the real-time image data to determine the state associated with at least the portion of the face further comprises:
          analyzing one or more virtual points on at least the portion of the face to identify a virtual point arrangement; and
          matching, within an allowable deviation, the virtual point arrangement with a facial expression model out of a plurality of facial expression models.
          6. The computer-implemented method of claim 5, further comprising:
          identifying the emoji out of a plurality of emojis based on the facial expression model, wherein each of the plurality of emojis is respectively associated with each of the plurality of facial expression models.
          7. The computer-implemented method of claim 5, wherein matching the virtual point arrangement with the facial expression model is based on at least one of a machine learning training process or a crowdsource training process.
          8. The computer-implemented method of claim 1, further comprising:
          analyzing the real-time image data to determine a second state associated with at least the portion of the face; and
          updating, based on the second state associated with at least the portion of the face, the emoji provided.
          9. The computer-implemented method of claim 1, further comprising:
          publishing the communication as at least one of a message, a journal entry, a diary entry, a blog entry, a comment, a response, or a post.
          10. The computer-implemented method of claim 1, further comprising:
          dynamically presenting a preview of the emoji prior to inputting the emoji in the communication to be made by the user.
          ''')
if st.button('Predict Patent Class', key=None):
    c = make_pipeline(tfidf, model)
    class_names = ['700','705','706']
    explainer = LimeTextExplainer(class_names=class_names)
    exp = explainer.explain_instance(txt, c.predict_proba, num_features=6, top_labels=1)
    # Display explainer HTML object
    components.html(exp.as_html(), height=800)