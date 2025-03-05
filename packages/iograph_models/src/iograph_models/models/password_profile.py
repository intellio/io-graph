from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordProfile(BaseModel):
	forceChangePasswordNextSignIn: Optional[bool] = Field(default=None,alias="forceChangePasswordNextSignIn",)
	forceChangePasswordNextSignInWithMfa: Optional[bool] = Field(default=None,alias="forceChangePasswordNextSignInWithMfa",)
	password: Optional[str] = Field(default=None,alias="password",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


