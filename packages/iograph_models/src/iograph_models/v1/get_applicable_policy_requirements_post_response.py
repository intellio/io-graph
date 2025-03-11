from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_applicable_policy_requirementsPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AccessPackageAssignmentRequestRequirements]] = Field(alias="value",default=None,)

from .access_package_assignment_request_requirements import AccessPackageAssignmentRequestRequirements

