#!/usr/bin/env python
import random


class Deck:
    """
    Simulates a deck of cards using lists.
    """
    def __init__(self):
        self.card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_suits = ["diamonds", "hearts", "clubs", "spades"]
        self.all_cards = [(value, suit) for value in self.card_values for suit in self.card_suits]

    def shuffle(self):
        """
        Randomly reorders :py:attr:`Deck.all_cards` attribute.
        """
        random.shuffle(self.all_cards)  # random shuffle

    def deal(self, ncards, destinations, location):
        """
        Takes cards from the top of deck, and deals to either the top of bottom of the deck/s listed in destinations

        :param ncards: number of cards to deal
        :type ncards: int
        :param destinations: list of :py:attr:`deck.Deck.all_cards` decks for the cards to be delt to.
        :type destinations: list
        :param location: Specifies to deal to the "Top" or "Bottom" of the destination decks
        :type location: str
        """
        for n in range(ncards):
            for pile in destinations:
                if location == "top":
                    pile.insert(0, self.all_cards.pop(0))
                elif location == "bottom":
                    pile.append(self.all_cards.pop(0))

    def upturn(self, ncards):
        """
        :param ncards: The number of cards to turn over.
        :type ncards: int
        """
        print(self.all_cards[0:ncards])

    def empty(self):
        """
        Clears all cards from :py:attr:`deck.all_cards`.
        """
        self.all_cards.clear()
