from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudLicensingService(BaseModel):
	assignableTo: Optional[CloudLicensingAssigneeTypes | str] = Field(alias="assignableTo",default=None,)
	planId: Optional[UUID] = Field(alias="planId",default=None,)
	planName: Optional[str] = Field(alias="planName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_licensing_assignee_types import CloudLicensingAssigneeTypes

