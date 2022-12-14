import numpy as np
import keras as k
import os
import pandas as pd
from sklearn.model_selection import train_test_split
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class MyLogger(k.callbacks.Callback):

    def __init__(self, n):
        self.n = n

    def on_epoch_end(self, epoch, logs=None):
        if logs is None:
            logs = {}
        if epoch % self.n == 0:
            curr_loss = logs.get('loss')
            curr_acc = logs.get('accuracy') * 100
            print("epoch = %4d loss = %0.6f acc = %0.2f%%" % (epoch, curr_loss, curr_acc))


def normalize_data(dt):
    min_col = []
    max_col = []
    for i in ["1", "2", "3"]:
        min_col.append(np.min(dt[i]))
        max_col.append(np.max(dt[i]))
    for i in ["1", "2", "3"]:
        dt[i] = (dt[i] - min_col[int(i) - 1]) / (max_col[int(i) - 1] - min_col[int(i) - 1])
    return dt


data = pd.read_csv('haberman.csv', dtype=float)

train = data[0:244]
test = data[244:]
train_x = train.drop(["4"], axis=1)
test_x = test.drop(["4"], axis=1)
train_y = train["4"]
test_y = test["4"]
train_x = normalize_data(train_x)
test_x = normalize_data(test_x)

my_init = k.initializers.glorot_uniform(seed=1)
model = k.models.Sequential()
model.add(k.layers.Dense(units=8, input_dim=3, activation='tanh', kernel_initializer=my_init))
model.add(k.layers.Dense(units=8, activation='tanh', kernel_initializer=my_init))
model.add(k.layers.Dense(units=1, activation='sigmoid', kernel_initializer=my_init))

simple_sgd = k.optimizers.SGD(learning_rate=0.001)
adam = k.optimizers.Adam(learning_rate=0.001)

model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])

max_epochs = 500
my_logger = MyLogger(n=50)
h = model.fit(train_x, train_y, batch_size=10, epochs=max_epochs, verbose=0, callbacks=[my_logger])

np.set_printoptions(precision=4, suppress=True)
eval_results = model.evaluate(test_x, test_y, verbose=0)
print("\nLoss, accuracy on test data: ")
print("%0.4f %0.2f%%" % (eval_results[0], eval_results[1]*100))

inpts = np.array([[0.4, 0.83, 0.076]], dtype=np.float32)
pred = model.predict(inpts)
print("\nPredicting authenticity for: ")
print(inpts)
print("Probability that class = 2: the patient died within 5 year")
print(pred)
