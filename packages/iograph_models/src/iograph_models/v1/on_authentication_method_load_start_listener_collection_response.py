from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAuthenticationMethodLoadStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OnAuthenticationMethodLoadStartListener]] = Field(alias="value", default=None,)

from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener

