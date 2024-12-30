def predict_email(model, vectorizer, email):
    email_vec = vectorizer.transform([email])
    prediction = model.predict(email_vec)
    return "Spam" if prediction[0] == 1 else "Not Spam"
