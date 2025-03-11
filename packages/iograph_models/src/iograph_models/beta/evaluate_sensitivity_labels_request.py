from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluateSensitivityLabelsRequest(BaseModel):
	currentLabel: Optional[CurrentLabel] = Field(alias="currentLabel",default=None,)
	discoveredSensitiveTypes: Optional[list[DiscoveredSensitiveType]] = Field(alias="discoveredSensitiveTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .current_label import CurrentLabel
from .discovered_sensitive_type import DiscoveredSensitiveType

