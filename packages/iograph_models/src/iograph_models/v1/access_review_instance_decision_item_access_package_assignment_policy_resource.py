from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessPackageDisplayName: Optional[str] = Field(alias="accessPackageDisplayName",default=None,)
	accessPackageId: Optional[str] = Field(alias="accessPackageId",default=None,)


