from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceActivityValueMetric(BaseModel):
	intervalStartDateTime: Optional[datetime] = Field(alias="intervalStartDateTime",default=None,)
	value: Optional[int] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


