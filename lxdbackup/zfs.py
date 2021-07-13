from dataclasses import dataclass

from abc import ABC
from typing import Any, List

from zfslib import zfslib as zfs


@dataclass
class ZfsDataset:
    full_path: str
    split_path: list


@dataclass
class ZfsPool:
    name: str
    zfs_datasets: List[ZfsDataset]


@dataclass
class ZfsDetails:
    host: str
    zfs_pools: List[ZfsPool]


class ZfsUtil:
    def __init__(self, host: str) -> None:
        self.host = host
        # setups / initiations
        self._get_conn()
        self._get_poolset()

        self.datasets: List = list()
        self._get_pool_datasets()
        self._get_pool_dataset_paths()
        self._get_pool_dataset_names()
        self._get_pool_lxd_dataset_names()
        self._get_pool_lxd_dataset_paths()

        pass

    def _get_conn(self):
        self.conn = zfs.Connection(host=self.host)

    def _get_poolset(self):
        self.poolset = self.conn.load_poolset()

    def get_pool_names(self):
        for p in self.poolset:
            print(p.name)

    def _get_pool_datasets(self):
        self.datasets = [p.get_all_datasets() for p in self.poolset]

    def _get_pool_dataset_paths(self):
        self.all_dataset_paths = [i.path for d in self.datasets for i in d]

    def _get_pool_dataset_names(self):
        self.all_dataset_names = [i.name for d in self.datasets for i in d]

    def _get_pool_lxd_dataset_names(self):
        self.all_lxd_dataset_names = [
            i.name
            for d in self.datasets
            for i in d
            if "lxd/containers" in i.path and i.name != "containers"
        ]
        print(self.all_lxd_dataset_names)

    def _get_pool_lxd_dataset_paths(self):
        self.all_lxd_dataset_paths = [
            i.path
            for d in self.datasets
            for i in d
            if "lxd/containers" in i.path and i.name != "containers"
        ]

    def print_dataset_names(self):
        for n in self.all_lxd_dataset_names:
            print(f"dataset name:  {n}")

    def print_dataset_paths(self):
        for p in self.all_lxd_dataset_paths:
            print(f"dataset path:  {p}")

    def get_dataset_from_container_name(self, container_name: str):
        if container_name in self.all_lxd_dataset_paths:
            return True
        else:
            return False
