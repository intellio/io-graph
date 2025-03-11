from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemAccessOperationsViewpoint(BaseModel):
	canComment: Optional[bool] = Field(alias="canComment",default=None,)
	canCreateFile: Optional[bool] = Field(alias="canCreateFile",default=None,)
	canCreateFolder: Optional[bool] = Field(alias="canCreateFolder",default=None,)
	canDelete: Optional[bool] = Field(alias="canDelete",default=None,)
	canDownload: Optional[bool] = Field(alias="canDownload",default=None,)
	canRead: Optional[bool] = Field(alias="canRead",default=None,)
	canUpdate: Optional[bool] = Field(alias="canUpdate",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


