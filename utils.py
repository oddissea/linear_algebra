import numpy as np
import sympy as sp

class MatrixWriter:
    def __init__(self):
        # Validate the input matrix
        pass

    def __is_valid_matrix(self, matrix):
        # Check if the matrix is either a numpy ndarray or a sympy Matrix
        return isinstance(matrix, (np.ndarray, sp.Matrix))

    def __convert_to_sympy(self, matrix):
        A_inv_sym = sp.Matrix(matrix)
        return A_inv_sym.applyfunc(lambda x: sp.Rational(x).limit_denominator())
        
    def __is_vector(self):
        if isinstance(self.matrix, np.ndarray):
            # Check if numpy array is 1D
            return self.matrix.ndim == 1
        elif isinstance(self.matrix, sp.Matrix):
            # Check if sympy Matrix is effectively a vector (1 row or 1 column)
            return self.matrix.shape[0] == 1 or self.matrix.shape[1] == 1
        return False

    # Create a function to display the matrix in Markdown format
    def __write_matrix(self):
        # Convert the matrix to a LaTeX formatted string
        matrix_str = '\\\\\n'.join([' & '.join(sp.latex(entry) for entry in row) 
                                    for row in self.matrix.tolist()])
        # Final format of the matrix in LaTeX
        return fr"\begin{{bmatrix}} {matrix_str} \end{{bmatrix}}"        

    def __call__(self, matrix, name=""):
        if not self.__is_valid_matrix(matrix):
            raise ValueError("Only numpy or sympy matrices or vectors are accepted.")
        # self.matrix = matrix
        self.matrix = self.__convert_to_sympy(matrix)
        return self.__write_matrix()