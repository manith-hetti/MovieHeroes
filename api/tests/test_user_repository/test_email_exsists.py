from lib.user_repository import UserRepository
from lib.database_connection import get_db

def test_create_new_user_is_added_to_db_already_exsits_returns_true():
    db = get_db()
    userRepository = UserRepository(db)
    result = userRepository.email_exists('jet@mail.com', table_name = 'test_users_table')
    assert result == False

def test_create_new_user_is_added_to_db_doesnt_exsist_return_false():
    db = get_db()
    userRepository = UserRepository(db)
    result = userRepository.email_exists('notjet@mail.com', table_name = 'test_users_table')
    assert result == False
