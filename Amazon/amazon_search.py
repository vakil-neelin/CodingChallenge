import unittest
from amazon_store_handler import *

# TODO Implement Better Way To Pull Possible Search Results
# Possibly python-amazon-paapi

# Possible Code For API
# import os
# from amazon.paapi import AmazonAPI
# # Allows variable pass in from pipeline if needed
# AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY"]
# AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
# AWS_ASSOCIATE_TAG = os.environ["AWS_ASSOCIATE_TAG"]
# amazon = AmazonAPI(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, 'US')
# expected_search_results = [product.title for product in amazon.search_products(item_count=expected_search_result_count, keywords="disney amphibia poster")]
possible_results = [
    'Watercolor She-Ra and the Princesses of Power Poster Prints - Set of 4 (8x10) Netflix Cartoon Reboot Wall Art Decor - Adora - Glimmer - Bow - Catra',
    'HUANGWW Amphibia Season 2 Finale Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x18inch(30x45cm)',
    'Your Butt Napkins My Lord - Dragon Decorations - Gothic Bathroom Decor - Medieval Decor - Funny Bathroom Wall Art - Toilet Paper Wall Art - Restroom Sign - Bath Wall Decor - Powder Room Decor',
    '"If I Quit Now-I\'ll Be Back to Where I Started"-Motivational Exercise Wall Decor -8 x 10" Fitness Wall Art Print- Ready to Frame. Inspirational Home-Office-Gym-Studio Decor. Great Gift of Motivation!',
    'Shvieiart 8 X 12 Metal Signs - Wanted Owl Lady (The owl House) Vintage Look Metal Tin Poster',
    '7 Rules Of Life, motivational poster print',
    'Prints Pirates of the Caribbean Disneyland Poster (11x17) Vintage New Orleans Square Disney Ride Reproduction Wall Art Print',
    'Disney Quotes Wall Art Decor for Boys, Girls, Toddlers, Kids Bedroom, Family or Living Room, Kitchen, Bathroom - Decorations or Inspirational Gift for Walt Disney World, Disneyland, Mickey Mouse Fans',
    'Disneyland Star Tours Poster (11x14) Vintage Attraction Reproduction Wall Art Print',
    'Prints Santa Fe Railroad Disneyland RR Poster (11x17) Vintage Grand Canyon Diorama Disney Ride Reproduction Wall Art Print',
    '7 Rules of Life Motivational Poster - Printed on Premium Cardstock Paper - Sized 11 x 14 Inch - Perfect Print For Bedroom or Home Office',
    'United States Historical Poster 2021 Featuring: States, Presidents, Flags, Military. Excellent Gift for Retired Veterans, Scouts Eagle Ceremony, homeschooling, grandparents, funeral display. informative, captivating, and intriguing.',
    'Your Butt Napkins My Lord - Gothic Bathroom Decor - Funny Bathroom Wall Art - Toilet Paper Wall Art - Restroom Sign - Bath Wall Decor - Skeleton Decoration - Funny Wall Decor - Powder Room Decor Print',
    'Disney Thunder Mountain Poster Vintage Disney Attraction Posters Magic Kingdom Frontierland Disneyland Disney World Home Decor Wall Art',
    'Wee Blue Coo Political Drug Abuse Marijuana Weed Weird Unframed Wall Art Print Poster Home Decor Premium',
    'The Simpsons Poster - Custom Family Portrait Wall Art Posters Decor Merchandise Gifts, Digital Cartoon Illustration Caricature Drawing From Photos, Get Simpsonized - iToonify',
    'Disney Quotes Wall Decor - Hakuna Matata - Inspirational Gifts for Women, Men, Kids, Walt Disney World, Disneyland, Mickey Mouse Fans - Motivational Wall Art - Disney Decorations',
    'akeke Skull Decor Vintage Dictionary Art Print Two Set - Skull Decorations Gentleman Lady Hat - Bone Art Wall Decor 8x10 inch Unframed Skull Couples Gifts for Women Men',
    'Amphibia Full Character Cartoon Classic Poster Canvas Art Poster and Wall Art Picture Print Modern Family bedroom Decor Posters，Canvas Wall Art Living Room Posters Bedroom Painting08x12inch(20x30cm)',
    'Vintage Amusement Park Rides Patent Prints, 6 (8x10) Unframed Photos, Wall Art Decor Gifts Under 25 for Home Office Garage Shop Man Cave College Student Teacher Coach Disney Theme Movies Fan Club',
    'Eras of Life Poster 24x36 Illustrated Geological Chart NEW EDITION! Art Poster Print, 24x36',
    'Walt Disney Quotes Wall Art- “Keep Moving Forward To Success!”- 8 x 10" Modern Mickey Art Print- Ready to Frame. Home-Office-Classroom Décor. Perfect Gift for Motivation & Inspiration for Graduates.',
    'Disney Rides Patent Art Prints - Vintage Wall Art Poster Set - Chic Rustic Home Decor for Boys, Girls, Teens, Kids Room - Gift for Mickey Mouse, Disney World, Disneyland Fans, 8x10 Photos Unframed',
    'Amphibia Anne Boonchuy Animated Character Poster Canvas Art Poster and Wall Art Picture Print Modern Family bedroom Decor Posters，Canvas Wall Art Living Room Posters Bedroom Painting08x12inch(20x30cm)',
    'Tower of Terror Poster The Hollywood Tower Hotel Vintage Disney Attraction Posters Disneyland Disney World Hollywood Studios Home Decor Wall Art',
    'Mickey Mouse Ears Wall Art, Home Decor - Walt Disney Poster, Print - Unique Cinderella Castle Room Decorations and Great Gift for Disney World, Disneyland Fans - 8x10 Photo Unframed',
    'Prints Tower of Terror Disneyland Poster (11x17) Vintage The Twilight Zone Disney Ride Reproduction Wall Art Print',
    'Mickey Mouse Wall Art Watercolor Poster Prints - Set of 6 (8 inches x 10 inches) Photos - with Mickey Minnie Donald Duck Goofy Pluto',
    'JUYT Amphibia Animated Classic Character Poster Canvas Art Poster and Wall Art Picture Print Modern Family Bedroom Decor Posters，Canvas Wall Art Living Room Posters Bedroom Painting08x12inch(20x30cm)',
    'EzPosterPrints - Bodybuilding Men Girl Fitness Workout Quotes Motivational Inspirational Muscle Gym Posters - Wall Art Print for Home Office Gym - MOTIVATION-QUOTE-18-18X12 inches',
    'The Owl House Cartoon Classic Character Poster Canvas Art Poster and Wall Art Picture Print Modern Family bedroom Decor Posters，Canvas Wall Art Living Room Posters Bedroom Painting08x12inch(20x30cm)',
    'Bride of Chucky Jennifer Tilly Poster Decorative Painting Canvas Wall Art Living Room Posters Bedroom Painting 16"×24"（40*60cm）',
    '20 Pack Motivational Posters for Classroom Decor, Positivity Quotes Wall Signs for Office, School, Teachers Supplies, Chalkboard Design (13 x 19 inches)',
    'Hitecera Animen Poster Gravity Falls Art Poster Canvas Art Poster and Wall Art Picture Print Modern Family Bedroom Decor 12x18inch(30x45cm)',
    'Peoplemover Poster Vintage Disney Attraction Posters Magic Kingdom Tomorrowland Disneyland Classic Disney World Home Decor Wall Art',
    'Hong Art- Lighted Canvas Prints with 9 LED Lights - Disney Resort Photo Castle Picture- Wall Art for Home Decor-12x16 Inch HA-17-CP-052',
    'Simpli Better Gravity Falls - Secret Messages Poster',
    'JUYT The Owl House and Amphibia Cartoon Poster Canvas Art Poster and Wall Art Picture Print Modern Family Bedroom Decor Posters，Canvas Wall Art Living Room Posters Bedroom Painting12x18inch(30x45cm)',
    'Original Inspirational Walt Disney Quote Poster Prints, Set of 1 (8x10) Unframed Photos, Wall Art Decor Gifts Under 15 for Home, Office, School, College Student, Teens, Teacher, Partner, Literary Fan',
    'Trends International Beetlejuice-Yellow and Green Neon Wall Poster, 22.375" x 34", Unframed Version',
    'Prints Autopia Disneyland Poster (11x17) VintageTomorrowland Disney Ride Reproduction Wall Art Print',
    'Holstee Manifesto Poster - The Original This is Your Life Poster (18 in x 24 in)',
    'HUANGWW Amphibia Super Anne and Marcy Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x18inch(30x45cm)',
    'Gravity Falls Wall Art Cartoon Movie Canvas Prints Art Poster Poster For Home Office Decorations Unframed 13"x8"',
    'Disney World Photo Art Print - Meet Me On Main Street - Vintage Wall Art Poster -Chic Home Decor for Boys, Girls, Kids Bedroom, Family Room, Bathroom - Mickey Mouse, Disneyworld, Disneyland Gifts',
    'Walt Disney Patent Wall Decor - Disney World, Disneyland Rides - Wall Art Prints Poster Set - Chic Vintage Rustic Home Decor for Boys, Girls, Teens, Kids Room - Disney Gifts for Mickey Mouse Fans',
    'Lao Tzu-"People Often Fail When They Are About to Succeed"-Inspirational Quotes Wall Art -10 x 8" Spiritual Photo Print w/Bust Image-Ready to Frame. Home-Office-Studio-Spa Decor. Perfect Zen Gift!',
    'HUANGWW Amphibia Season 2 Anime Poster Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x18inch(30x45cm)',
    'HUANGWW Amphibia Season 2 Fan Art Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x18inch(30x45cm)',
    'HUANGWW Amphibia Children of The Spore Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x18inch(30x45cm)',
    'Original Disney Rides Patent Art Prints - Set of Four Photos (8x10) Unframed - Makes a Great Home Decor and Gift Under $20 for Disney Fans',
    'HUANGWW Amphibia Season 3 Fanart Canvas Art Poster and Canvas Wall Art Living Room Posters Bedroom Painting, Wall Art Picture Print Modern Family Bedroom Decor Posters 12x12inch(30x30cm)'
]


class AmazonSearch(unittest.TestCase):
    amazon_store_handler = None

    @classmethod
    def setUpClass(cls):
        cls.amazon_store_handler = AmazonStoreHandler()
        return

    def test_amazon_search(self):
        print("Step 1: Search Amazon Store...")
        self.amazon_store_handler.search_store("disney amphibia poster")
        print("success")

        print("Step 2: Process Search Results...")
        expected_search_result_count = self.amazon_store_handler.get_number_search_results_from_item_range()
        results = self.amazon_store_handler.get_search_results()
        self.assertEqual(len(results), expected_search_result_count)

        # TODO Implement Better Method For Search Result Validation
        # Use API Like Documented Above
        # for result in results:
        #     self.assertIn(result, possible_results)
        print("success")
        return

    @classmethod
    def tearDownClass(cls):
        return


if __name__ == '__main__':
    unittest.main()
