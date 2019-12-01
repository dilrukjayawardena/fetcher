import unittest
import requests
from lxml import html
from DataHandler import DataHandler

class TestDataHandler(unittest.TestCase):
    def test_getDataFields(self):
        self.maxDiff = None
        dtObj=DataHandler()
        url='https://ikman.lk/en/ad/mitsubishi-montero-2003-for-sale-gampaha-149'
        respItem =requests.get(url)
        pageItem=html.fromstring(html=respItem.text)
        strData='Montero V6 3500cc Engine Full Option Dual A /C Cruise Control Sun Roof Teak Panels Triptronic Gears Beige Leather Seats 7 Seater All 4 Brand New Tyres TV DVD Reverse Camera Totally Accident Free Vehicle In Showroom Condition'
        listdt=['//i.ikman-st.com/f6e41ee1-fe09-44c9-a916-c3f951fdc42a/136/102/cropped.jpg',
                '//i.ikman-st.com/618708cd-b871-42a6-a854-5a3f8a0b4d7e/136/102/cropped.jpg',
                '//i.ikman-st.com/aa1f6a27-ee66-4c0a-9f06-beea458c9d83/136/102/cropped.jpg',
                '//i.ikman-st.com/1540d68c-4f04-4a6c-8360-3cdf204d7575/136/102/cropped.jpg',
                '//i.ikman-st.com/27de2571-77e4-410a-bcf2-997628f20d37/136/102/cropped.jpg' ]
        self.assertListEqual(dtObj.getDataFields('imageList',pageItem),listdt )
        self.assertEqual(dtObj.getDataFields('title',pageItem),'Cars : Mitsubishi Montero 2003 | Gampaha | ikman.lk' )
        self.assertEqual(dtObj.getDataFields('date',pageItem),'11 Nov  8:29 am' )
        self.assertEqual(dtObj.getDataFields('shortDescription',pageItem),'Mitsubishi Montero 2003' )
        self.assertEqual(dtObj.getDataFields('category',pageItem), 'Cars')
        self.assertEqual(dtObj.getDataFields('price',pageItem), '4,900,000')
        self.assertListEqual(dtObj.getDataFields('contact',pageItem), ['0778885438'])
       
if __name__ == '__main__':
    unittest.main()