# coding: utf-8

import unittest
from datetime import datetime
import time

import easytrader
from easytrader import gj_clienttrader as gj


if __name__ == '__main__':
    u1 = gj.GJClientTrader()
    u1.prepare()
    u1.buy('002422', 15, 1000)
    u1.sell('002422', 17, 1000)
