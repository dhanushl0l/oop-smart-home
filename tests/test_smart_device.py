import pytest
from devices.base import Device 
from devices.fan import Fan
from devices.light import Light
from controller import Controller

def test_encapsulation_breach():
    fan = Fan()
    with pytest.raises(AttributeError):
        _ = fan.__is_on
    
    with pytest.raises(AttributeError):
        fan.is_on = True

    assert fan.is_on is False 

def test_state_consistency():
    fan = Fan()
    assert fan.start() == "Fan has started"
    assert fan.is_on is True
    
    assert fan.start() == "Fan is already on."
    assert fan.is_on is True

def test_polymorphism(capsys):
    light = Light()
    controller = Controller(light) 
    
    controller.power_on()
    captured = capsys.readouterr()
    assert "Light switched on" in captured.out
    assert light.is_on is True

    controller.power_off()
    captured = capsys.readouterr()
    assert "Light switched off" in captured.out
    assert light.is_on is False

def test_extensibility(capsys):
    class Radio(Device):
        name = "Radio"
        msg_start = "Radio playing music"
        msg_stop = "Radio silenced"
    
    radio = Radio()
    controller = Controller(radio)
    
    controller.power_on()
    captured = capsys.readouterr()
    assert "Radio playing music" in captured.out
    assert radio.is_on is True
    
    controller.power_off()
    captured = capsys.readouterr()
    assert "Radio silenced" in captured.out
    assert radio.is_on is False