from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceActivityPerformanceMetric(BaseModel):
	intervalStartDateTime: Optional[datetime] = Field(alias="intervalStartDateTime",default=None,)
	percentage: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric

