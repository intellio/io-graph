from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AwsAssociatedIdentities(BaseModel):
	all: Optional[list[Annotated[Union[AwsAccessKey, AwsEc2Instance, AwsGroup, AwsLambda, AwsRole, AwsUser]],Field(discriminator="odata_type")]]] = Field(alias="all", default=None,)
	roles: Optional[list[AwsRole]] = Field(alias="roles", default=None,)
	users: Optional[list[AwsUser]] = Field(alias="users", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .aws_access_key import AwsAccessKey
from .aws_ec2_instance import AwsEc2Instance
from .aws_group import AwsGroup
from .aws_lambda import AwsLambda
from .aws_role import AwsRole
from .aws_user import AwsUser
from .aws_role import AwsRole
from .aws_user import AwsUser

