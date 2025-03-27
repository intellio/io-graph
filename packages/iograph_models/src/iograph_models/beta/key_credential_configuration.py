from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class KeyCredentialConfiguration(BaseModel):
	certificateBasedApplicationConfigurationIds: Optional[list[str]] = Field(alias="certificateBasedApplicationConfigurationIds", default=None,)
	maxLifetime: Optional[str] = Field(alias="maxLifetime", default=None,)
	restrictForAppsCreatedAfterDateTime: Optional[datetime] = Field(alias="restrictForAppsCreatedAfterDateTime", default=None,)
	restrictionType: Optional[AppKeyCredentialRestrictionType | str] = Field(alias="restrictionType", default=None,)
	state: Optional[AppManagementRestrictionState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
from .app_management_restriction_state import AppManagementRestrictionState

