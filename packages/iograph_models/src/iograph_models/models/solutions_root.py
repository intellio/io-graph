from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SolutionsRoot(BaseModel):
	backupRestore: Optional[BackupRestoreRoot] = Field(default=None,alias="backupRestore",)
	bookingBusinesses: list[BookingBusiness] = Field(alias="bookingBusinesses",)
	bookingCurrencies: list[BookingCurrency] = Field(alias="bookingCurrencies",)
	virtualEvents: Optional[VirtualEventsRoot] = Field(default=None,alias="virtualEvents",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .backup_restore_root import BackupRestoreRoot
from .booking_business import BookingBusiness
from .booking_currency import BookingCurrency
from .virtual_events_root import VirtualEventsRoot

