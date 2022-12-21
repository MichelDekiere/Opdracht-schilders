import keras
import matplotlib.pyplot as plt
from IPython.display import clear_output

class RealTimePlotCallback(keras.callbacks.Callback): # erft van keras.callbacks.Callback
    """Zelf geschreven callback die de accuracy en loss in real-time afdrukt tijdens het trainen"""

    def on_train_begin(self, logs):
        self._loss = []
        self._acc = []
        self._val_loss = []
        self._val_acc = []

    def on_epoch_end(self, epoch, logs={}):
        clear_output() # vorige plot verwijderen
        plt.clf()  # clear current figure
        epochs = range(0, len(self._acc) + 1) # aantal epochs voor de x-as

        # accuracy & loss van nieuwste epoch toevoegen aan de lists die gebruikt worden voor de plots
        self._acc.append(logs.get("accuracy"))
        self._val_acc.append(logs.get("val_accuracy"))
        self._loss.append(logs.get("loss"))
        self._val_loss.append(logs.get("val_loss"))

        fig, (ax1, ax2) = plt.subplots(1, 2) # 2 plots naast elkaar zetten

        fig.set_size_inches(12, 3) # grootte van plots instellen

        # Accuracy plot
        ax1.plot(epochs, self._acc, "b-", label="Training accuracy")
        ax1.plot(epochs, self._val_acc, "r-", label="Validation accuracy")
        ax1.set_title("Training and validation accuracy")
        plt.xlabel("Epochs")
        ax1.legend()
        ax1.grid()

        # Loss plot
        ax2.plot(epochs, self._loss, "b-", label="Training loss")
        ax2.plot(epochs, self._val_loss, "r-", label="Validation loss")
        ax2.set_title("Training and validation loss")
        plt.xlabel("Epochs")
        ax2.legend()
        ax2.grid()

        plt.show() # tonen van plots

        # printen van concrete loss & accuracy cijfers
        print(f"training loss: {self._loss[-1]}")
        print(f"validation loss: {self._val_loss[-1]}")
        print(f"training accuracy: {self._acc[-1]}")
        print(f"validation accuracy: {self._val_acc[-1]}\n")
        print(f"epochs: {epoch+1}\n")