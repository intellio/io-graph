from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DayNote(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	dayNoteDate: Optional[str] = Field(alias="dayNoteDate",default=None,)
	draftDayNote: Optional[ItemBody] = Field(alias="draftDayNote",default=None,)
	sharedDayNote: Optional[ItemBody] = Field(alias="sharedDayNote",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_body import ItemBody
from .item_body import ItemBody

