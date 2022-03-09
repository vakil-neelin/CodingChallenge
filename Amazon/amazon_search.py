import unittest
from amazon_store_handler import *

expected_results = [['Disney Channel Amphibia T-Shirt', '$22.99'], ['Disney Mickey And Friends Daisy & Minnie Fashion T-Shirt', '$22.99'], ['Disney Princess Dress Up Trunk Deluxe 21 Piece [Amazon Exclusive]', '$34.99'], ['Disney Mickey And Friends Minnie Mouse Leopard Bow Portrait T-Shirt', '$22.99'], ['Disney Princess Ultimate Celebration Castle, 4 Feet Tall Doll House with Furniture and Accessories, Musical Fireworks Light Show, Toy for Girls 3 and Up', '$119.00'], ['Disney Princess Belle Ariel Cinderella Jasmine 4 Pack Graphic T-Shirts', '$29.99'], ["Disney Little Girls' Minnie Seven-Pack of Brief Underwear", '$10.94'], ['LEGO Disney Rapunzel’s Tower 43187 Building Kit for Kids; A Great Birthday for Disney Princess Fans; Ideal for Kids who Like Rapunzel, Flynn Rider and Pascal (369 Pieces)', '$59.99'], ['Disney Mickey Mouse Classic Small Pose T-Shirt', '$22.99'], ["Disney Boys' Toddler Mickey Mouse Luxe Plush Robe", '$22.99'], ['Disney+', '$0.00'], ['Disney Mickey And Friends Minnie Mouse Traditional Portrait T-Shirt', '$22.99'], ['LEGO Disney Cinderella’s Royal Carriage 43192; Creative Building Kit That Makes a Great Gift, New 2021 (237 Pieces)', '$39.99'], ['Simple Modern 14oz Disney Summit Kids Water Bottle Thermos with Straw Lid - Dishwasher Safe Vacuum Insulated Double Wall Tumbler Travel Cup 18/8 Stainless Steel - Disney: Mickey Ears', '$18.85'], ['Toddler Girls Princess Night Dress Flutter Sleeve Baby Girls Cute Summer Dress Daily Home Wearing', '$15.99'], ['Disney Princess Birthday Party Banner,Birthday Party decoration for Girl', '$9.66'], ['Disney Princess Underwear Mulipacks', '$18.00'], ['Disney Mickey And Friends Mickey Retro Beach T-Shirt', '$22.99'], ['Minnie Mouse, Never Grow Up T-Shirt, Funny Cute Matching Disney Shirts for Ladies, Girls Summer Tanks', '$20.99'], ['Yoto Player & 2 Disney Audio Cards - Join Mickey & Friends in 5 Minute Mickey Mouse Stories - 5 Minute Disney Sleepy Time Bedtime Stories - Children’s Storytelling Speaker Plays Audiobook Cards & More', '$109.99'], ['Mickey Mouse Toddler Boys Hooded Robe, Bathrobe/Terry', '$32.00'], ['Disney Princess Sterling Silver Cubic Zirconia Jeweled Tiara Necklace, Official License', '$59.99']]


class MyTestCase(unittest.TestCase):
    amazon_store_handler = None

    @classmethod
    def setUpClass(cls):
        cls.amazon_store_handler = AmazonStoreHandler(headless=False)
        return

    def test_amazon_search(self):
        print("Step 1: Search Amazon Store...")
        self.amazon_store_handler.search_store("Disney")
        print("success")

        print("Step 2: Process Search Results...")
        results = self.amazon_store_handler.get_search_results()
        print(results)
        print(expected_results == results)
        print(len(expected_results))
        print(len(results))
        for result in results:
            print("Disney" in result[0])
            if "Disney" not in result[0]:
                print(result)
        print("success")
        return

    @classmethod
    def tearDownClass(cls):
        return


if __name__ == '__main__':
    unittest.main()
