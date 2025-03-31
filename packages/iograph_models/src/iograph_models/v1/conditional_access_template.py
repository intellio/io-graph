from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConditionalAccessTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.conditionalAccessTemplate"] = Field(alias="@odata.type",)
	description: Optional[str] = Field(alias="description", default=None,)
	details: Optional[ConditionalAccessPolicyDetail] = Field(alias="details", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	scenarios: Optional[TemplateScenarios | str] = Field(alias="scenarios", default=None,)

from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
from .template_scenarios import TemplateScenarios
