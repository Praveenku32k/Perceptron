"""
author: Praveen kumar
email:praveenku32k@gmail.com
phone Number: 9006336740
"""

from utils.model import Perceptron
from utils.all_utils import prepare_data, save_plot, save_model
import pandas as pd


def main(data, modelname, plotname, eta, epochs):

    df = pd.DataFrame(data)

    print(df)

    X,y = prepare_data(df)



    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()

    save_model(model, filename=modelname)
    save_plot(df, plotname, model)



if __name__ == '__main__':
    
    OR = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,1,1,1],
    }

    ETA = 0.3 # 0 and 1
    EPOCHS = 10

    main(data=OR, modelname="or.model", plotname="or.png", eta=ETA, epochs=EPOCHS)