from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CorsConfiguration(BaseModel):
	allowedHeaders: Optional[list[str]] = Field(alias="allowedHeaders", default=None,)
	allowedMethods: Optional[list[str]] = Field(alias="allowedMethods", default=None,)
	allowedOrigins: Optional[list[str]] = Field(alias="allowedOrigins", default=None,)
	maxAgeInSeconds: Optional[int] = Field(alias="maxAgeInSeconds", default=None,)
	resource: Optional[str] = Field(alias="resource", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

