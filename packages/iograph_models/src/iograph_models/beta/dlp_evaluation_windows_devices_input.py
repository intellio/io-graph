from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DlpEvaluationWindowsDevicesInput(BaseModel):
	currentLabel: Optional[CurrentLabel] = Field(alias="currentLabel", default=None,)
	discoveredSensitiveTypes: Optional[list[DiscoveredSensitiveType]] = Field(alias="discoveredSensitiveTypes", default=None,)
	odata_type: Literal["#microsoft.graph.dlpEvaluationWindowsDevicesInput"] = Field(alias="@odata.type", default="#microsoft.graph.dlpEvaluationWindowsDevicesInput")
	contentProperties: Optional[ContentProperties] = Field(alias="contentProperties", default=None,)
	sharedBy: Optional[str] = Field(alias="sharedBy", default=None,)

from .current_label import CurrentLabel
from .discovered_sensitive_type import DiscoveredSensitiveType
from .content_properties import ContentProperties
