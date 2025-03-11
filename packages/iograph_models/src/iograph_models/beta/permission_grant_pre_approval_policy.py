from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantPreApprovalPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	conditions: Optional[list[PreApprovalDetail]] = Field(alias="conditions",default=None,)

from .pre_approval_detail import PreApprovalDetail

