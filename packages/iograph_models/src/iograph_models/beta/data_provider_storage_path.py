from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataProviderStoragePath(BaseModel):
	containerName: Optional[str] = Field(alias="containerName", default=None,)
	dataProviderId: Optional[str] = Field(alias="dataProviderId", default=None,)
	path: Optional[str] = Field(alias="path", default=None,)
	storageAccountName: Optional[str] = Field(alias="storageAccountName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


