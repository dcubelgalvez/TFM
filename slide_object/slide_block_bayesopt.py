import bayesopt
import numpy as np
import slide_block_function as sbf
import pickle

function = sbf.SlideBlock()  # Inicializacion

n = 5  # n dimensions
lb = np.array([-0.3, -0.3, 0, 0.05, 0])
ub = np.array([0.3, 0.3, 0.2, 0.3, np.pi])

params = {'n_iterations': 500,
          'n_iter_relearn': 10,
          'n_init_samples': 2*n}

listas = []
n_experimentos = 5

for i in range(n_experimentos):
    function.clean_lists()
    mvalue, x_out, error = bayesopt.optimize(function.slide_block, n, lb, ub, params)
    print("Result", mvalue, "at", x_out)
    listas_optimizacion = function.return_lists()
    listas.append(listas_optimizacion)

pickle.dump(listas, open("listas_bayesopt_slideblock.p", "wb"))

function.shutdown()  # Apagado
