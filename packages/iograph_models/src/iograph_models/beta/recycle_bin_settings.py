from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecycleBinSettings(BaseModel):
	retentionPeriodOverrideDays: Optional[int] = Field(alias="retentionPeriodOverrideDays", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


