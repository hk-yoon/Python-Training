class Sequence:
    @staticmethod
    def is_valid_base(base):
        return base in {"A", "T", "G", "C"}
print(Sequence.is_valid_base("A"))
