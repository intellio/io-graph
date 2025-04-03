from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityRulesRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.rulesRoot"] = Field(alias="@odata.type", default="#microsoft.graph.security.rulesRoot")
	detectionRules: Optional[list[SecurityDetectionRule]] = Field(alias="detectionRules", default=None,)

from .security_detection_rule import SecurityDetectionRule
