import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import json



if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('test_cases')
    with open('results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
    with open("results.json", 'r', encoding='utf-8') as json_data:
        json_content = json.load(json_data)
        json_data.close()

    print("Autograder results:\n")
    score_earned = 0
    max_score = 0
    for i, result in enumerate(json_content["tests"]):
        print("Test case:{}. Score (earned/max): {}/{}".format(i,result['score'],result['max_score']))
        print("Test case name:{}. Status: {}".format(result['name'],result['status']))

        if "output" in result.keys():
            print("Reason:{}".format(result['output']))
        score_earned += result['score']
        max_score += result['max_score']
        print("\n")
    print("Final score (earned/max): {}/{}".format(score_earned,max_score))

