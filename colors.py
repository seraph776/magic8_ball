# !/usr/bin/env python
"""project: Magic 8 Ball Game, created:7/29/2021, author:seraph★776, email:seraph776@gmail.com"""


class Colors:
    """This is a class that handles the color response of the Magic 8 Ball."""

    @staticmethod
    def red(self):
        """red color font"""
        return f"\033[31m{self}\033[0m"

    @staticmethod
    def green(self):
        """green color font"""
        return f"\033[32m{self}\033[0m"

    @staticmethod
    def yellow(self):
        """yellow color font"""
        return f"\033[33m{self}\033[0m"


magick8BallColors = Colors()


