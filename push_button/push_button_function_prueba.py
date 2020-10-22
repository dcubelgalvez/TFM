import numpy as np
import push_button.push_button_function as fun
import pickle

TASK_NAME = "push_button"
# coords_type = "esfericas"

file = "solucion_bayesopt_" + TASK_NAME + ".p"
wp_params = pickle.load(open(file, "rb"))
print(wp_params[0])

function = fun.PushButton(headless_mode=False)  # Inicializacion

push_params = np.array([0.0685, 0.0, -0.1187, 0.0, np.pi / 6, 0.0])
reward = function.push_button(push_params)
print(reward)

function.shutdown()  # Apagado
