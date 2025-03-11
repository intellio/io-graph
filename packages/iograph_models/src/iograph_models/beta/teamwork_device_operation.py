from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDeviceOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[OperationError] = Field(alias="error",default=None,)
	lastActionBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastActionBy",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	operationType: Optional[TeamworkDeviceOperationType | str] = Field(alias="operationType",default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)

from .identity_set import IdentitySet
from .operation_error import OperationError
from .identity_set import IdentitySet
from .teamwork_device_operation_type import TeamworkDeviceOperationType

