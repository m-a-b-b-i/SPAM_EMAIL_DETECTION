from src.preprocess import load_and_preprocess_data
from src.train import train_model
from src.predict import predict_email

def main():
    # Load and preprocess data
    data = load_and_preprocess_data("data/spam.csv")

    # Train model
    model, vectorizer = train_model(data)

    # Test with a sample email
    email = "Congratulations! You've won a $1,000 gift card. Click here to claim now!"
    prediction = predict_email(model, vectorizer, email)
    print(f"The email is classified as: {prediction}")

if __name__ == "__main__":
    main()
