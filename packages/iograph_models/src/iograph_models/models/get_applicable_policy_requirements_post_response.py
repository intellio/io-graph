from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_applicable_policy_requirementsPostResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AccessPackageAssignmentRequestRequirements]] = Field(default=None,alias="value",)

from .access_package_assignment_request_requirements import AccessPackageAssignmentRequestRequirements

