import os

from typing import List

from zfslib import zfslib as zfs


class ZfsUtil:
    def __init__(self, host: str, user: str) -> None:
        self.host = host
        self.user = user
        # setups / initiations
        self._get_conn()
        self._get_poolset()

        self.datasets: List = list()
        self._get_pool_datasets()
        self._get_pool_dataset_paths()
        self._get_pool_dataset_names()
        self._get_pool_lxd_dataset_names()
        self._get_pool_lxd_dataset_paths()
        self._set_dataset_path()
        self._get_pool_lxd_dataset_mounts()
        self._set_mount_paths()


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

    def _get_pool_lxd_dataset_mounts(self):
        self.all_lxd_dataset_mountpoints = [
            i.mountpoint
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

    def set_source_container(self, container_name: str):
        for path in self.all_lxd_dataset_paths:
            if container_name in path:
                self.source_container_path = path
                return

    def set_destination_container(self, container_name: str):
        self.destination_container_path = str(
            f"{self.lxd_dataset_path}/{container_name}"
        )

    def _set_dataset_path(self):
        if len(self.all_lxd_dataset_paths) > 0:
            self.lxd_dataset_path = self._split_path(self.all_lxd_dataset_paths[0])

    def _set_mount_paths(self):
        if len(self.all_lxd_dataset_mountpoints) > 0:
            all_lxd_mount_paths = [
                self._split_path(mount)
                for mount in self.all_lxd_dataset_mountpoints
                if mount != "none"
            ]
            self.all_lxd_mount_paths = self._make_unique_list(all_lxd_mount_paths)

    def _make_unique_list(self, non_unique_list: list):
        return set(non_unique_list)

    def _get_dataset_mounts(self):

        self.all_dataset_paths = [i.path for d in self.datasets for i in d]

    def _set_zfs_mounts(self):
        pass

    def _split_path(self, dataset_path):
        component_paths = os.path.split(dataset_path)
        return component_paths[0]


class Mounter:
    def __init__(self) -> None:
        pass

    def get_zfs_mountpoints(self):
        # todo
        # self.zfs_mountpoints = mountpoints
        pass

    def set_zfs_mountpoint(self, container):
        pass

    def mount_container(self):
        pass


class BackupFile:
    def __init__(self) -> None:
        pass

    def find_backup_file():
        pass

    def modify_backup_file():
        pass

    def modify_pool_source():
        pass

    def modify_pool_name():
