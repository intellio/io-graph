from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NoEntitlementsDataCollection(BaseModel):
	odata_type: Literal["#microsoft.graph.noEntitlementsDataCollection"] = Field(alias="@odata.type", default="#microsoft.graph.noEntitlementsDataCollection")


