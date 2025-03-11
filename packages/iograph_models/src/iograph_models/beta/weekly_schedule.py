from __future__ import annotations
from enum import StrEnum


class WeeklySchedule(StrEnum):
	userDefined = "userDefined"
	everyday = "everyday"
	sunday = "sunday"
	monday = "monday"
	tuesday = "tuesday"
	wednesday = "wednesday"
	thursday = "thursday"
	friday = "friday"
	saturday = "saturday"
	noScheduledScan = "noScheduledScan"

