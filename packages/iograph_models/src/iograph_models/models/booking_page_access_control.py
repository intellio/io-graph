from __future__ import annotations
from enum import Enum


class BookingPageAccessControl(Enum):
	unrestricted = "unrestricted"
	restrictedToOrganization = "restrictedToOrganization"
	unknownFutureValue = "unknownFutureValue"

