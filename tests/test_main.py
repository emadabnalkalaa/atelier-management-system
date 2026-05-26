import sys
import os
import builtins

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import Customer, Order, create_order, main


# ✅ Customer Test
def test_create_customer():
    c = Customer("emad")
    assert c.name == "emad"


# ✅ Order Creation Test
def test_create_order():
    c = Customer("Ali")
    o = Order(c, "wood", "brown", 100)

    assert o.customer.name == "Ali"
    assert o.material == "wood"
    assert o.color == "brown"
    assert o.price == 100


# ✅ Show Order Output
def test_show_order(capsys):
    c = Customer("Ali")
    o = Order(c, "wood", "brown", 100)

    o.show_order()
    captured = capsys.readouterr()

    output = captured.out.lower()

    assert "ali" in output
    assert "wood" in output
    assert "brown" in output
    assert "100" in output


# ✅ Test input flow
def test_create_order_input(monkeypatch):
    inputs = iter(["Ali", "wood", "brown", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    create_order()


# ✅ Integration Test (Flow)
def test_create_order_flow(monkeypatch):
    inputs = iter(["Ali", "wood", "brown", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    create_order()


# ✅ Main Exit Test
def test_main_exit(monkeypatch):
    inputs = iter(["2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()