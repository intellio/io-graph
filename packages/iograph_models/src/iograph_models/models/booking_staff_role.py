from __future__ import annotations
from enum import StrEnum


class BookingStaffRole(StrEnum):
	guest = "guest"
	administrator = "administrator"
	viewer = "viewer"
	externalGuest = "externalGuest"
	unknownFutureValue = "unknownFutureValue"
	scheduler = "scheduler"
	teamMember = "teamMember"

