import os


class Utils:
    @staticmethod
    def _split_path(dataset_path):
        component_paths = os.path.split(dataset_path)
        return component_paths[0]
