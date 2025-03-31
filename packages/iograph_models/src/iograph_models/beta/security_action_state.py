from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityActionState(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	user: Optional[str] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .operation_status import OperationStatus
