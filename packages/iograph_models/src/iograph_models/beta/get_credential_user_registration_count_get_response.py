from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_credential_user_registration_countGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CredentialUserRegistrationCount]] = Field(alias="value", default=None,)

from .credential_user_registration_count import CredentialUserRegistrationCount
