def insert_orders(persistance, session_id, request, table, table_rows, error_msg, success_msg):
    returns = []
    session = f"'{session_id}'"
    for x in range(1, table_rows + 1):
        id = request.form[f'id{x}']
        order = request.form[f'order{x}']
        insert_return = persistance.insert_orders(table, item_id=id, orders=order, session=session)

        returns.append(insert_return)

    if False in returns:
        return error_msg

    return success_msg


def api_insert_orders(persistance, session_id, request, table):
    session_id = f"'{session_id}'"
    for id, order in request.items():
        insert_return = persistance.insert_orders(table, item_id=id, orders=order, session=session_id)
        if not insert_return:
            return f"{{\n\tcode: 400,\n\tmessage: Error on insert id: {id} / order {order}\n}}"

    return "{\n\tcode: 200\n\tmessage: Success\n}"


def calculate_score(query, session_id):
    game = query.select_game_by_session(session_id)

    delta_individual = 0
    delta_team = 0

    for single, team, answer in game:
        delta_individual += abs(answer - single)
        delta_team += abs(answer - team)

    return ( delta_individual - delta_team * 100 ) / 112


