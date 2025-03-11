from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExternallyAccessibleAwsStorageBucketFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	accessibility: Optional[AwsAccessType | str] = Field(alias="accessibility",default=None,)
	accountsWithAccess: SerializeAsAny[Optional[AccountsWithAccess]] = Field(alias="accountsWithAccess",default=None,)
	storageBucket: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="storageBucket",default=None,)

from .aws_access_type import AwsAccessType
from .accounts_with_access import AccountsWithAccess
from .authorization_system_resource import AuthorizationSystemResource

