from __future__ import annotations

from collections import defaultdict

import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeRegressor


def score(clf, x, y):
    return roc_auc_score(y == 1, clf.predict_proba(x)[:, 1])


class Boosting:

    def __init__(
            self,
            base_model_params: dict = None,
            n_estimators: int = 10,
            learning_rate: float = 0.1,
            subsample: float = 0.3,
            early_stopping_rounds: int = None,
            plot: bool = False,
    ):
        self.base_model_class = DecisionTreeRegressor
        self.base_model_params: dict = {} if base_model_params is None else base_model_params

        self.n_estimators: int = n_estimators

        self.models: list = []
        self.gammas: list = []

        self.learning_rate: float = learning_rate
        self.subsample: float = subsample

        self.early_stopping_rounds: int = early_stopping_rounds
        if early_stopping_rounds is not None:
            self.validation_loss = np.full(self.early_stopping_rounds, np.inf)

        self.plot: bool = plot

        self.history = defaultdict(list)

        self.sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.loss_fn = lambda y, z: -np.log(self.sigmoid(y * z)).mean()
        self.loss_derivative = lambda y, z: -y * self.sigmoid(-y * z)
        self.n_features = None

    def fit_new_base_model(self, x, y, predictions):
        idx = np.random.randint(0, x.shape[0], int(self.subsample * x.shape[0]))
        x_boot = x[idx]
        y_boot = y[idx]
        pred_boot = predictions[idx]
        last_residuals = -self.loss_derivative(y, predictions)
        model = self.base_model_class(**self.base_model_params).fit(x_boot, last_residuals[idx])
        self.models.append(model)
        gamma = self.find_optimal_gamma(y_boot, pred_boot, pred_boot + model.predict(x_boot))

        self.gammas.append(gamma)

    def fit(self, x_train, y_train, x_valid, y_valid):
        """
        :param x_train: features array (train set)
        :param y_train: targets array (train set)
        :param x_valid: features array (validation set)
        :param y_valid: targets array (validation set)
        """
        train_predictions = np.zeros(y_train.shape[0])
        valid_predictions = np.zeros(y_valid.shape[0])
        self.history['train'] = []
        self.history['val'] = []
        self.n_features = x_train.shape[1]

        for _ in range(self.n_estimators):
            self.fit_new_base_model(x_train, y_train, train_predictions)
            model = self.models[-1]
            gamma = self.gammas[-1]
            train_predictions += self.learning_rate * gamma * model.predict(x_train)
            train_loss = self.loss_fn(train_predictions, y_train)
            val_pred = model.predict(x_valid)
            val_loss = self.loss_fn(val_pred, y_valid)
            self.history['train'].append(train_loss)
            self.history['val'].append(val_loss)

            if self.early_stopping_rounds is not None and self.early_stopping_rounds > 2:
                last_history = self.history['val'][self.early_stopping_rounds:]
                if last_history[-1] > last_history[-2] and last_history[-1] > last_history[-3]:
                    break

        if self.plot:
            plt.figure(figsize=(10, 6))
            plt.title('Train Loss', weight='bold', size=15)
            plt.plot(self.history['train'])
            plt.xlabel('Iteration', size=12)
            plt.ylabel('Loss', size=12)

    def predict_proba(self, x):
        preds = np.zeros(x.shape[0])
        for gamma, model in zip(self.gammas, self.models):
            preds += gamma * model.predict(x)

        preds = self.sigmoid(preds)
        return np.hstack([(1 - preds).reshape(-1, 1), preds.reshape(-1, 1)])

    def find_optimal_gamma(self, y, old_predictions, new_predictions) -> float:
        gammas = np.linspace(start=0, stop=1, num=100)
        losses = [self.loss_fn(y, old_predictions + gamma * new_predictions) for gamma in gammas]

        return gammas[np.argmin(losses)]

    def score(self, x, y):
        return score(self, x, y)

    @property
    def feature_importances_(self):
        w = np.zeros(self.n_features)
        for model in self.models:
            w += model.feature_importances_ 
        w /= self.n_estimators
        return w / np.sum(w)
