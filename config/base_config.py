from confuse.core import Configuration
import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Dict
import pytest

import confuse

# from pytest import fixture
from pytest_cases import fixture


class BackupConfig:
    def __init__(self, config_file) -> None:
        self.config = self._get_base_config(config_file)
        self.lxd = self.config.get()
        self._set_backup_jobs()

        pass

    def _get_base_config(self, config_file):
        # use confuse to parse config file
        config = confuse.Configuration("lxdbackup", __name__)
        config.set_file(config_file)  # set the specific config file
        return config

    def _set_backup_jobs(self):
        cfg = self.config.get()
        self.backup_jobs = cfg["lxd"]["backup"]["jobs"]

    def get_backup_jobs(self):
        return self.backup_jobs

    def get_job_containers(self, job) -> Dict:
        return self.config["lxd"]["backup"][job]["containers"]
