from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Assign_and_activate_by_serial_numberPostRequest(BaseModel):
	verificationCode: Optional[str] = Field(alias="verificationCode", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

