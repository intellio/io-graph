from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EncryptedAwsStorageBucketFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.encryptedAwsStorageBucketFinding"] = Field(alias="@odata.type", default="#microsoft.graph.encryptedAwsStorageBucketFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibility: Optional[AwsAccessType | str] = Field(alias="accessibility", default=None,)
	storageBucket: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="storageBucket", default=None,discriminator="odata_type", )

from .aws_access_type import AwsAccessType
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
