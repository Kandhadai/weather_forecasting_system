def test_get_user_by_username_failure(mocker):
    # Mock the UserDAO method to return None when user is not found
    mocker.patch('HU.Project.Website.dao.user_dao.UserDAO.get_user_by_username', return_value=None)

    with pytest.raises(ValueError, match="User with username 'non_existent_user' not found."):
        User.get_user_by_username("non_existent_user")


def test_get_user_by_id_failure(mocker):
    # Mock the UserDAO method to return None when user is not found
    mocker.patch('HU.Project.Website.dao.user_dao.UserDAO.get_user_by_id', return_value=None)

    with pytest.raises(ValueError, match="User with ID '999' not found."):
        User.get_user_by_id(999)
