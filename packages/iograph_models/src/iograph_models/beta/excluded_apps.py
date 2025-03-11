from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExcludedApps(BaseModel):
	access: Optional[bool] = Field(alias="access",default=None,)
	bing: Optional[bool] = Field(alias="bing",default=None,)
	excel: Optional[bool] = Field(alias="excel",default=None,)
	groove: Optional[bool] = Field(alias="groove",default=None,)
	infoPath: Optional[bool] = Field(alias="infoPath",default=None,)
	lync: Optional[bool] = Field(alias="lync",default=None,)
	oneDrive: Optional[bool] = Field(alias="oneDrive",default=None,)
	oneNote: Optional[bool] = Field(alias="oneNote",default=None,)
	outlook: Optional[bool] = Field(alias="outlook",default=None,)
	powerPoint: Optional[bool] = Field(alias="powerPoint",default=None,)
	publisher: Optional[bool] = Field(alias="publisher",default=None,)
	sharePointDesigner: Optional[bool] = Field(alias="sharePointDesigner",default=None,)
	teams: Optional[bool] = Field(alias="teams",default=None,)
	visio: Optional[bool] = Field(alias="visio",default=None,)
	word: Optional[bool] = Field(alias="word",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


