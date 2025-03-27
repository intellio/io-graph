from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsAlertRuleDefinitionTemplate(BaseModel):
	defaultSeverity: Optional[ManagedTenantsAlertSeverity | str] = Field(alias="defaultSeverity", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_alert_severity import ManagedTenantsAlertSeverity

