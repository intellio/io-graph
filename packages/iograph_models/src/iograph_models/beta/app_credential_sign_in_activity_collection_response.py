from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppCredentialSignInActivityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppCredentialSignInActivity]] = Field(alias="value", default=None,)

from .app_credential_sign_in_activity import AppCredentialSignInActivity
