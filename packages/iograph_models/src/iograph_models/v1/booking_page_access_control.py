from __future__ import annotations
from enum import StrEnum


class BookingPageAccessControl(StrEnum):
	unrestricted = "unrestricted"
	restrictedToOrganization = "restrictedToOrganization"
	unknownFutureValue = "unknownFutureValue"

