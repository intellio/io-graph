from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CorsConfiguration_v2CollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CorsConfiguration_v2]] = Field(alias="value",default=None,)

from .cors_configuration_v2 import CorsConfiguration_v2

