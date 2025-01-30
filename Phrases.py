# Simply a list of phrases that will randomly be chosen for the user to guess.

from Caesar_Guesser import * 
class Phrase():
    def __init__(self):
        self.phrases: list = ["A dime a dozen", "All in the same boat", "Barking up the wrong tree", "Beat around the bush", "Burning the candle at both ends",
                "Caught between a rock and a hard place", "Don't cry over spilled milk", "Fish out of water", "Give the benefit of the doubt",
                "Head in the clouds", "It takes two to tango", "Let sleeping dogs lie", "Roll with the punches", 
                "The tip of the iceberg", "A blessing in disguise", "Actions speak louder than words", "An arm and a leg", "Back to square one", "Burn the midnight oil", 
                "Easy come, easy go", "Every cloud has a silver lining", "Go the extra mile", "Hit the ground running", "In the same boat", "Jump on the bandwagon", 
                "Kill two birds with one stone", "Leave no stone unturned", "The last straw", "Throw in the towel", "Break a leg", "Better late than never", "Bite the bullet", 
                "Call it a day", "Cut to the chase", "Hit the nail on the head", "Let the cat out of the bag", "Miss the boat", "Once in a blue moon", "Piece of cake", 
                "Pull someone's leg", "Speak of the devil", "Spill the beans", "The ball is in your court", "Under the weather", "A bird in the hand is worth two in the bush", 
                "A picture is worth a thousand words", "A watched pot never boils", "Actions speak louder than words", "Add fuel to the fire", "All in a day's work", "All ears",
                "An eye for an eye", "Bite the hand that feeds you", "Break the ice", "By the book", "Cry over spilled milk", "Curiosity killed the cat", 
                "Don't bite off more than you can chew", "Don't count your chickens before they hatch", "Don't judge a book by its cover", "Don't put all your eggs in one basket", 
                "Easy does it", "Every dog has its day", "Get a taste of your own medicine", "Give someone the cold shoulder", "Go for broke", "Hit the nail on the head", 
                "In a nutshell", "In hot water", "It's not rocket science", "Jump the gun", "Keep your head above water", "Know the ropes", "Let the chips fall where they may", 
                "Make a long story short", "Miss the boat", "No pain, no gain", "On the same page", "Out of the blue", "Out of the frying pan and into the fire", "Play it by ear", 
                "Pull the plug", "Put all your eggs in one basket", "Put your money where your mouth is", "Read between the lines", "Rome wasn't built in a day", 
                "Save it for a rainy day", "Shoot the breeze", "Sit tight", "Steal someone's thunder", "The ball is in your court", 
                "The best of both worlds", "The early bird catches the worm", "The grass is always greener on the other side", "The straw that broke the camel's back",
                "Through thick and thin", "Tie the knot", "Turn a blind eye", "Under the weather", "Up in the air", "You can't judge a book by its cover", 
                "You can't have your cake and eat it too", "You win some, you lose some", "Your guess is as good as mine", "All's well that ends well", "An arm and a leg", 
                "Back to the drawing board", "Be a fly on the wall", "Beat around the bush", "Better safe than sorry", "Blow off steam", "Break the bank", 
                "Burning the midnight oil", "Call it a day", "Cut to the chase", "Hit the sack", "In the blink of an eye", "Saved by the bell", "Be careful what you wish for", 
                "You are on thin ice"]

    def get_phrases(self) -> list:
        return self.phrases


