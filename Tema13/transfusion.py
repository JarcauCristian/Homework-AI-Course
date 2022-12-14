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
    for i in ["Recency(months)", "Frequency(times)", "Monetary(c.c.blood)", "Time(months)"]:
        min_col.append(np.min(dt[i]))
        max_col.append(np.max(dt[i]))
    c = 0
    for i in ["Recency(months)", "Frequency(times)", "Monetary(c.c.blood)", "Time(months)"]:
        dt[i] = (dt[i] - min_col[c]) / (max_col[c] - min_col[c])
        c += 1
    return dt


data = pd.read_csv('transfusion.csv', dtype=float)

train = data[0:598]
test = data[598:]
train_x = train.drop(["Result"], axis=1)
test_x = test.drop(["Result"], axis=1)
train_y = train["Result"]
test_y = test["Result"]
train_x = normalize_data(train_x)
test_x = normalize_data(test_x)

my_init = k.initializers.glorot_uniform(seed=1)
model = k.models.Sequential()
model.add(k.layers.Dense(units=8, input_dim=4, activation='tanh', kernel_initializer=my_init))
model.add(k.layers.Dense(units=8, activation='tanh', kernel_initializer=my_init))
model.add(k.layers.Dense(units=1, activation='sigmoid', kernel_initializer=my_init))

simple_sgd = k.optimizers.SGD(learning_rate=0.0001)

model.compile(loss='binary_crossentropy', optimizer=simple_sgd, metrics=['accuracy'])

max_epochs = 500
my_logger = MyLogger(n=50)
h = model.fit(train_x, train_y, batch_size=32, epochs=max_epochs, verbose=0, callbacks=[my_logger])

np.set_printoptions(precision=4, suppress=True)
eval_results = model.evaluate(test_x, test_y, verbose=0)
print("\nLoss, accuracy on test data: ")
print("%0.4f %0.2f%%" % (eval_results[0], eval_results[1]*100))

inpts = np.array([[0.4, 0.83, 0.076, 0.3]], dtype=np.float32)
pred = model.predict(inpts)
print("\nPredicting authenticity for: ")
print(inpts)
print("Probability that class = 2: the patient died within 5 year")
print(pred)
