#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import hashlib

def u2b( x ):
	return [ \
	( x >> 7 ) & 1, \
	( x >> 6 ) & 1, \
	( x >> 5 ) & 1, \
	( x >> 4 ) & 1, \
	( x >> 3 ) & 1, \
	( x >> 2 ) & 1, \
	( x >> 1 ) & 1, \
	x & 1 ]

def b2u( x ):
	return \
	x[0] * 0b10000000 + \
	x[1] * 0b01000000 + \
	x[2] * 0b00100000 + \
	x[3] * 0b00010000 + \
	x[4] * 0b00001000 + \
	x[5] * 0b00000100 + \
	x[6] * 0b00000010 + \
	x[7] * 0b00000001

def uarray2barray( u ):
	b = [ u2b( uu ) for uu in u ]
	b = np.asarray(b)
	b = np.reshape( b, [len(u)*8] )
	return b.tolist()

def barray2uarray( b ):
	l = len(b)
	b = np.asarray( b )
	b = np.reshape( b, [l//8, 8] )
	b = b.tolist()
	return [ b2u(bb) for bb in b ]

class shabinary:
	def algorithms_available():
		return hashlib.algorithms_available
	
	def __init__( self, name, length = None ):
		self.name = name
		self.length = length
		
		if( not ( name in hashlib.algorithms_available ) ):
			raise ValueError( name + ' is not available.' )
	
	def hash( self, data ):
		if( self.length is None ):
			b = hashlib.new( self.name, data ).digest()
		else:
			b = hashlib.new( self.name, data ).digest(self.length)
		return np.asarray( bytearray(b), dtype=np.uint8 )

	def binary1d( self, b ):
		if( isinstance(b,np.ndarray) ):
			return np.asarray( uarray2barray( self.hash( np.asarray( barray2uarray( b.tolist() ) ) ), dtype=np.uint8 ) )
		return uarray2barray( self.hash( np.asarray( barray2uarray( b ), dtype=np.uint8 ) ) )
	
	def binary2d( self, b ):
		if( isinstance(b,np.ndarray) ):
			return np.asarray( [ self.binary1d( bb ) for bb in b.tolist() ], dtype=np.uint8)
		return [ self.hash_b1( bb ) for bb in b ]

def _logisticmap( x0, a=4-1E-12, init_itr=100 ):
	x = x0
	for i in range(init_itr):
		x = a*x*(1-x)
	while( True ):
		x = a*x*(1-x)
		yield x

def logisticmap( sRow, sCol, seed, a=4-1E-12, init_itr=100 ):
	lm = _logisticmap( seed/4294967295 * (1.0-2.0E-12 ) + 1.0E-12, a, init_itr )
	d = [ lm.__next__() for i in range(sRow*sCol) ]
	d = np.asarray( d, dtype=np.float )
	d = np.reshape( d, [sRow, sCol] )
	return d

def logisticmap_binary( sRow, sCol, seed, a=4-1E-12, init_itr=100 ):
	return np.uint8( logisticmap( sRow, sCol, seed, a, init_itr ) > 0.5 )

if( __name__ == '__main__'):
	print( hashbinary.algorithms_available() )

'''
if( __name__ == '__main__'):

	h = hash( 'sha256' )
	Y = np.asarray( [0,1,2,3,4], dtype=np.uint8 )
	X = h.hash( Y )
	
	print(X)
	print(Y)


	Y = logisticmap_b( 4, 256, 888 )
	X = h.hash_b2(Y)
	
	print(X)
	print(Y)
'''
