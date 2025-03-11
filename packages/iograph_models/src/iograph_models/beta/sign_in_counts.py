from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SignInCounts(BaseModel):
	noSignIn: Optional[int] = Field(alias="noSignIn",default=None,)
	withSignIn: Optional[int] = Field(alias="withSignIn",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


