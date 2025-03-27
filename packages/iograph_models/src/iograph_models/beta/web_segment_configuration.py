from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WebSegmentConfiguration(BaseModel):
	odata_type: Literal["#microsoft.graph.webSegmentConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.webSegmentConfiguration")
	applicationSegments: Optional[list[WebApplicationSegment]] = Field(alias="applicationSegments", default=None,)

from .web_application_segment import WebApplicationSegment

