import argparse


def parse_arguments(parser):
    parser.add_argument('--type', type=str)
    args = parser.parse_args()
    return args


parser = argparse.ArgumentParser()
args = parse_arguments(parser)
inp = open("trainset/" + args.type, "r")
oup = open("output2/" + args.type, 'r')

stat = open("stat" + args.type, 'a')

wrong = 0

for i in range(8000):
    a = float(oup.readline())
    if (a > 0.5):
        if int(inp.readline().split('\t')[1]) == 0:
            wrong += 1
    else:
        if int(inp.readline().split('\t')[1]) == 1:
            wrong += 1

inp.close()
oup.close()
per = wrong / 80
outstr = "The wrong prediction of RNA %s is %d, %f%%" % (args.type, wrong, per)
print(outstr)
stat.write(outstr)
stat.write('\n')
stat.close()
