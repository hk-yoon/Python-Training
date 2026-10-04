import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--lr", type=float, default=0.001)
parser.add_argument("--batch-size", type=int, default=32)
args = parser.parse_args()
print(args.epochs, args.lr, args.batch_size)
