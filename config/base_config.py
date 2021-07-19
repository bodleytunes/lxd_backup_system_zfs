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
        pass

    def _get_base_config(self, config_file):
        # use confuse to parse config file
        config = confuse.Configuration("lxdbackup", __name__)
        config.set_file(config_file)  # set the specific config file
        return config

    def get_backup_jobs(self) -> Dict:
        cfg = self.config.get()
        return cfg["lxd"]["backup"]["jobs"]

    def get_job_containers(self, job) -> Dict:
        return self.config["lxd"]["backup"][job]["containers"]
