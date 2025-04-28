class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUM
        self.__channel: int = self.MIN_CHANNEL
    
    def power(self):
        """
        Function to change boolean __status between true and false
        """
        self.__status = not self.__status

    def mute(self):
        """
        Function to change boolean __muted between true and false when __status is True
        """
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self):
        """
        Function to increase a number when a value is True, sets number to minimum value when number hits maximum
        """
        if self.__status == True:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Function to decrease a number when a value is True, sets number to maximum value when number hits minimum
        """
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Function to increase a number when a value is True, keeps number at maximum value when number is greater than maximum
        """
        if self.__status == True:
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        """
        Function to decrease a number when a value is True, keeps number at minimum value when number goes lower than minimum
        """
        if self.__status == True:
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self):
        """
        Function to return a string value of the current __status, __channel, and __volume
        :return: string of Power, Channel, and Volume
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
        
