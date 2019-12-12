# Profitability cases
# Market Entry/General framework (Product, Consumer, Company, Competition)
# 3Cs framework / porters 5 forces
# M&A framework
# math problems (with a lot of zeros)
# Math formulas (Revenue, cost, profit, ROI, break-even, profit margin)
# Fit Qs
# PEI Qs (tough situation, disagreement with boss, overcame difficult challenge
# Understand the 7 different Qs and identify what framework/structure to use
# Situation
# Framework development
# framework exploration
# Quant-DataProvided
# Quant-NoDataProvided
# Creativity
# Recommendation

import random

sys_random = random.SystemRandom()
multdiv = "*/"
thousandsmillionsbillions = "kmb"

for _ in range(1000):
    value1 = random.randint(0, 1000)
    value2 = random.choice(multdiv)
    value3 = random.randint(0, 1000)
    value4 = random.choice(thousandsmillionsbillions)

profit = """
    Case Q:
    Our profits are down, what should we do?
    """
newproduct = """
    Case Q:
    We would like to launch a new product. How should we do it?
    """
newmarket = """
    Case Q:
    We would like to enter a new market. How should we do it?
    """
MnA = """
    We are thinking about buying a competitor of ours.
    What aspects should we look at and should we do it?
    """

mathnumbers = [value1, value2, value3, value4]

mathformulas = """
        What's the formula for:
        - REVENUE
        - COST
        - PROFIT
        - PROFIT MARGIN
        - ROI
        - BREAKEVEN/payback period
        """
fit = """
    Why this company?
    Why consulting?
    Walk me through your resume.
    Tell me something not on your resume.
    tell me about your greatest accomplishment.
    """
pei = """
    Tell me about a time when you;
    - lead a team through a tough situation.
    - worked in a team and had to manage a conflict.
    - had a disagreement with a colleague / boss.
    - had to change someone's / a groups mind.
    - overcame a really difficult challange.
    """

database = [profit,
            newproduct,
            newmarket,
            MnA,
            mathnumbers,
            mathformulas,
            fit,
            pei,
            ]

print(sys_random.choice(database))
