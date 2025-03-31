from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageNotificationSettings(BaseModel):
	isAssignmentNotificationDisabled: Optional[bool] = Field(alias="isAssignmentNotificationDisabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

