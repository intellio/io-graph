from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_statusPostRequest(BaseModel):
	status: Optional[DeviceAppManagementTaskStatus | str] = Field(alias="status", default=None,)
	note: Optional[str] = Field(alias="note", default=None,)

from .device_app_management_task_status import DeviceAppManagementTaskStatus
