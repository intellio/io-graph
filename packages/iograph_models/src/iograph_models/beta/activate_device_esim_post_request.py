from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Activate_device_esimPostRequest(BaseModel):
	carrierUrl: Optional[str] = Field(alias="carrierUrl", default=None,)

