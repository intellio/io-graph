from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_password_single_sign_on_credentialsPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PasswordSingleSignOnCredentialSet]] = Field(alias="value", default=None,)

from .password_single_sign_on_credential_set import PasswordSingleSignOnCredentialSet

