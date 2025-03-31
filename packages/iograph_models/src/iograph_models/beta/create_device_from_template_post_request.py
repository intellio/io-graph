from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Create_device_from_templatePostRequest(BaseModel):
	externalDeviceId: Optional[str] = Field(alias="externalDeviceId", default=None,)
	operatingSystemVersion: Optional[str] = Field(alias="operatingSystemVersion", default=None,)
	externalSourceName: Optional[str] = Field(alias="externalSourceName", default=None,)
	keyCredential: Optional[KeyCredential] = Field(alias="keyCredential", default=None,)
	accountEnabled: Optional[bool] = Field(alias="accountEnabled", default=None,)
	alternativeNames: Optional[list[str]] = Field(alias="alternativeNames", default=None,)

from .key_credential import KeyCredential
