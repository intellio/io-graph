from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessApplications(BaseModel):
	applicationFilter: Optional[ConditionalAccessFilter] = Field(alias="applicationFilter", default=None,)
	excludeApplications: Optional[list[str]] = Field(alias="excludeApplications", default=None,)
	includeApplications: Optional[list[str]] = Field(alias="includeApplications", default=None,)
	includeAuthenticationContextClassReferences: Optional[list[str]] = Field(alias="includeAuthenticationContextClassReferences", default=None,)
	includeUserActions: Optional[list[str]] = Field(alias="includeUserActions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_filter import ConditionalAccessFilter
