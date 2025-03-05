from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingStaffMemberBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: SerializeAsAny[Optional[list[BookingStaffMemberBase]]] = Field(default=None,alias="value",)

from .booking_staff_member_base import BookingStaffMemberBase

