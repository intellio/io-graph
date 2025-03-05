from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SignInActivity(BaseModel):
	lastNonInteractiveSignInDateTime: Optional[datetime] = Field(default=None,alias="lastNonInteractiveSignInDateTime",)
	lastNonInteractiveSignInRequestId: Optional[str] = Field(default=None,alias="lastNonInteractiveSignInRequestId",)
	lastSignInDateTime: Optional[datetime] = Field(default=None,alias="lastSignInDateTime",)
	lastSignInRequestId: Optional[str] = Field(default=None,alias="lastSignInRequestId",)
	lastSuccessfulSignInDateTime: Optional[datetime] = Field(default=None,alias="lastSuccessfulSignInDateTime",)
	lastSuccessfulSignInRequestId: Optional[str] = Field(default=None,alias="lastSuccessfulSignInRequestId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


