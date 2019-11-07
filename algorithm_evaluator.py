import os

from detector import Detector


class AlgorithmEvaluator:

    @staticmethod
    def run_evaluation():
        base_path = os.path.dirname(os.path.realpath(__file__))
        succesful_classifications = 0
        names = []
        for root, sub, filenames in os.walk(os.path.join(base_path, 'sample_Signature')):
            for filename in filenames:
                names.append(filename)

        for name in names:
            print(name)
            algorithm_result = Detector.is_signature_real(name)
            correct_result = name[-7:-4] == name[4: 7]
            if algorithm_result == correct_result:
                succesful_classifications += 1
        return succesful_classifications / len(names)


print(f'accuracy is {AlgorithmEvaluator.run_evaluation()*100}%')
