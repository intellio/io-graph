from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NoMfaOnRoleActivationAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NoMfaOnRoleActivationAlertIncident]] = Field(alias="value",default=None,)

from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident

