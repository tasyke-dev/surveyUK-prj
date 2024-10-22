import json
import sys
sys.stdout.encoding

def loadJSON(pathToFile):

    with open(pathToFile,'r',encoding='utf-8') as f:
            data=json.load(f)

    return data


class SurveyCalculator:

    def __init__(self,answers:dict):
        self.answers=answers

    
    def calculateCategories(self,jsonData):

        self.scores={"P":0,"W":0,"F":0,"R":0}
        self.categoriesCount={"P":0,"W":0,"F":0,"R":0}

        for id,value in self.answers.items():
            score=int(value)

            questionCat=jsonData[id]

            if questionCat['Reversed']:
                score=5-int(self.answers[id])
                
            self.scores[questionCat['flag']]+=score

            self.categoriesCount[questionCat['flag']]+=1


        self.total_score= sum(self.scores.values())

        self.total_wo_R=self.total_score-self.scores["R"]

        solvedQuestions=sum(self.categoriesCount.values())


        self.div_total_score=self.total_score/solvedQuestions

        self.div_total_wo_R=self.total_wo_R/(solvedQuestions-self.categoriesCount['R'])
        
        self.div_scores={}
        for flag in self.scores.keys():
            self.div_scores[flag]=self.scores[flag]/self.categoriesCount[flag]


        print(self.categoriesCount)


        for category, score in self.scores.items():
            print(f"{category} category total score is: {score}")

        print(f"Total score is: {self.total_score}")
        print(f"Total score w/o R is: {self.total_wo_R}")


        for category,div_score in self.div_scores.items():
            print(f"{category} category divided scores is:: {div_score}")

        print(f"Total divided score: {self.div_total_score}")
        print(f"Total divided score w/o R: {self.div_total_wo_R}")




