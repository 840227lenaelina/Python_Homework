import requests


base_url = "https://ru.yougile.com/api-v2/"
my_key = 'key'  # подставить Ваш ключ
id_users = 'id'  # подставить id users из вашего проекта


def test_create_project_positive():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    list_projects = requests.get(base_url + 'projects', headers=headers)
    len_before = list_projects.json().get("content", [])

    name_project = {
        "title": "Test_users123",
        "users": {
            f"{id_users}": "worker"
        }
    }
    resp = requests.post(base_url + 'projects',
                         headers=headers, json=name_project)

    list_projects = requests.get(base_url + 'projects', headers=headers)
    len_after = list_projects.json().get("content", [])
    assert resp.status_code == 201
    assert len(len_after) - len(len_before) == 1


def test_create_project_negative():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    list_projects = requests.get(base_url + 'projects', headers=headers)
    len_before = list_projects.json().get("content", [])

    name_project = {
        "title": '',
        "users": {
            f"{id_users}": "worker"
        }
    }
    resp = requests.post(base_url + 'projects',
                         headers=headers, json=name_project)

    list_projects = requests.get(base_url + 'projects', headers=headers)
    len_after = list_projects.json().get("content", [])
    assert resp.status_code == 400
    assert len(len_after) - len(len_before) == 0


def test_update_project_positive():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    name_project = {
        "title": "Test_project",
        "users": {
            f"{id_users}": "worker"
        }
    }
    resp = requests.post(base_url + 'projects',
                         headers=headers, json=name_project)
    project_id = resp.json()["id"]
    id_project = project_id

    new_name = {
        "deleted": True,
        "title": "New_test_company",
        "users": {
            f"{id_users}": "worker"
        },
    }
    resp = requests.put(f"{base_url}projects/{id_project}",
                        headers=headers, json=new_name)
    assert resp.status_code == 200

    updated_project_resp = requests.get(
        f"{base_url}projects/{id_project}",
        headers=headers)
    updated_project = updated_project_resp.json()
    assert updated_project["title"] == "New_test_company"


def test_update_project_negative():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    new_name = {
        "deleted": True,
        "title": "New_test_company_name2",
        "users": {
            f"{id_users}": "worker"
        },
    }
    resp = requests.put(base_url + 'projects/123',
                        headers=headers, json=new_name)
    assert resp.status_code == 404


def test_get_project_id_positive():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    list_projects = requests.get(base_url + 'projects', headers=headers)
    project_list = list_projects.json().get("content", [])
    project_id = project_list[-1]["id"]
    id_project = project_id

    resp = requests.get(f"{base_url}projects/{id_project}", headers=headers)
    assert resp.status_code == 200
    return ("Информация о проекте:", resp.json())


def test_get_project_id_negative():
    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json"
    }
    resp = requests.get(f"{base_url}projects/123", headers=headers)
    assert resp.status_code == 404
