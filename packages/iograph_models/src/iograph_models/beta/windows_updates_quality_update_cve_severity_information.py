from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesQualityUpdateCveSeverityInformation(BaseModel):
	maxBaseScore: float | str | ReferenceNumeric
	maxSeverity: Optional[WindowsUpdatesCveSeverityLevel | str] = Field(alias="maxSeverity",default=None,)
	exploitedCves: Optional[list[WindowsUpdatesCveInformation]] = Field(alias="exploitedCves",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric
from .windows_updates_cve_severity_level import WindowsUpdatesCveSeverityLevel
from .windows_updates_cve_information import WindowsUpdatesCveInformation

