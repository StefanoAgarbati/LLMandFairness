class SplitRepository:

    def __init__(self):
        self.splits = []

    def add_split(self, split):
        #item = {"name": name, "split": split}
        #print(f"SplitRepository -> split {split.get_name()} added")
        self.splits.append(split)

    def get_split_by_name(self, name):
        #print(f"SplitRepository -> get_split_by_name({name})")
        for split in self.splits:
            if split.get_name() == name:
                return split
        raise Exception(f"SplitRepository -> The split {name} doesn't exist")
