import uuid

from flask import Flask, render_template, request

from reuse.process import insert_orders, calculate_score, api_insert_orders

from reuse.database.query import Query
from reuse.database.connection import Connection
from reuse.database.persistence import Persistence


app = Flask(__name__)

# Database connection for all transactions
conn = Connection()

# Object for query database
query = Query(conn)

# Object for transaction in database
persistance = Persistence(conn)

# routes
index_route = "/"
single_route = "/single"
team_route = "/team"
post_single_route = "/post-single"
post_team_route = "/post-team"
score_route = "/score"

# api routes
api_get_session_id = "/api/get-session"
api_post_single = "/api/post-single"
api_post_team = "/api/post-team"
api_score_route = "/api/score"

session_id = str(uuid.uuid4())


@app.route(index_route)
def index():
    items = query.select_all('items', 'id', 'description')
    return render_template('index.html', title='Desafio da Nasa', items=items, route=single_route)


@app.route(single_route)
def single():
    items = query.select_all('items', 'id', 'description')
    return render_template('items.html', title='Teste individual', items=items, route=post_single_route)


@app.route(team_route)
def team():
    items = query.select_all('items', 'id', 'description')
    return render_template('items.html', title='Teste da equipe', items=items, route=post_team_route)


@app.route(post_single_route, methods=['POST'])
def post_single():
    table_rows = len(request.form) // 2

    error_msg = {
        'title': 'Erro ao salvar!',
        'message': 'Por favor, tente novamente',
        'html_class': 'error',
        'message_button': 'TENTE NOVAMENTE',
        'route': single_route
    }
    success_msg = {
        'title': 'Sucesso!',
        'message': 'Ordem dos itens individuais salvo com sucesso!',
        'html_class': 'success',
        'message_button': 'CONTINUE PARA TESTE DE EQUIPE',
        'route': team_route
    }

    msg_template = insert_orders(
        request=request,
        session_id=session_id,
        persistance=persistance,
        table='single_orders',
        table_rows=table_rows,
        error_msg=error_msg,
        success_msg=success_msg
    )

    return render_template('message.html',
                           title=msg_template['title'],
                           message=msg_template['message'],
                           alert_class=msg_template['html_class'],
                           message_button=msg_template['message_button'],
                           route=msg_template['route']
                           )


@app.route(post_team_route, methods=['POST'])
def post_team():
    table_rows = len(request.form) // 2

    error_msg = {
        'title': 'Erro ao salvar!',
        'message': 'Por favor, tente novamente',
        'html_class': 'error',
        'message_button': 'TENTE NOVAMENTE',
        'route': team_route
    }
    success_msg = {
        'title': 'Sucesso!',
        'message': 'Ordem dos itens de equipe salvo com sucesso!',
        'html_class': 'success',
        'message_button': 'VEJA SUA PONTUAÇÃO',
        'route': score_route
    }

    msg_template = insert_orders(
        request=request,
        session_id=session_id,
        persistance=persistance,
        table='team_orders',
        table_rows=table_rows,
        error_msg=error_msg,
        success_msg=success_msg
    )

    return render_template('message.html',
                           title=msg_template['title'],
                           message=msg_template['message'],
                           alert_class=msg_template['html_class'],
                           message_button=msg_template['message_button'],
                           route=msg_template['route']
                           )


@app.route(score_route)
def score():
    score = calculate_score(query, session_id)

    template = {
        'title': 'Sua pontuação é...',
        'message': score,
        'html_class': 'success',
        'message_button': 'INICIO',
        'route': '/',
        'style': 'block'
    }

    return render_template('message.html',
                           title=template['title'],
                           message=template['message'],
                           alert_class=template['html_class'],
                           message_button=template['message_button'],
                           route=template['route'],
                           style=template['style']
                           )


@app.route(api_get_session_id)
def api_get_session_id():
    return str(uuid.uuid4())


@app.route(api_post_single, methods=['POST'])
def api_post_single(table='single_orders'):
    if request.method == 'POST':
        try:
            data = request.get_json()

            response = api_insert_orders(
                persistance,
                session_id=data['session'],
                request=data['orders'],
                table=table
            )

            return response
        except Exception as e:
            return f"{{\n\tcode: 400\n\tmessage: error on request\n\tError details:\n\t{e}}}"


@app.route(api_post_team, methods=['POST'])
def api_post_team():
    return api_post_single('team_orders')


@app.route(api_score_route, methods=['GET'])
def api_score():
    try:
        if request.method == 'GET':
            data = request.get_json()

            score = calculate_score(query, data['session'])

            return f"{{\n\t'code': 200,\n\t'message': 'success',\n\t'response': {{\n\t\t'score': {score} \n\t}}\n}}"
    except Exception as e:
        return f"{{\n\t'code': 500,\n\t'message': 'error on request',\n\t'response': {{\n\t\t'message': {e} \n\t}}\n}}"


if __name__ == "__main__":
    app.run(debug=True)
    conn.close()

