from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Wipe_managed_app_registrations_by_device_tagPostRequest(BaseModel):
	deviceTag: Optional[str] = Field(alias="deviceTag",default=None,)


