import numpy as np
import matplotlib.pyplot as plt

from util import getData

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def main():
    X, Y = getData(balance_ones=False)

    # 48by48 = 2304 dimensions per sample

    # Data structure
    # 0-48 one row
    # 48-96 second row and so on

    # infinite loop. Break out of it by via input
    while True:
        # loop through 7 emotions
        for i in range(7):
            x, y = X[Y==i], Y[Y==i]  # choose all the data points that equal to this emotion
            N = len(y)  # number of data points equals to this emotion
            j = np.random.choice(N)  # randomly select this point
            plt.imshow(x[j].reshape(48, 48), cmap='gray')  # plot this point. Reshape it
            plt.title(label_map[y[j]])  # plot the label - emotion
            plt.show()
        prompt = input('Quit? Enter Y:\n')
        if prompt == 'Y':
            break


if __name__ == '__main__':
    main()

