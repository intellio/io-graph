from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessPackageDisplayName: Optional[str] = Field(default=None,alias="accessPackageDisplayName",)
	accessPackageId: Optional[str] = Field(default=None,alias="accessPackageId",)


