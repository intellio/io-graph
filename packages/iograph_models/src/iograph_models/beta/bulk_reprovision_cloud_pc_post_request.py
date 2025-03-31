from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bulk_reprovision_cloud_pcPostRequest(BaseModel):
	managedDeviceIds: Optional[list[str]] = Field(alias="managedDeviceIds", default=None,)

