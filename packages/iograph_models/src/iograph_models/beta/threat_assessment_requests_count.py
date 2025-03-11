from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ThreatAssessmentRequestsCount(BaseModel):
	count: Optional[int] = Field(alias="count",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	pivotValue: Optional[str] = Field(alias="pivotValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


