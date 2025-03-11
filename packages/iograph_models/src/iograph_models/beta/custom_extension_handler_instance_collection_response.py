from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionHandlerInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CustomExtensionHandlerInstance]] = Field(alias="value",default=None,)

from .custom_extension_handler_instance import CustomExtensionHandlerInstance

