from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignUpIdentity(BaseModel):
	signUpIdentifier: Optional[str] = Field(alias="signUpIdentifier", default=None,)
	signUpIdentifierType: Optional[SignUpIdentifierType | str] = Field(alias="signUpIdentifierType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sign_up_identifier_type import SignUpIdentifierType
