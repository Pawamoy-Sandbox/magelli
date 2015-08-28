#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class Timer :
	def __init__(self) :
		self.t = 0

	def start(self) :
		self.t = time.time()

	def time(self) :
		return time.time() - self.t