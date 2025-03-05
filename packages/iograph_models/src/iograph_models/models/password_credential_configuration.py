from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordCredentialConfiguration(BaseModel):
	maxLifetime: Optional[str] = Field(default=None,alias="maxLifetime",)
	restrictForAppsCreatedAfterDateTime: Optional[datetime] = Field(default=None,alias="restrictForAppsCreatedAfterDateTime",)
	restrictionType: Optional[AppCredentialRestrictionType] = Field(default=None,alias="restrictionType",)
	state: Optional[AppManagementRestrictionState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .app_credential_restriction_type import AppCredentialRestrictionType
from .app_management_restriction_state import AppManagementRestrictionState

