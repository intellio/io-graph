from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActivityTimeSet(BaseModel):
	lastRecordedDateTime: Optional[datetime] = Field(alias="lastRecordedDateTime", default=None,)
	observedDateTime: Optional[datetime] = Field(alias="observedDateTime", default=None,)
	recordedDateTime: Optional[datetime] = Field(alias="recordedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


