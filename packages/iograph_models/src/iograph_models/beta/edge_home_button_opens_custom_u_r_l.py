from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EdgeHomeButtonOpensCustomURL(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeHomeButtonOpensCustomURL"] = Field(alias="@odata.type", default="#microsoft.graph.edgeHomeButtonOpensCustomURL")
	homeButtonCustomURL: Optional[str] = Field(alias="homeButtonCustomURL", default=None,)


