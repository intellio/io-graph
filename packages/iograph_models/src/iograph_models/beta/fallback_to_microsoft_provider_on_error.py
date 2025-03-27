from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class FallbackToMicrosoftProviderOnError(BaseModel):
	odata_type: Literal["#microsoft.graph.fallbackToMicrosoftProviderOnError"] = Field(alias="@odata.type", default="#microsoft.graph.fallbackToMicrosoftProviderOnError")


