from flask import Blueprint
from Control.operadora_controller import buscar_operadoras

routes = Blueprint('routes', __name__)
routes.route('/buscar', methods=['GET'])(buscar_operadoras)
