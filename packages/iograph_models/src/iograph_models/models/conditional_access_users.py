from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessUsers(BaseModel):
	excludeGroups: Optional[list[str]] = Field(default=None,alias="excludeGroups",)
	excludeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(default=None,alias="excludeGuestsOrExternalUsers",)
	excludeRoles: Optional[list[str]] = Field(default=None,alias="excludeRoles",)
	excludeUsers: Optional[list[str]] = Field(default=None,alias="excludeUsers",)
	includeGroups: Optional[list[str]] = Field(default=None,alias="includeGroups",)
	includeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(default=None,alias="includeGuestsOrExternalUsers",)
	includeRoles: Optional[list[str]] = Field(default=None,alias="includeRoles",)
	includeUsers: Optional[list[str]] = Field(default=None,alias="includeUsers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers
from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

