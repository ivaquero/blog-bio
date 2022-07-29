def load_fashion_mnist():

    X = np.load(file="../../datasets/handson/fashion_mnist_X.npz")
    y = np.load(file="../../datasets/handson/fashion_mnist_y.npz")
    X_train_full, X_test = X["train"], X["test"]
    y_train_full, y_test = y["train"], y["test"]
    X_train_full = X_train_full / 255.0
    X_test = X_test / 255.0
    X_valid, X_train = X_train_full[:5000], X_train_full[5000:]
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

    return X_train, y_train, X_valid, y_valid, X_test, y_test