from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasskeyAuthenticationMethodTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PasskeyAuthenticationMethodTarget]] = Field(alias="value", default=None,)

from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget

