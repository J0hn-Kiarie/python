import pytest
from television import *

@pytest.fixture
def tv():
    return Television()

def test_power_on(tv):
    tv.power()
    assert "Power = True" in str(tv)

def test_power_off(tv):
    tv.power()
    tv.power()
    assert "Power = False" in str(tv)

def test_channel_up_once(tv):
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_to_zero(tv):
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  
    assert "Channel = 0" in str(tv)

def test_channel_down_to_max(tv):
    tv.power()
    tv.channel_down() 
    assert "Channel = 3" in str(tv)

def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

def test_volume_up_to_max(tv):
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down_to_min(tv):
    tv.power()
    tv.volume_down()
    assert "Volume = 0" in str(tv)
