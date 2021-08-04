class DatasetCheck:
    def __init__(self) -> None:
        pass

    def check_for_existing_dataset(self, datasets: list):

        pass


# I want to check for an existing dataset, and if it doesn't exist then create one
# CheckDataset, CreateDataset

# Feature: DatasetCheck

# Scenario: Check for existing LXD dataset
# Given:
# When I search all lxd datasets in a zpool
# Then: I should find at least one with the string lxd in it

# Given:
# when i search for all  lxd datasets in a pool and don't find any
# then: I should create a new single lxd dataset


class DatasetCreator:
    def __init__(self) -> None:
        pass

    def create_dataset(self, zpool_name):
        pass
