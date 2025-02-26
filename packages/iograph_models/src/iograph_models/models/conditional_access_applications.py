from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessApplications(BaseModel):
	applicationFilter: Optional[ConditionalAccessFilter] = Field(default=None,alias="applicationFilter",)
	excludeApplications: list[str] = Field(alias="excludeApplications",)
	includeApplications: list[str] = Field(alias="includeApplications",)
	includeAuthenticationContextClassReferences: list[str] = Field(alias="includeAuthenticationContextClassReferences",)
	includeUserActions: list[str] = Field(alias="includeUserActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_filter import ConditionalAccessFilter

