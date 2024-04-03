import numpy as np
from scipy.optimize import minimize

def least_squares(A, b, constraints):
    """
    
    
    """
    def objective(x):
        return np.linalg.norm(A @ x - b)**2
    
    def constraint(x):
        for lower_bound, upper_bound  in constraints:
            if lower_bound > x[0] or x[0] > upper_bound:
                return np.inf
        return 0
    
    if __name__ == "__main__":
        A = np.array([[1, 2], [3, 4]])
        b = np.array([5, 6])
        constraints = [(0, 10)]

        x = minimize(objective, x0=np.array([0, 0]), constraints={'type': 'eq', 'fun': constraint})
        print(x)