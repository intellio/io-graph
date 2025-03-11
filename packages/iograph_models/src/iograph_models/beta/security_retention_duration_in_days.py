from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionDurationInDays(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	days: Optional[int] = Field(alias="days",default=None,)


