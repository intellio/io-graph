from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Export_mobile_configGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


