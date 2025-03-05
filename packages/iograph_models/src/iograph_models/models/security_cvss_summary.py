from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCvssSummary(BaseModel):
	score: float | str | ReferenceNumeric
	severity: Optional[SecurityVulnerabilitySeverity] = Field(default=None,alias="severity",)
	vectorString: Optional[str] = Field(default=None,alias="vectorString",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .security_vulnerability_severity import SecurityVulnerabilitySeverity

