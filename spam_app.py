import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Win a free iPhone now! Click here!",
    "Congratulations! You won $1000!",
    "Free money waiting for you!",
    "Buy cheap medications online!",
    "Hey, are we still meeting tomorrow?",
    "Can you send me the homework?",
    "Lunch at 12?",
    "Your report is ready to review."
]
labels = ["spam","spam","spam","spam","ham","ham","ham","ham"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
model = MultinomialNB()
model.fit(X, labels)

st.title("Spam Email Checker")
message = st.text_area("Enter your message:")
if st.button("Check"):
    result = model.predict(vectorizer.transform([message]))
    if result[0] == "spam":
        st.error("WARNING: This is SPAM")
    else:
        st.success("SAFE: This is a real message")
