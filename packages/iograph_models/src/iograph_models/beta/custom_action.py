from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomAction(BaseModel):
	odata_type: Literal["#microsoft.graph.customAction"] = Field(alias="@odata.type", default="#microsoft.graph.customAction")
	name: Optional[str] = Field(alias="name", default=None,)
	properties: Optional[list[KeyValuePair]] = Field(alias="properties", default=None,)

from .key_value_pair import KeyValuePair
