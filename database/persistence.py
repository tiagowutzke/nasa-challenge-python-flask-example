import logging

from database.query import Query

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Persistence:
    def __init__(
        self,
        conn=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.connection = conn

    def insert_orders(self, table, **cols_values):
        query = Query()

        columns, _ = query.get_cols_param(cols_values.keys())
        values, _ = query.get_cols_param(cols_values.values())

        try:
            sql = f"""
                INSERT INTO {table} ({columns})
                VALUES ({values})
            """
            self.connection.commit_transaction(sql)
            return True

        except Exception as e:
            message = f'Error on insert values:\n{e}'
            logging.info(message)
            return False
