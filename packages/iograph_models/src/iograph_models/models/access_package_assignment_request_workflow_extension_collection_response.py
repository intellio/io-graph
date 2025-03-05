from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequestWorkflowExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AccessPackageAssignmentRequestWorkflowExtension]] = Field(default=None,alias="value",)

from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension

