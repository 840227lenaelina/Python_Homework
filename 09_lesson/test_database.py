from DataBase import DataBase

db = DataBase()


def test_select_subject():
    db_list = db.select_subject()
    row = db_list[0]
    assert row["subject_id"] == 1
    assert row["subject_title"] == 'English'


def test_create_subject():
    body = db.select_subject()
    len_before = len(body)

    new_subject_title = "Technology"
    new_id = 16
    result = db.create_subject(new_subject_title, new_id)
    new_subject_id = result['subject_id']

    body = db.select_subject()
    len_after = len(body)

    db.delete_subject(new_subject_id)
    assert len_after - len_before == 1


def test_update_subject():
    new_subject_title = "Technology"
    new_id = 16
    result = db.create_subject(new_subject_title, new_id)
    new_subject_id = result['subject_id']

    title = "New_History"
    subject_id = new_subject_id
    result_update = db.update_subject(title, subject_id)

    subject_id1 = new_subject_id
    select = db.select_subject_only_id(subject_id1)

    db.delete_subject(new_subject_id)
    assert result_update is True
    assert len(select) > 0
    assert select[0]['subject_title'] == title


def test_delete_subject():
    new_subject_title = "Technology"
    new_id = 17
    result = db.create_subject(new_subject_title, new_id)
    new_subject_id = result['subject_id']

    db.delete_subject(new_subject_id)

    select = db.select_subject_only_id(new_subject_id)
    assert len(select) == 0
