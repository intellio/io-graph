from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebSegmentConfiguration(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationSegments: Optional[list[WebApplicationSegment]] = Field(alias="applicationSegments",default=None,)

from .web_application_segment import WebApplicationSegment

