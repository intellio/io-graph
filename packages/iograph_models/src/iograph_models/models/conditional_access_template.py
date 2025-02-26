from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	details: Optional[ConditionalAccessPolicyDetail] = Field(default=None,alias="details",)
	name: Optional[str] = Field(default=None,alias="name",)
	scenarios: Optional[TemplateScenarios] = Field(default=None,alias="scenarios",)

from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
from .template_scenarios import TemplateScenarios

