from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IpSegmentConfiguration(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationSegments: Optional[list[IpApplicationSegment]] = Field(alias="applicationSegments",default=None,)

from .ip_application_segment import IpApplicationSegment

