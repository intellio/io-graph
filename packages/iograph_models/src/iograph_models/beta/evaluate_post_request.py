from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluatePostRequest(BaseModel):
	discoveredSensitiveTypes: Optional[list[DiscoveredSensitiveType]] = Field(alias="discoveredSensitiveTypes", default=None,)
	currentLabel: Optional[CurrentLabel] = Field(alias="currentLabel", default=None,)

from .discovered_sensitive_type import DiscoveredSensitiveType
from .current_label import CurrentLabel

