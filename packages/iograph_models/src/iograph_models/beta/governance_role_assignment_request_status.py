from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GovernanceRoleAssignmentRequestStatus(BaseModel):
	status: Optional[str] = Field(alias="status", default=None,)
	statusDetails: Optional[list[KeyValue]] = Field(alias="statusDetails", default=None,)
	subStatus: Optional[str] = Field(alias="subStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .key_value import KeyValue
