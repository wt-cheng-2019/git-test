from lib.foo import Foo


def test_foo_is_true():
    assert Foo.foo() is True


def test_bar_is_false():
    assert Foo.bar() is False
