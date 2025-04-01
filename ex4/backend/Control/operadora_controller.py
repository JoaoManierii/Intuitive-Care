from flask import jsonify, request
from Model.operadora_model import OperadoraModel

operadora_model = OperadoraModel()

def buscar_operadoras():
    termo = request.args.get('q', '')
    if not termo:
        return jsonify({"erro": "Parâmetro 'q' é obrigatório."}), 400
    
    resultados = operadora_model.buscar_por_texto(termo)
    return jsonify(resultados)
