from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Wipe_managed_app_registrations_by_azure_ad_device_idPostRequest(BaseModel):
	azureAdDeviceId: Optional[str] = Field(alias="azureAdDeviceId", default=None,)


