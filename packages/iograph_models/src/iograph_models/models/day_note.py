from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DayNote(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	dayNoteDate: Optional[str] = Field(default=None,alias="dayNoteDate",)
	draftDayNote: Optional[ItemBody] = Field(default=None,alias="draftDayNote",)
	sharedDayNote: Optional[ItemBody] = Field(default=None,alias="sharedDayNote",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_body import ItemBody
from .item_body import ItemBody

