from src.app import get_activities


def test_get_activities_filters_by_activity_name():
    result = get_activities(activity="Chess")

    assert list(result.keys()) == ["Chess Club"]


def test_get_activities_filters_by_category():
    result = get_activities(category="Sports")

    assert set(result.keys()) == {"Gym Class", "Soccer Team", "Basketball Team"}
