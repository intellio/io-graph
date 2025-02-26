from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessUsers(BaseModel):
	excludeGroups: list[str] = Field(alias="excludeGroups",)
	excludeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(default=None,alias="excludeGuestsOrExternalUsers",)
	excludeRoles: list[str] = Field(alias="excludeRoles",)
	excludeUsers: list[str] = Field(alias="excludeUsers",)
	includeGroups: list[str] = Field(alias="includeGroups",)
	includeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(default=None,alias="includeGuestsOrExternalUsers",)
	includeRoles: list[str] = Field(alias="includeRoles",)
	includeUsers: list[str] = Field(alias="includeUsers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers
from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

