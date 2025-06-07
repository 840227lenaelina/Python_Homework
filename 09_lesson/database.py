from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:12345@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_create_subject():
    connection = db.connect()
    transaction = connection.begin()

    body = connection.execute(text("SELECT * FROM subject")).mappings().all()
    body_after = len(body)

    subject = text("INSERT INTO subject (\"subject_title\", \"subject_id\") "
                   "VALUES (:new_subject_title, :new_id)RETURNING subject_id")
    result = connection.execute(subject, {
        "new_subject_title": "Tecnol", "new_id": 16})
    new_id = result.fetchone()[0]

    body2 = connection.execute(text("SELECT * FROM subject")).mappings().all()
    body_begin = len(body2)

    delete_subject = text(
        "DELETE FROM subject  where subject_id = :subject_id")
    connection.execute(delete_subject, {"subject_id": new_id})
    transaction.commit()
    assert body_begin - body_after == 1
    connection.close()


def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()

    subject = text("INSERT INTO subject (\"subject_title\", \"subject_id\")"
                   "VALUES (:new_subject_title, :new_id)RETURNING subject_id")
    result = connection.execute(subject, {
        "new_subject_title": "Tecnol", "new_id": 16})
    new_id = result.fetchone()[0]

    update = text("UPDATE subject SET "
                  "subject_title = :title where subject_id = :subject_id")
    connection.execute(update, {"title": 'Technology', "subject_id": new_id})
    check_title = text(
        "SELECT subject_title FROM subject WHERE subject_id = :subject_id")
    update_title_result = connection.execute(check_title,
                                             {"subject_id": new_id}).fetchone()

    assert update_title_result[0] == 'Technology'

    delete_subject = text(
        "DELETE FROM subject  where subject_id = :subject_id")
    connection.execute(delete_subject, {"subject_id": new_id})

    transaction.commit()
    connection.close()


def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()

    subject = text("INSERT INTO subject (\"subject_title\", \"subject_id\") "
                   "VALUES (:new_subject_title, :new_id)RETURNING subject_id")
    result = connection.execute(subject, {
        "new_subject_title": "New_history", "new_id": 17})
    new_id = result.fetchone()[0]

    delete_subject = text(
        "DELETE FROM subject  where subject_id = :subject_id")
    connection.execute(delete_subject, {"subject_id": new_id})
    check_delete = text("SELECT * FROM subject WHERE subject_id = :subject_id")
    delete_sub = connection.execute(check_delete,
                                    {"subject_id": new_id}).fetchone()

    assert delete_sub is None

    transaction.commit()
    connection.close()
