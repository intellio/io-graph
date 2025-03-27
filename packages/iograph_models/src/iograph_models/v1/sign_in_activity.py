from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SignInActivity(BaseModel):
	lastNonInteractiveSignInDateTime: Optional[datetime] = Field(alias="lastNonInteractiveSignInDateTime", default=None,)
	lastNonInteractiveSignInRequestId: Optional[str] = Field(alias="lastNonInteractiveSignInRequestId", default=None,)
	lastSignInDateTime: Optional[datetime] = Field(alias="lastSignInDateTime", default=None,)
	lastSignInRequestId: Optional[str] = Field(alias="lastSignInRequestId", default=None,)
	lastSuccessfulSignInDateTime: Optional[datetime] = Field(alias="lastSuccessfulSignInDateTime", default=None,)
	lastSuccessfulSignInRequestId: Optional[str] = Field(alias="lastSuccessfulSignInRequestId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


