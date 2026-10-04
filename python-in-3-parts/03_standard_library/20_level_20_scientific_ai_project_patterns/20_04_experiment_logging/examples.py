import logging
logging.basicConfig(filename="train.log", level=logging.INFO)
epochs, lr = 20, 0.001
logging.info("Training started: epochs=%d, lr=%f", epochs, lr)
print("Wrote train.log")
