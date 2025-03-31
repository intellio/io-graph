from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IpSegmentConfiguration(BaseModel):
	odata_type: Literal["#microsoft.graph.ipSegmentConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.ipSegmentConfiguration")
	applicationSegments: Optional[list[IpApplicationSegment]] = Field(alias="applicationSegments", default=None,)

from .ip_application_segment import IpApplicationSegment
