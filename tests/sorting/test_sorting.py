from src.pre_built.sorting import sort_by

mocked_jobs = [
    {
        "date_posted": "05-11-2022",
        "max_salary": 1600,
        "min_salary": 1200,
    },
    {
        "date_posted": "10-03-2022",
        "max_salary": 5000,
        "min_salary": 2500,
    },
    {
        "date_posted": "18-04-2022",
        "max_salary": 3000,
        "min_salary": 2000,
    },
    {
        "date_posted": "11-01-2023",
        "max_salary": 4200,
        "min_salary": 3600,
    },
]


def test_sort_by_criteria():
    sort_by(mocked_jobs, "min_salary")
    assert mocked_jobs[0]["min_salary"] == 1200
    assert mocked_jobs[1]["min_salary"] == 2000

    sort_by(mocked_jobs, "max_salary")
    assert mocked_jobs[0]["max_salary"] == 5000
    assert mocked_jobs[1]["max_salary"] == 4200

    sort_by(mocked_jobs, "date_posted")
    assert mocked_jobs[0]["date_posted"] == "10-03-2022"
    assert mocked_jobs[1]["date_posted"] == "11-01-2023"
