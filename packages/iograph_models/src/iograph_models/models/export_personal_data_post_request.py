from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Export_personal_dataPostRequest(BaseModel):
	storageLocation: Optional[str] = Field(alias="storageLocation",default=None,)


