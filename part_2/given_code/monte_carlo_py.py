from random import seed, uniform

class MonteCarlo:
    def __init__(self):
        self.attr = {
            "pomposity" : {
                "min": 0, 
                "max": 1  
                },
            "learning_curve" : {
                "min": 1, 
                "max": 100
                },
            "optimism" : {
                "min": 0.1, 
                "max": 10},
            "atleast" : {
                "min": 0, 
                "max": 100
                },
            "done_percent" : {
                "min": 0, 
                "max": 100
                },
            "sDR_param1" : {
                "min": 0, 
                "max": 1 
                },
            "sDR_param2" : {
                "min": 1, 
                "max": 10
                },
            "sDR_param2" : {
                "min": 1, 
                "max": 10
                },
            "d" : {
                "min": 0, 
                "max": 90
                },
            "ep" : {
                "min": 1, 
                "max": 30
                },
            "nprod" : {
                "min": 0.1, 
                "max": 1
                },
            "np" : {
                "min": 1, 
                "max": 30
                },
            "ts" : {
                "min": 1, 
                "max": 10
                },
            "to" : {
                "min": 1, 
                "max": 100
                },
            "r" : {
                "min": 100, 
                "max": 1000
                },
        }

    def generator(self, iters=1):
        for i in range(int(iters)):
            row = {key: round(uniform(item["min"], item["max"]),2) for key, item in self.attr.items()}
            print(row)

import argparse

def monte_carlo_main(iters, seed_val):
    mc = MonteCarlo()
    seed(seed_val)
    mc.generator(iters)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monte Carlo generator.')
    parser.add_argument('-n', '--num-repeats', metavar='rep', type=int, default=1, help='Number of repeats')
    parser.add_argument('-s', '--seed', metavar='seed', type=int, default=1, help='Random number seed') 
    args = parser.parse_args()
    monte_carlo_main(iters=args.num_repeats, seed_val=args.seed)