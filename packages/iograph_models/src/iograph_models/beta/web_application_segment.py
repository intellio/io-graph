from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WebApplicationSegment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.webApplicationSegment"] = Field(alias="@odata.type", default="#microsoft.graph.webApplicationSegment")
	alternateUrl: Optional[str] = Field(alias="alternateUrl", default=None,)
	externalUrl: Optional[str] = Field(alias="externalUrl", default=None,)
	internalUrl: Optional[str] = Field(alias="internalUrl", default=None,)
	corsConfigurations: Optional[list[CorsConfiguration_v2]] = Field(alias="corsConfigurations", default=None,)

from .cors_configuration_v2 import CorsConfiguration_v2

