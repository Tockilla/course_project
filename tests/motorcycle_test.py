from rental.transport.motorcycle import Motorcycle


def test_motorcycle_initialization():
    moto = Motorcycle(
        id="M001",
        brand="Yamaha",
        model="R1",
        year=2019,
        color="Red",
        engine_capacity=1.0,
        extra="Sport",
    )

    assert moto.id == "M001"
    assert moto.brand == "Yamaha"
    assert moto.model == "R1"
    assert moto.year == 2019
    assert moto.color == "Red"
    assert moto.engine_capacity == 1.0
    assert moto.extra == "Sport"


def test_motorcycle_show_info():
    moto = Motorcycle(
        id="M001",
        brand="Yamaha",
        model="R1",
        year=2019,
        color="Red",
        engine_capacity=1.0,
        extra="Sport",
    )

    info = moto.show_info()

    assert "[MOTORCYCLE] M001" in info
    assert "Yamaha" in info
    assert "R1" in info
    assert "2019" in info
    assert "Red" in info
    assert "1.0" in info
    assert "Sport" in info
