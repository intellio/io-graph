from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPhone81AppXBundleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsPhone81AppXBundle]] = Field(alias="value", default=None,)

from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

