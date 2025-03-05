from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCvssSummary(BaseModel):
	score: float | str | ReferenceNumeric
	severity: Optional[SecurityVulnerabilitySeverity | str] = Field(alias="severity",default=None,)
	vectorString: Optional[str] = Field(alias="vectorString",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric
from .security_vulnerability_severity import SecurityVulnerabilitySeverity

