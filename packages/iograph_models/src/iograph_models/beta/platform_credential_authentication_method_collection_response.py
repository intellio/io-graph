from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlatformCredentialAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PlatformCredentialAuthenticationMethod]] = Field(alias="value",default=None,)

from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod

