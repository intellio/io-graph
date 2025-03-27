from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ZebraFotaArtifact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	boardSupportPackageVersion: Optional[str] = Field(alias="boardSupportPackageVersion", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	patchVersion: Optional[str] = Field(alias="patchVersion", default=None,)
	releaseNotesUrl: Optional[str] = Field(alias="releaseNotesUrl", default=None,)


