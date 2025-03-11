from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeCard(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	breaks: Optional[list[TimeCardBreak]] = Field(alias="breaks",default=None,)
	clockInEvent: Optional[TimeCardEvent] = Field(alias="clockInEvent",default=None,)
	clockOutEvent: Optional[TimeCardEvent] = Field(alias="clockOutEvent",default=None,)
	confirmedBy: Optional[ConfirmedBy | str] = Field(alias="confirmedBy",default=None,)
	notes: Optional[ItemBody] = Field(alias="notes",default=None,)
	originalEntry: Optional[TimeCardEntry] = Field(alias="originalEntry",default=None,)
	state: Optional[TimeCardState | str] = Field(alias="state",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .time_card_break import TimeCardBreak
from .time_card_event import TimeCardEvent
from .time_card_event import TimeCardEvent
from .confirmed_by import ConfirmedBy
from .item_body import ItemBody
from .time_card_entry import TimeCardEntry
from .time_card_state import TimeCardState

