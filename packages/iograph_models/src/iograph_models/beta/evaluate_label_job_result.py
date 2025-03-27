from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluateLabelJobResult(BaseModel):
	responsiblePolicy: Optional[ResponsiblePolicy] = Field(alias="responsiblePolicy", default=None,)
	responsibleSensitiveTypes: Optional[list[ResponsibleSensitiveType]] = Field(alias="responsibleSensitiveTypes", default=None,)
	sensitivityLabel: Optional[MatchingLabel] = Field(alias="sensitivityLabel", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .responsible_policy import ResponsiblePolicy
from .responsible_sensitive_type import ResponsibleSensitiveType
from .matching_label import MatchingLabel

