class Calculation:
    def __init__(self):
        self.scores = {
            "Kamala": 0,
            "Trump": 0
        }

        # Array of questions and their associated candidates and stances
        self.questions = [
            {
                "question": "Do you agree that corporate tax should be increased?", 
                "candidate": "Kamala", 
                "stance": "increasetax"
            },
            {
                "question": "Do you think immigrants should be restricted from entering the country?", 
                "candidate": "Trump", 
                "stance": "restrictimmigration"
            },

            {
                
                "question": "Do you think police should have immunity?", 
                "candidate": "Trump", 
                "stance": "immunityPolice"
            }
        ]

    def calculate_score(self, emotion, stance):
        """
        This method calculates the score based on emotion and the stance of the candidate.
        """
        if stance == "increasetax":
            if emotion in ["happy"]:
                self.scores["Kamala"] += 1  # Kamala's score increases
            elif emotion in ["sad"]:
                self.scores["Trump"] += 1  # Trump's score increases
        
        elif stance == "restrictimmigration":
            if emotion in ["happy"]:
                self.scores["Trump"] += 1  # Trump's score increases
            elif emotion in ["sad"]:
                self.scores["Kamala"] += 1  # Kamala's score increases
        elif stance == "immunityPolice":
            if emotion in ["happy", "smile"]:
                self.scores["Trump"]+=1
            elif emotion in ["sad"]:
                self.scores["Kamala"]+=1

    def get_score(self, figure):
    
        return self.scores.get(figure, 0)

    def process_responses(self, responses):
       
        for response in responses:
            question = response["question"]
            detected_emotion = response["emotion"]

            print(f"Question: {question}")
            print(f"Detected emotion: {detected_emotion}")

           
            matching_question = next(q for q in self.questions if q["question"] == question)
            candidate_stance = matching_question["stance"]

            # Calculate the score based on the detected emotion
            self.calculate_score(detected_emotion, candidate_stance)

            # Print the current score for both Kamala and Trump
            print(f"Current score for Kamala: {self.get_score('Kamala')}")
            print(f"Current score for Trump: {self.get_score('Trump')}")
            print("------")

    

    

scorer = Calculation()

# Fake responses for testing
responses = [
    {"question": "Do you agree that corporate tax should be increased?", "emotion": "happy"},  # Kamala's stance
    {"question": "Do you think immigrants should be restricted from entering the country?", "emotion": "happy"},
    {"question": "Do you think police should have immunity?", "emotion":"happy"}
]

# Process each response and calculate the score
scorer.process_responses(responses)
