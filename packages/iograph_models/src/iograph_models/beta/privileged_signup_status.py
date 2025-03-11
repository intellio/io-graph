from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedSignupStatus(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isRegistered: Optional[bool] = Field(alias="isRegistered",default=None,)
	status: Optional[SetupStatus | str] = Field(alias="status",default=None,)

from .setup_status import SetupStatus

