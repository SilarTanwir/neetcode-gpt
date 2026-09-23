class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def gradient(x):
            return 2*x
        
        answer = init
        for i in range(iterations):
            answer -= gradient(answer)*learning_rate

        return round(answer, 5)
