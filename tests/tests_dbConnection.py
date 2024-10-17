from HU.Project.Website.entities.db_connection import DatabaseConnection


def test_get_connection():
    connection = DatabaseConnection.get_connection()
    assert connection is not None
