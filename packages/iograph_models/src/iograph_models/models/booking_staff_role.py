from __future__ import annotations
from enum import Enum


class BookingStaffRole(Enum):
	guest = "guest"
	administrator = "administrator"
	viewer = "viewer"
	externalGuest = "externalGuest"
	unknownFutureValue = "unknownFutureValue"
	scheduler = "scheduler"
	teamMember = "teamMember"

