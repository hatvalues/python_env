'Test Main Module'
import main


def test_get_or_create_session():
    assert main.get_or_create_session() == "dummy session"
