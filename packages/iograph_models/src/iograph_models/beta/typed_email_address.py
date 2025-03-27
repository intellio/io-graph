from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TypedEmailAddress(BaseModel):
	address: Optional[str] = Field(alias="address", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.typedEmailAddress"] = Field(alias="@odata.type", default="#microsoft.graph.typedEmailAddress")
	otherLabel: Optional[str] = Field(alias="otherLabel", default=None,)
	type: Optional[EmailType | str] = Field(alias="type", default=None,)

from .email_type import EmailType

