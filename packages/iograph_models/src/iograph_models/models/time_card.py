from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeCard(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	breaks: Optional[list[TimeCardBreak]] = Field(default=None,alias="breaks",)
	clockInEvent: Optional[TimeCardEvent] = Field(default=None,alias="clockInEvent",)
	clockOutEvent: Optional[TimeCardEvent] = Field(default=None,alias="clockOutEvent",)
	confirmedBy: Optional[ConfirmedBy] = Field(default=None,alias="confirmedBy",)
	notes: Optional[ItemBody] = Field(default=None,alias="notes",)
	originalEntry: Optional[TimeCardEntry] = Field(default=None,alias="originalEntry",)
	state: Optional[TimeCardState] = Field(default=None,alias="state",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_card_break import TimeCardBreak
from .time_card_event import TimeCardEvent
from .time_card_event import TimeCardEvent
from .confirmed_by import ConfirmedBy
from .item_body import ItemBody
from .time_card_entry import TimeCardEntry
from .time_card_state import TimeCardState

