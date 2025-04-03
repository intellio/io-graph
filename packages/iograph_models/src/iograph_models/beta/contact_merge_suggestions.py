from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ContactMergeSuggestions(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contactMergeSuggestions"] = Field(alias="@odata.type", default="#microsoft.graph.contactMergeSuggestions")
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)

