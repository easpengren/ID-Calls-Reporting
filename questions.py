#!/usr/bin/env python3

#QUESTIONS_ANSWERS_LOOKUP = [
#
#    ['intro',
#     'Hi, my name is ________ and I’m working with Collective PAC North Carolina to talk to voters about the upcoming election. May I please speak with ______________?'],
#    ['q1', 'Hi _________, are you planning to vote in the upcoming election? (mark answer)'],
#    ['q1a', 'Okay, I understand. Is there a specific reason why you aren’t planning to vote?'],
#    ['q2',
#     'Okay, that’s great! I’m so excited you’re planning to vote! Do you know if you’ll be voting by mail, voting in person early, or voting on election day? (mark answer)'],
#    ['q2a', 'Have you submitted your vote by mail application? (mark answer)'],
#    ['q2b', 'Do you know when you’re planning to vote early?'],
#    ['q2c', 'Would you be open to voting early in person?']
#]

#QUESTIONS_ANSWERS_LOOKUP_DICT = {question[0]:question[1:] for question in QUESTIONS_ANSWERS_LOOKUP}
#questions_dict = QUESTIONS_ANSWERS_LOOKUP_DICT

QUESTIONS_ANSWERS_LOOKUP = [
    ['intro', 'My name is ________________ and I’m calling on behalf of the Collective PAC. We are calling to ensure everyone interested in registering to vote through votetolive.org has completed the process.'],
    ['q1', 'Have you completed an application to register to vote by printing, signing and mailing to your county election office?'],
    ['q2', 'Have you received your voter registration certificate?']
]

QUESTIONS_ANSWERS_LOOKUP_DICT = {question[0]:question[1:] for question in QUESTIONS_ANSWERS_LOOKUP}
questions_dict = QUESTIONS_ANSWERS_LOOKUP_DICT
