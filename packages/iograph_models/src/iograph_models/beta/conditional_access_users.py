from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessUsers(BaseModel):
	excludeGroups: Optional[list[str]] = Field(alias="excludeGroups",default=None,)
	excludeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(alias="excludeGuestsOrExternalUsers",default=None,)
	excludeRoles: Optional[list[str]] = Field(alias="excludeRoles",default=None,)
	excludeUsers: Optional[list[str]] = Field(alias="excludeUsers",default=None,)
	includeGroups: Optional[list[str]] = Field(alias="includeGroups",default=None,)
	includeGuestsOrExternalUsers: Optional[ConditionalAccessGuestsOrExternalUsers] = Field(alias="includeGuestsOrExternalUsers",default=None,)
	includeRoles: Optional[list[str]] = Field(alias="includeRoles",default=None,)
	includeUsers: Optional[list[str]] = Field(alias="includeUsers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers
from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

