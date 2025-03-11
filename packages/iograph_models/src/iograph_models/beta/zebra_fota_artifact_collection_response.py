from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ZebraFotaArtifactCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ZebraFotaArtifact]] = Field(alias="value",default=None,)

from .zebra_fota_artifact import ZebraFotaArtifact

