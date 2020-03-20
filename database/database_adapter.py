from database.connection import Connection
from database.persistence import Persistence
from database.query import Query


class DatabaseAdapter:
    def __init__(
            self,
            *args,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.conn = Connection()
        self.query = Query(self.conn)
        self.persistence = Persistence(self.conn)

    def select_all(self, table, *columns):
        return self.query.select_all(table, columns)

    def close(self):
        return self.conn.close()