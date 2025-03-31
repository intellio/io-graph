from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesApplicationSegment(BaseModel):
	alternateUrl: Optional[str] = Field(alias="alternateUrl", default=None,)
	corsConfigurations: Optional[list[CorsConfiguration]] = Field(alias="corsConfigurations", default=None,)
	externalUrl: Optional[str] = Field(alias="externalUrl", default=None,)
	internalUrl: Optional[str] = Field(alias="internalUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cors_configuration import CorsConfiguration
