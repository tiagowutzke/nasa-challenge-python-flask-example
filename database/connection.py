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
            host='ec2-52-200-119-0.compute-1.amazonaws.com',
            database='d2vb1674stun3q',
            user='nprdjtrodglaic',                                          
            password='4d670d30987de1f8704bdd8ec2470396638f25f27ebce0840f2a762fd2c40c5c'
'
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
