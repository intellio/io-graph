from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRulesRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	detectionRules: Optional[list[SecurityDetectionRule]] = Field(alias="detectionRules", default=None,)

from .security_detection_rule import SecurityDetectionRule

