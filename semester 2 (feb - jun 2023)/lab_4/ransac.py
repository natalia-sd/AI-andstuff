import numpy as np
import matplotlib.pyplot as plt
import line

"""
RANSAC for 2d lines module:

Algorithm:

I Hypotesis generation Stage
1. Sample 2d points (1. 2 points; 2. 5 points)
2. Model estimation (1. analytics; 2. MSE estimation)

II Hypotesis evaluation Stage

3. Inlier counting (%inlier > threshold) 
    if True -> best params
    if False -> 1.
4. # iter > num_iter?

"""
import numpy as np
import matplotlib.pyplot as plt
from line import Line

class RANSAC:
    """
    RANSAC algo class
    """
    def __init__(self) -> None:
        self.iter_num: int = 100
        self.n_pointsy: int = 2
        self.inlin_thrsh: float = 0.8
        self.epsilon: float = 0.1
        self.best_params: dict = {}
        self.inliers_x: list = []
        self.inliers_y: list = []
        self.outliers_x: list = []
        self.outliers_y: list = []
        self.score: int = 0
        self.x: np.ndarray = None
        self.y: np.ndarray = None

    def set_case(self, case_params) -> None:
        if 'iter_num' in case_params.keys():
            self.iter_num = case_params['iter_num']
        if 'n_pointsy' in case_params.keys():
            self.n_pointsy = case_params['n_pointsy']
        if 'inlin_thrsh' in case_params.keys():
            self.inlin_thrsh = case_params['inlin_thrsh']
        if 'epsilon' in case_params.keys():
            self.epsilon = case_params['epsilon']
        if not ('x' in case_params.keys() and 'y' in case_params.keys()):
            raise ValueError(f"case_params обязан включать в себя ключи 'x' и 'y'")
        self.x = case_params['x']
        self.y = case_params['y']

    def clear_case(self) -> None:
        self.__init__()

    def fit(self) -> None:
        for i in range(self.iter_num):
            ind = range(len(self.x))
            ind_sampl = np.random.choice(ind, self.n_pointsy)
            x_sampl = self.x[ind_sampl]
            y_sampl = self.y[ind_sampl]
            line = Line(x_sampl, y_sampl)
            line.estimate_params()
            inliers_x, inliers_y, outliers_x, outliers_y = line.devide_points(self.x, self.y, self.epsilon)
            score = len(inliers_x) / len(self.x)
            if score > self.score:
                k, b = line.get_params()
                self.best_params = {'k': k, 'b': b}
                self.score = score
                self.inlinears_x = inliers_x
                self.inlinears_y = inliers_y
                self.outliers_x = outliers_x
                self.outliers_y = outliers_y

    def draw(self) -> None:
        plt.plot(self.inliers_x, self.inliers_y, 'o', label='inliers')
        plt.plot(self.outliers_x, self.outliers_y, 'o', label='outliers')
        plt.plot(self.x, self.best_params['k'] * self.x + self.best_params['b'], 'r', label='Fitted line')
        plt.legend()
        plt.show()


    # def __init__(self) -> None:
    #         self.iter_num: int = 100
    #         self.line_points: int = 2 # сколько точек, по которым строим линию
    #         self.inlin_thrsh: float = 0.8
    #         self.epsilon: float = 0.1
    #         self.best_params: dict = {}
    #         self.inliers_x: list = []
    #         self.inliers_y: list = []
    #         self.outliers_x: list = []
    #         self.outliers_y: list = []
    #         self.score: int = 0
    #         self.x_points: np.ndarray = None
    #         self.y_points: np.ndarray = None

    # # Задаём конкретную проверку
    # def set_case(self, case_params) -> None:
    #     if 'iter_num' in case_params.keys():   # проверка наличия ключа iter_num
    #         self.iter_num = case_params['iter_num']  # задаём ключ в case_params
    #     if 'line_points' in case_params.keys():  # аналогично для остального
    #         self.n_pointsy = case_params['line_points']
    #     if 'inlin_thrsh' in case_params.keys():
    #         self.inlin_thrsh = case_params['inlin_thrsh']
    #     if 'epsilon' in case_params.keys():
    #         self.epsilon = case_params['epsilon']
    #     if not ('x' in case_params.keys() and 'y' in case_params.keys()):
    #         raise ValueError(f"case_params обязан включать в себя ключи 'x' и 'y'")
    #     self.x_points = case_params['x']
    #     self.y_points = case_params['y']

    # # очищаем значения кейса
    # def clear_case(self) -> None:
    #     self.__init__()

    # def fit(self) -> None:
    #     for i in range(self.iter_num):
    #         ind = range(len(self.x_points))  # массив от 0 до кол-ва данных
    #         ind_samples = np.random.choice(ind, self.line_points)  # кол-во данных для построения
    #         # разделяем на x и y для упрощения использования numpy-функций
    #         x_samples = self.x_points[ind_samples]
    #         y_samples = self.y_points[ind_samples]
    #         line = Line(x_samples, y_samples)
    #         line.estimate_params()
    #         # разбиваем на in и out (по x и y)
    #         inlrs_x, inlrs_y, outlrs_x, outlrs_y = line.divide_points(self.x_points, self.y_points, self.epsilon)
    #         score = len(inlrs_x) / len(self.x_points) # accuracy
    #         if score > self.score:
    #             k, b = line.get_params()
    #             self.best_params = [k, b]
    #             self.score = score
    #             self.inliers_x = inlrs_x
    #             self.inliers_y = inlrs_y
    #             self.outliers_x = outlrs_x
    #             self.outliers_y = outlrs_y


    # def draw(self) -> None:
    #     plt.plot(self.inlinears_x, self.inlinears_y, 'x', label='inlinears')
    #     plt.plot(self.outliers_x, self.outliers_y, 'x', label='outliers')
    #     plt.plot(self.x_points, self.best_params[0] * self.x_points + self.best_params[1], 'r', label='Fitted line')
    #     plt.legend()
    #     plt.show()