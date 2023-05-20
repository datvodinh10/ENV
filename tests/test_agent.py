# import pytest
# @pytest.fixture(scope="session")
# def name(pytestconfig):
#     return pytestconfig.getoption("name")

import os

# from git import Repo
import subprocess
from tests.CheckEnv import check_pytest


def get_changed_files():
    # Đường dẫn tới thư mục git
    # repo_path = ""

    # Khởi tạo đối tượng Repo từ đường dẫn thư mục git
    # repo = Repo(repo_path)

    # Lấy commit gần nhất
    # latest_commit = repo.head.commit
    # print(latest_commit, type(latest_commit))
    # print(repo.commit("HEAD~1"), type(repo.commit("HEAD~1")))

    # changed_files = []
    # for diff in repo.commit("HEAD~1").diff():
    #     changed_files.append(diff.a_path)

    # Liệt kê các tệp tin đã thay đổi trong commit gần nhất
    # changed_files = []
    # for diff in latest_commit.diff(None):
    #     changed_files.append(diff.a_path)
    command = f"git diff --name-only HEAD~1"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    changed_files = output.strip().split("\n")
    print(changed_files)
    return changed_files


def test_print_name():
    changed_files = get_changed_files()

    for file in changed_files:
        if "Base/" in file and "/_env.py" in file:
            env_name = file.replace("Base/", "").replace("/_env.py", "")
            print(env_name, "checking...")
            check_env, list_bug = check_pytest(env_name)
            if check_env == False:
                print("ENV:", env_name, "FALSE:", list_bug)
                assert False
            else:
                print("ENV:", env_name, "TRUE")
                assert True
