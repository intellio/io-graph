from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentWorkflowExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessPackageAssignmentWorkflowExtension]] = Field(alias="value", default=None,)

from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension

