from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ZebraFotaArtifact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.zebraFotaArtifact"] = Field(alias="@odata.type",)
	boardSupportPackageVersion: Optional[str] = Field(alias="boardSupportPackageVersion", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	patchVersion: Optional[str] = Field(alias="patchVersion", default=None,)
	releaseNotesUrl: Optional[str] = Field(alias="releaseNotesUrl", default=None,)

