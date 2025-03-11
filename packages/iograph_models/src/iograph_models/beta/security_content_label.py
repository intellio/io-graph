from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityContentLabel(BaseModel):
	assignmentMethod: Optional[SecurityAssignmentMethod | str] = Field(alias="assignmentMethod",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	sensitivityLabelId: Optional[str] = Field(alias="sensitivityLabelId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_assignment_method import SecurityAssignmentMethod

