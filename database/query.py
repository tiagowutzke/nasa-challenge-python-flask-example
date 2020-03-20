import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Query:
    def __init__(
        self,
        conn=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.connection = conn

    @staticmethod
    def get_cols_param(columns):
        # Casting list to words comma separated
        is_more_one_column = len(columns) > 1
        return ', '.join(columns) if is_more_one_column else columns[0], is_more_one_column

    def select_all(self, table, columns):
        """ Select all rows from chosen table and columns
        :param table: (str) table that query will made
        :param columns: (list) columns chosen to table query
        :return: list contaning query result
        """
        columns, is_more_one_column = self.get_cols_param(columns)

        try:
            sql = f"""
                SELECT
                    {columns}
                FROM   
                    {table}
            """

            self.connection.cursor.execute(sql)

            if is_more_one_column:
                return self.connection.cursor.fetchall()

            return [row[0] for row in self.connection.cursor]

        except Exception as e:
            logging.info(f'Error on query:\n{e}')
            return False

    def select_game_by_session(self, session):
        try:
            sql = f"""
                SELECT
                    single.orders AS single_orders,
                    team.orders AS team_orders,
                    answer
                FROM
                    items
                JOIN
                    team_orders team
                    ON items.id = team.item_id
                JOIN 
                    single_orders single
                    USING ("session", item_id)
                WHERE
                    single."session" = '{session}' 
            """

            self.connection.cursor.execute(sql)

            return self.connection.cursor.fetchall()

        except Exception as e:
            logging.info(f'Error on query:\n{e}')
            return False


