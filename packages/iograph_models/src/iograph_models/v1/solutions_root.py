from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SolutionsRoot(BaseModel):
	backupRestore: Optional[BackupRestoreRoot] = Field(alias="backupRestore", default=None,)
	bookingBusinesses: Optional[list[BookingBusiness]] = Field(alias="bookingBusinesses", default=None,)
	bookingCurrencies: Optional[list[BookingCurrency]] = Field(alias="bookingCurrencies", default=None,)
	virtualEvents: Optional[VirtualEventsRoot] = Field(alias="virtualEvents", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .backup_restore_root import BackupRestoreRoot
from .booking_business import BookingBusiness
from .booking_currency import BookingCurrency
from .virtual_events_root import VirtualEventsRoot

