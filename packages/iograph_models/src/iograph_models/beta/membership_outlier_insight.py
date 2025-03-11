from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MembershipOutlierInsight(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	insightCreatedDateTime: Optional[datetime] = Field(alias="insightCreatedDateTime",default=None,)
	containerId: Optional[str] = Field(alias="containerId",default=None,)
	memberId: Optional[str] = Field(alias="memberId",default=None,)
	outlierContainerType: Optional[OutlierContainerType | str] = Field(alias="outlierContainerType",default=None,)
	outlierMemberType: Optional[OutlierMemberType | str] = Field(alias="outlierMemberType",default=None,)
	container: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="container",default=None,)
	lastModifiedBy: Optional[User] = Field(alias="lastModifiedBy",default=None,)
	member: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="member",default=None,)

from .outlier_container_type import OutlierContainerType
from .outlier_member_type import OutlierMemberType
from .directory_object import DirectoryObject
from .user import User
from .directory_object import DirectoryObject

