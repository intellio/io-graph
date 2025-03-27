from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedRoleAssignmentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrivilegedRoleAssignmentRequest]] = Field(alias="value", default=None,)

from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest

