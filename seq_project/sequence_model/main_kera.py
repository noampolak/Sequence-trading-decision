import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from .trade_models import trade_dec_model
from helpers import to_one_hot
import sklearn
import seaborn as sns
from sklearn.metrics import confusion_matrix
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Dense, Input, Dropout, LSTM, Activation
# from tensorflow.keras.preprocessing import sequence
# from tensorflow.keras.initializers import glorot_uniform
import keras
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform

mpl.rcParams['figure.figsize'] = (12, 10)
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']



METRICS = [
      keras.metrics.TruePositives(name='tp'),
      keras.metrics.FalsePositives(name='fp'),
      keras.metrics.TrueNegatives(name='tn'),
      keras.metrics.FalseNegatives(name='fn'), 
      keras.metrics.CategoricalAccuracy(name='c_accuracy'),
      keras.metrics.CategoricalCrossentropy(name='c_crossentropy'),
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall'),
      keras.metrics.AUC(name='auc'),
]

early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_recall', 
    verbose=1,
    patience=30,
    mode='max',
    restore_best_weights=True)

def build_model(X, Y, model_type):
    data_shape = (X.shape)[-2:]
    print('data_shape = ' , data_shape)
    Y_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y)
    try:
        model = trade_dec_model(data_shape, Y_one_hot.shape[1])
    except:
        # case Y is binary vector
        model = trade_dec_model(data_shape, 1)
    return model

def analize_model(model):
    model.summary()
def compile_model(model, loss='categorical_crossentropy' , optimizer='adam',metrics=METRICS): 
    
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


def fit_model(model, X, Y, epochs =50, batch_size =32, shuffle=True,class_weight=None):
    Y_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y)
    baseline_history = model.fit(X, Y_one_hot, epochs = epochs, batch_size = batch_size, shuffle=shuffle,class_weight=class_weight)

def fit_plus_val_model(model, X, Y, val_features, val_labels, epochs =50, batch_size =200, shuffle=True,class_weight=None):
    Y_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y)
    baseline_history = model.fit(X, Y_one_hot, epochs = epochs, batch_size = batch_size, shuffle=shuffle,class_weight=class_weight, callbacks=[early_stopping],validation_data=(val_features, val_labels))
    return baseline_history
    
def evaluate_model(model, X_test, Y_test, batch_size =32, callbacks=['BaseLogger']):
    print("X_test shape  = ", X_test.shape)
    print("Y_test shape  = ", Y_test.shape)
    Y_test_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y_test)
    score = model.evaluate(X_test, Y_test_one_hot, batch_size)
    print("Test score = ", score)
    
def predict_model(model, X_test):
    return model.predict(X_test)

def save_model(model,filename):
    model.save(filename)

def plot_metrics(history):
  metrics = ['loss', 'auc', 'precision', 'recall']
  for n, metric in enumerate(metrics):
    name = metric.replace("_"," ").capitalize()
    plt.subplot(2,2,n+1)
    plt.plot(history.epoch, history.history[metric], color=colors[0], label='Train')
    plt.plot(history.epoch, history.history['val_'+metric],
             color=colors[0], linestyle="--", label='Val')
    plt.xlabel('Epoch')
    plt.ylabel(name)
    if metric == 'loss':
      plt.ylim([0, plt.ylim()[1]])
    elif metric == 'auc':
      plt.ylim([0.8,1])
    else:
      plt.ylim([0,1])

    plt.legend()

def plot_cm(labels, predictions, p=0.5):
  cm = confusion_matrix(labels, predictions > p)
  plt.figure(figsize=(5,5))
  sns.heatmap(cm, annot=True, fmt="d")
  plt.title('Confusion matrix @{:.2f}'.format(p))
  plt.ylabel('Actual label')
  plt.xlabel('Predicted label')

  print('Legitimate Transactions Detected (True Negatives): ', cm[0][0])
  print('Legitimate Transactions Incorrectly Detected (False Positives): ', cm[0][1])
  print('Fraudulent Transactions Missed (False Negatives): ', cm[1][0])
  print('Fraudulent Transactions Detected (True Positives): ', cm[1][1])
  print('Total Fraudulent Transactions: ', np.sum(cm[1]))

def plot_roc(name, labels, predictions, **kwargs):
  fp, tp, _ = sklearn.metrics.roc_curve(labels, predictions)

  plt.plot(100*fp, 100*tp, label=name, linewidth=2, **kwargs)
  plt.xlabel('False positives [%]')
  plt.ylabel('True positives [%]')
  plt.xlim([-0.5,20])
  plt.ylim([80,100.5])
  plt.grid(True)
  ax = plt.gca()
  ax.set_aspect('equal')