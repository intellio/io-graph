from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationCount(BaseModel):
	registrationCount: Optional[int] = Field(alias="registrationCount",default=None,)
	registrationStatus: Optional[RegistrationStatusType | str] = Field(alias="registrationStatus",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .registration_status_type import RegistrationStatusType

