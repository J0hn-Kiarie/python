class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default settings.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Toggle the power status of the TV (on/off).
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status if the TV is on.
        """
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        """
        Increase the channel number by 1 if the TV is on.
        Wraps to MIN_CHANNEL if channel exceeds MAX_CHANNEL.
        """
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel number by 1 if the TV is on.
        Wraps to MAX_CHANNEL if channel goes below MIN_CHANNEL.
        """
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by 1 if the TV is on.
        Does not exceed MAX_VOLUME.
        """
        if self.__status == True:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 if the TV is on.
        Does not go below MIN_VOLUME.
        """
        if self.__status == True:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Return a string representation of the TV's status, channel, and volume.
        If muted, volume is shown as 0.
        :return: A formatted string showing the TV status.
        """
        volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
        
        
