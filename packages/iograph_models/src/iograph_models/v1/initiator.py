from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Initiator(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.initiator"] = Field(alias="@odata.type", default="#microsoft.graph.initiator")
	initiatorType: Optional[InitiatorType | str] = Field(alias="initiatorType", default=None,)

from .initiator_type import InitiatorType

