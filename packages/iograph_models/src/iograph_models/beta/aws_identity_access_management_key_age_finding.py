from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AwsIdentityAccessManagementKeyAgeFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	actionSummary: Optional[ActionSummary] = Field(alias="actionSummary",default=None,)
	awsAccessKeyDetails: Optional[AwsAccessKeyDetails] = Field(alias="awsAccessKeyDetails",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	status: Optional[IamStatus | str] = Field(alias="status",default=None,)
	accessKey: Optional[AwsAccessKey] = Field(alias="accessKey",default=None,)

from .action_summary import ActionSummary
from .aws_access_key_details import AwsAccessKeyDetails
from .permissions_creep_index import PermissionsCreepIndex
from .iam_status import IamStatus
from .aws_access_key import AwsAccessKey

