from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordProfile(BaseModel):
	forceChangePasswordNextSignIn: Optional[bool] = Field(alias="forceChangePasswordNextSignIn",default=None,)
	forceChangePasswordNextSignInWithMfa: Optional[bool] = Field(alias="forceChangePasswordNextSignInWithMfa",default=None,)
	password: Optional[str] = Field(alias="password",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


