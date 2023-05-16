import argparse

parser = argparse.ArgumentParser(description='Data Processing.')

parser.add_argument("-il", "--input_link", help="link folder of input.", default="data/input", type=str)
parser.add_argument("-ll", "--label_link", help="link of label.", default="data/label", type=str)
parser.add_argument("-ol", "--output_link", help="link of output.", default="data/output", type=str)
parser.add_argument("-fl", "--flag_suppressed", help="flag.", default=False, type=bool)

args = parser.parse_args()

print(args)