from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsHelloForBusinessAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsHelloForBusinessAuthenticationMethod]] = Field(alias="value", default=None,)

from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

