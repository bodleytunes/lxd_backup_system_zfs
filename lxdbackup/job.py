from lxdbackup.config.base_config import BackupConfig


class Job:
    def __init__(self, bc: BackupConfig) -> None:
        self.bc = bc
        self.jobs: list
        self.job_containers: dict
        pass

    @property
    def jobs(self):
        return self.bc.backup_jobs

    @property
    def job_containers(self):
        return self.bc.get_job_containers(0)
