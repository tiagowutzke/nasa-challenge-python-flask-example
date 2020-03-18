import psycopg2


class Connection:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.conn, self.cursor = self._get_conn()

    @staticmethod
    def _get_conn():
        conn = psycopg2.connect(
            host='localhost',
            database='reuse_db',
            user='local',
            password='1234'
        )
        return conn, conn.cursor()

    def commit_transaction(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def rollback(self):
        self.commit_transaction('ROLLBACK')

    def close(self):
        self.conn.close()
