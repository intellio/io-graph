from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAlertTemplate(BaseModel):
	category: Optional[str] = Field(alias="category",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	impactedAssets: SerializeAsAny[Optional[list[SecurityImpactedAsset]]] = Field(alias="impactedAssets",default=None,)
	mitreTechniques: Optional[list[str]] = Field(alias="mitreTechniques",default=None,)
	recommendedActions: Optional[str] = Field(alias="recommendedActions",default=None,)
	severity: Optional[SecurityAlertSeverity | str] = Field(alias="severity",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_impacted_asset import SecurityImpactedAsset
from .security_alert_severity import SecurityAlertSeverity

