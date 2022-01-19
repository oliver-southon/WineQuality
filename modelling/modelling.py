import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, mean_squared_error

def get_model_fit():
    TEST_SIZE = 0.2

    # Load DataFrame
    df = pd.read_csv("data/winequality_white.csv", header=0, sep=";")

    # Create Category (Label)
    df["quality_category"] = pd.cut(df["quality"], bins=[0, 5, 9], labels=["poor", "good"])

    # Creaete dummies to convert to numerical values
    df_dummies = pd.get_dummies(df, drop_first=True)

    # Get target and features
    target = df_dummies["quality_category_good"]
    features = df_dummies.drop(["quality_category_good", "quality"], axis=1)

    # Split Data Into Train/Test
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2) # 8 is my lucky number

    #   Normalise the Data
    normalise = MinMaxScaler()
    fit = normalise.fit(X_train)
    X_train = fit.transform(X_train)
    X_test = fit.transform(X_test)

    # Create Model
    model = RandomForestClassifier(random_state=8)
    model.fit(X_train, y_train)

    return model, fit





