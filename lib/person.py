#!/usr/bin/env python3

class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name, job):
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            raise ValueError("Job must be in the list of approved jobs.")