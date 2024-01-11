from sqlite3 import Connection
from entities.ResultQuestion import ResultQuestion
from database_utils import convert_to_model
from dataclasses import astuple

class ResultsService : 

    @staticmethod
    def create_results(conn: Connection, result: ResultQuestion):
        conn.execute(
            "INSERT INTO ResultQuestion VALUES(%s, %s, %s);",
            *astuple(result)
        )


    @staticmethod
    def get_results_sorted(conn: Connection):
        res = conn.execute("SELECT * FROM ResultQuestion ORDER BY id;")
        return convert_to_model(res, ResultQuestion)

    @staticmethod
    def delete_result(conn: Connection, id_result: str):
        conn.execute("DELETE FROM ResultQuestion WHERE id = %s", (id_result,))
        conn.commit()

    @staticmethod
    def delete_all_results(conn: Connection):
        conn.execute("DELETE FROM ResultQuestion;")
        conn.commit()
