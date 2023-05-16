import argparse

parser = argparse.ArgumentParser(description='Elasticsearch.')

parser.add_argument("-acc", "--account", help="Account of Elasticsearch.", default="elastic", type=str)
parser.add_argument("-pw", "--password", help="Password of Elasticsearch.", default=None, type=str)
parser.add_argument("-ix", "--index", help="Index name.", default="es_coliee", type=str)

parser.add_argument("-il", "--input_link", help="link of input", default="data/input", type=str)
parser.add_argument("-ol", "--output_link", help="link of folder output.", default="data/output", type=str)


args = parser.parse_args()

print(args)