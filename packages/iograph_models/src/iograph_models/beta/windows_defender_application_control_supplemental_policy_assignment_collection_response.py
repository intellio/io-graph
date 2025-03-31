from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsDefenderApplicationControlSupplementalPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = Field(alias="value", default=None,)

from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
