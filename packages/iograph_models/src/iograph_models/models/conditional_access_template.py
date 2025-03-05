from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	details: Optional[ConditionalAccessPolicyDetail] = Field(alias="details",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	scenarios: Optional[str | TemplateScenarios] = Field(alias="scenarios",default=None,)

from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
from .template_scenarios import TemplateScenarios

