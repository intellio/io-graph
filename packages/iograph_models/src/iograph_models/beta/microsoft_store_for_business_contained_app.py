from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftStoreForBusinessContainedApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftStoreForBusinessContainedApp"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftStoreForBusinessContainedApp")
	appUserModelId: Optional[str] = Field(alias="appUserModelId", default=None,)


