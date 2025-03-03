from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessApplications(BaseModel):
	applicationFilter: Optional[ConditionalAccessFilter] = Field(default=None,alias="applicationFilter",)
	excludeApplications: Optional[list[str]] = Field(default=None,alias="excludeApplications",)
	includeApplications: Optional[list[str]] = Field(default=None,alias="includeApplications",)
	includeAuthenticationContextClassReferences: Optional[list[str]] = Field(default=None,alias="includeAuthenticationContextClassReferences",)
	includeUserActions: Optional[list[str]] = Field(default=None,alias="includeUserActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_filter import ConditionalAccessFilter

