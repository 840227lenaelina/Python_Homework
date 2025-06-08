from sqlalchemy import text
from DbConnection import get_db_connection


class DataBase:
    scripts = {
        "select": text("SELECT * FROM subject"),
        "select_only_id": text(
            "SELECT * FROM subject where subject_id = :subject_id"),
        "create": text(
            "INSERT INTO subject (\"subject_title\", \"subject_id\") "
            "VALUES (:new_subject_title, :new_id)RETURNING subject_id"),
        "delete": text("DELETE FROM subject  where subject_id = :subject_id"),
        "update": text(
            "UPDATE subject SET subject_title = :title "
            "where subject_id = :subject_id")
    }

    def select_subject(self):
        with get_db_connection() as session:
            result = session.execute(self.scripts["select"])
            return result.mappings().all()

    def select_subject_only_id(self, subject_id1):
        with get_db_connection() as session:
            select = self.scripts["select_only_id"]
            result = session.execute(select, {"subject_id": subject_id1})
            return result.mappings().all()

    def create_subject(self, subject_title, subject_id):
        with get_db_connection() as session:
            transaction = session.begin()
            subject = self.scripts["create"]
            result = session.execute(subject, {
                "new_subject_title": subject_title, "new_id": subject_id})
            transaction.commit()
            return result.mappings().one()

    def delete_subject(self, subject_id):
        with get_db_connection() as session:
            transaction = session.begin()
            session.execute(self.scripts["delete"], {
                "subject_id": subject_id})
            transaction.commit()

    def update_subject(self, subject_title, subject_id):
        with get_db_connection() as session:
            transaction = session.begin()
            update = self.scripts["update"]
            session.execute(update, {
                "title": subject_title,
                "subject_id": subject_id
            })
            transaction.commit()
            return True
