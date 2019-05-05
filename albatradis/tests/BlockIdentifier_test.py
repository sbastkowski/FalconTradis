import unittest
import os
import logging
from albatradis.BlockIdentifier import BlockIdentifier

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','blockidentifier')

class TestBlockIdentifier(unittest.TestCase):

	def test_block_identifier_normal_case(self):
		b = BlockIdentifier(os.path.join(data_dir, 'normalcase'),os.path.join(data_dir, 'normalcase_forward'),os.path.join(data_dir, 'normalcase_reverse'), 1)
		blocks = b.block_generator()
	
		
		self.assertEqual(2, len(blocks))
		
		self.assertEqual([6, 14], [ x.start for x in blocks] )
		self.assertEqual([8, 19], [ x.end for x in blocks] )
		self.assertEqual([2, -3], [ x.max_logfc for x in blocks] )
		self.assertEqual([3, 6], [ x.block_length for x in blocks] )
		self.assertEqual(['forward', 'reverse'], [ x.direction for x in blocks] )
		self.assertEqual(['increased_insertions', 'decreased_insertions'], [ x.expression for x in blocks] )

	def test_noblocks(self):
		b = BlockIdentifier(os.path.join(data_dir, 'noblocks'),os.path.join(data_dir, 'noblocks_forward'),os.path.join(data_dir, 'noblocks_reverse'), 1)
		blocks = b.block_generator()
		self.assertEqual(0, len(blocks))
		
	def test_blocks_at_end(self):
		b = BlockIdentifier(os.path.join(data_dir, 'blocksatends'),os.path.join(data_dir, 'blocksatends_forward'),os.path.join(data_dir, 'blocksatends_reverse'), 1)
		blocks = b.block_generator()
		self.assertEqual(2, len(blocks))
		
		self.assertEqual([1, 16], [ x.start for x in blocks] )
		self.assertEqual([3, 21], [ x.end for x in blocks] )
		self.assertEqual([2, -3], [ x.max_logfc for x in blocks] )
		self.assertEqual([3, 6], [ x.block_length for x in blocks] )
		self.assertEqual(['forward', 'reverse'], [ x.direction for x in blocks] )
		self.assertEqual(['increased_insertions', 'decreased_insertions'], [ x.expression for x in blocks] )
		
	def test_peak_from_array(self):
		b = BlockIdentifier('','','', 1)
		self.assertEqual(15, b.peak_from_array([1,5,10,15,0,1]))
		self.assertEqual(-15, b.peak_from_array([-1,-5,-10,-15,0,-1]))
		self.assertEqual(-15, b.peak_from_array([1,-5,10,-15,0,1]))
		