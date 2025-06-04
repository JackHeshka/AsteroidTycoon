"""Here is where the player will be able to trade resources to get more money"""
import player as Pl
import station as St

class tradeHub:
    def __init__(self, station: St.station):
        self.station = station

    def trade_resources(self, player: Pl.player, resource: str, amount: int):
        """This function will allow the player to trade resources for credits."""
