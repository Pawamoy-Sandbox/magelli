#!/usr/bin/python
# -*- coding: utf-8 -*-

class Key :
	def __init__(self, val) :
		self.val = val
		self.it  = 1

	def __repr__(self) :
		return str(self.val)

	def add(self, val) :
		self.it += 1
		if self.it > 1 :
			self.val = ((self.it-1.)*self.val + val)/self.it
		else :
			self.val = val

class Config :
	def __init__(self, name) :
		self.name = name
		self.dict = {}

	def __repr__(self) :
		return str(self.name) + ' : \n\t' + str(self.dict) + '\n'

	def add(self, key, val) :
		if key in self.dict.keys() :
			self.dict[key].add(val)
		else :
			self.dict[key] = Key(val)
			
	def intersection(self, config2) :
		return list(set(self.dict.keys()) & set(config2.dict.keys()))