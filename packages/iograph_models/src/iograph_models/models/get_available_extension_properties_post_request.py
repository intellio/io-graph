from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_available_extension_propertiesPostRequest(BaseModel):
	isSyncedFromOnPremises: Optional[bool] = Field(default=None,alias="isSyncedFromOnPremises",)


