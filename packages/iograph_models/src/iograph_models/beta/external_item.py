from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalItem"] = Field(alias="@odata.type",)
	acl: Optional[list[Acl]] = Field(alias="acl", default=None,)
	content: Optional[ExternalItemContent] = Field(alias="content", default=None,)
	properties: Optional[Properties] = Field(alias="properties", default=None,)

from .acl import Acl
from .external_item_content import ExternalItemContent
from .properties import Properties
