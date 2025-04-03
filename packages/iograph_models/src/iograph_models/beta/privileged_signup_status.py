from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrivilegedSignupStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedSignupStatus"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedSignupStatus")
	isRegistered: Optional[bool] = Field(alias="isRegistered", default=None,)
	status: Optional[SetupStatus | str] = Field(alias="status", default=None,)

from .setup_status import SetupStatus
