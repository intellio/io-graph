from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_device_log_collection_requestPostRequest(BaseModel):
	templateType: Optional[DeviceLogCollectionRequest] = Field(alias="templateType",default=None,)

from .device_log_collection_request import DeviceLogCollectionRequest

