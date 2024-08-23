from django.test import TestCase
from quotes import ml

class MoodTester(TestCase):
    """Test to predict mood"""
    
    def test_happy_mood(self):
        """Test to predict happy mood"""
        self.assertEqual(ml.predict_mood("I am feeling great and very happy!"), 'happy')

    def test_sad_mood(self):
        """Test to predict sad mood"""
        self.assertEqual(ml.predict_mood("I am feeling very down and sad."), 'sad')

    def test_stressed_mood(self):
        """Test to predict stressed mood"""
        self.assertEqual(ml.predict_mood("I am overwhelmed and anxious about the workload."), 'stressed')

    def test_motivated_mood(self):
        """Test to predict motivated mood"""
        self.assertEqual(ml.predict_mood("I am highly motivated and ready to achieve my goals!"), 'motivated')

    def test_neutral_mood(self):
        """Test to predict neutral mood"""
        self.assertEqual(ml.predict_mood("Just another day."), 'neutral')

    def test_empty_text(self):
        """Test to predict mood with empty text"""
        self.assertEqual(ml.predict_mood(""), 'neutral')

    def test_none_text(self):
        """Test to predict mood with None text"""
        self.assertEqual(ml.predict_mood(None), 'neutral')