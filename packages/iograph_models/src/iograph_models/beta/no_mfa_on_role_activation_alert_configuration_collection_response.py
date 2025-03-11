from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NoMfaOnRoleActivationAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NoMfaOnRoleActivationAlertConfiguration]] = Field(alias="value",default=None,)

from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration

