from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	acl: Optional[list[Acl]] = Field(alias="acl",default=None,)
	content: Optional[ExternalItemContent] = Field(alias="content",default=None,)
	properties: Optional[Properties] = Field(alias="properties",default=None,)

from .acl import Acl
from .external_item_content import ExternalItemContent
from .properties import Properties

