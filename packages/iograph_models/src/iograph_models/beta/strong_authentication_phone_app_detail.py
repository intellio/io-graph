from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class StrongAuthenticationPhoneAppDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.strongAuthenticationPhoneAppDetail"] = Field(alias="@odata.type",)
	authenticationType: Optional[str] = Field(alias="authenticationType", default=None,)
	authenticatorFlavor: Optional[str] = Field(alias="authenticatorFlavor", default=None,)
	deviceId: Optional[UUID] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag", default=None,)
	deviceToken: Optional[str] = Field(alias="deviceToken", default=None,)
	hashFunction: Optional[str] = Field(alias="hashFunction", default=None,)
	lastAuthenticatedDateTime: Optional[datetime] = Field(alias="lastAuthenticatedDateTime", default=None,)
	notificationType: Optional[str] = Field(alias="notificationType", default=None,)
	oathSecretKey: Optional[str] = Field(alias="oathSecretKey", default=None,)
	oathTokenMetadata: Optional[OathTokenMetadata] = Field(alias="oathTokenMetadata", default=None,)
	oathTokenTimeDriftInSeconds: Optional[int] = Field(alias="oathTokenTimeDriftInSeconds", default=None,)
	phoneAppVersion: Optional[str] = Field(alias="phoneAppVersion", default=None,)
	tenantDeviceId: Optional[str] = Field(alias="tenantDeviceId", default=None,)
	tokenGenerationIntervalInSeconds: Optional[int] = Field(alias="tokenGenerationIntervalInSeconds", default=None,)

from .oath_token_metadata import OathTokenMetadata
