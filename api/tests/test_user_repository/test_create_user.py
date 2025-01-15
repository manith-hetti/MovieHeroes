from lib.user_repository import UserRepository
from lib.database_connection import get_db
from lib.user import User


def test_create_new_user_is_added_to_db():
    db = get_db()
    userRepository = UserRepository(db)

    user = User('John Doe', "john1@mail.com", "Password123!")
    created_user = userRepository.create(user, table_name='users')
    print(f"user: {user.full_name} created")
    user_in_table = userRepository.db['test_users_table'].find_one({'_id': created_user.id})
    assert user_in_table['full_name'] == 'John Doe'
    assert user_in_table['email'] == 'john1@mail.com'
    assert user_in_table['password'] is not None


