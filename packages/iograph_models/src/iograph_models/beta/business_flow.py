from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BusinessFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.businessFlow"] = Field(alias="@odata.type", default="#microsoft.graph.businessFlow")
	customData: Optional[str] = Field(alias="customData", default=None,)
	deDuplicationId: Optional[str] = Field(alias="deDuplicationId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	policy: Optional[GovernancePolicy] = Field(alias="policy", default=None,)
	policyTemplateId: Optional[str] = Field(alias="policyTemplateId", default=None,)
	recordVersion: Optional[str] = Field(alias="recordVersion", default=None,)
	schemaId: Optional[str] = Field(alias="schemaId", default=None,)
	settings: Optional[BusinessFlowSettings] = Field(alias="settings", default=None,)

from .governance_policy import GovernancePolicy
from .business_flow_settings import BusinessFlowSettings
