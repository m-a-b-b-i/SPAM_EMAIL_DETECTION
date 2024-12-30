import pandas as pd

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    print(data.columns)  # Debugging: Print the column names
    data = data[['Label', 'Message']]  # Correct column names
# Use only the necessary columns
    return data

# Correct usage of file path as a string
file_path = r"C:\\Users\\mabbi\\Desktop\\PROJECTS\\SPAM EMAIL DETECTION\\data\\spam.csv"
data = load_and_preprocess_data(file_path)
