from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsStatement(BaseModel):
	actions: Optional[list[str]] = Field(alias="actions",default=None,)
	condition: Optional[AwsCondition] = Field(alias="condition",default=None,)
	effect: Optional[AwsStatementEffect | str] = Field(alias="effect",default=None,)
	notActions: Optional[list[str]] = Field(alias="notActions",default=None,)
	notResources: Optional[list[str]] = Field(alias="notResources",default=None,)
	resources: Optional[list[str]] = Field(alias="resources",default=None,)
	statementId: Optional[str] = Field(alias="statementId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .aws_condition import AwsCondition
from .aws_statement_effect import AwsStatementEffect

