import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        """Setup a new Television before each test."""
        self.tv1 = Television()
    
    def teardown_method(self):
        """Teardown the Television after each test."""
        del self.tv1

    def test_init(self):
        """Test initial TV values."""
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

    def test_power_on_off(self):
        """Test toggling TV power."""
        self.tv1.power()
        assert str(self.tv1).startswith("Power = True")
        self.tv1.power()
        assert str(self.tv1).startswith("Power = False")

    def test_mute_behavior(self):
        """Test muting and unmuting the TV."""
        self.tv1.power()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"

        self.tv1.mute()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.power()
        self.tv1.mute()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up_behavior(self):
        """Test increasing channel and wrapping around."""
        self.tv1.channel_up()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.channel_up()
        assert str(self.tv1) == "Power = True, Channel = 1, Volume = 0"

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()  
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down_behavior(self):
        """Test decreasing channel and wrapping around."""
        self.tv1.channel_down()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.channel_down()
        assert str(self.tv1) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up_behavior(self):
        """Test increasing volume and respecting max limit."""
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down_behavior(self):
        """Test decreasing volume and respecting min limit."""
        self.tv1.volume_down()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 2"

        self.tv1.volume_down()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_down()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"