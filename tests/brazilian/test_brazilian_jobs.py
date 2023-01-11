from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    excepted_keys = {"title", "salary", "type"}

    path = "tests/mocks/brazilians_jobs.csv"
    result = read_brazilian_file(path)

    keys = set()
    for job in result:
        for key in job.keys():
            keys.add(key)
    assert keys == excepted_keys
